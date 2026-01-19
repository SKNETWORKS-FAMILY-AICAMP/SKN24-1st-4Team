import pandas as pd
import mysql.connector
import os
import glob

connection = mysql.connector.connect(
    host="localhost",           # mysql 서버 주소 (ip)
    user="ohgiraffers",         # 사용자 이름
    password="ohgiraffers",     # 비밀번호
    database="traffic"           # 사용할 DB 스키마
)
cursor = connection.cursor()

# 서버연결 성공 여부 판독
if connection.is_connected():
    print("mysql connect complete")

sql = """
insert into tbl_road (
    road_id,
    registed_region,
    road_name,
    start_point,
    end_point,
    derection)
values (%s ,%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
  registed_region=VALUES(registed_region),
  road_name=VALUES(road_name),
  start_point=VALUES(start_point),
  end_point=VALUES(end_point),
  derection=VALUES(derection);
"""

data_dir = "../../data"
excel_files = glob.glob(os.path.join(data_dir, "*서울시 차량통행속도.xlsx"))


for path in excel_files:
    filename = os.path.basename(path)

    year = filename.split("년")[0]                 
    month = filename.split("년")[1].split("월")[0].strip() 
    suffix = f"{year[2:]}{int(month)}"
    
    print(f"처리 중: {os.path.basename(path)} suffix={suffix}")
    # 여기서 pd.read_excel 사용
    df = pd.read_excel(path)
    df["일자"] = df["일자"].astype(int)
    # 파일마다 첫 일자(보통 그 달 1일)
    first_day = int(df["일자"].min())

    road_df = (
        df[df["일자"] == first_day][
            ["링크아이디", "권역구분", "도로명", "시점명", "종점명", "방향"]
        ]
        .drop_duplicates()
        .dropna(subset=["링크아이디"])
        .fillna("")
    )

    rows = [
        (
            int(f"{int(r['링크아이디'])}{suffix}"),
            r["권역구분"],
            r["도로명"],
            r["시점명"],
            r["종점명"],
            r["방향"]
        )
        for _, r in road_df.iterrows()
    ]

    if rows:
        cursor.executemany(sql, rows)
        connection.commit()
        print(f"  → {len(rows)}건 저장 완료")

cursor.close() # 캐시 반환
connection.close() # db 종료