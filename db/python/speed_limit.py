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
    insert into tbl_speed_limit(
        road_code,
        road_type,
        speed_limit
    ) values (%s, %s, %s)
"""

data_dir = "../../data"

excel_files = glob.glob(os.path.join(data_dir, "*서울시 차량통행속도.xlsx"))
for path in excel_files:
    filename = os.path.basename(path)
    
    year = filename.split("년")[0]                 
    month = filename.split("년")[1].split("월")[0].strip()  
    suffix = f"{year[2:]}{int(month)}"
    
    print(f"처리중: {os.path.basename(path)} suffix={suffix}")

    ars_df = pd.read_excel(path)
    df = pd.DataFrame(ars_df)
    df["일자"] = df["일자"].astype(int)
    first_day = int(df["일자"].min())


    speed_limit_df = (
        df[df["일자"] == first_day][["링크아이디","기능유형구분"]]
        .drop_duplicates()
        .dropna(subset=["링크아이디"])
        .fillna("")
    )

    rows = [
        (int(f"{int(r['링크아이디'])}{suffix}"),
         r["기능유형구분"], 
         100 if r["기능유형구분"] == "도시고속도로" else 60)
        for _, r in speed_limit_df.iterrows()
    ]
    
    if rows:
            cursor.executemany(sql, rows)
            connection.commit()
            print(f"  → {len(rows)}건 저장 완료 (suffix={suffix})")

cursor.close()
connection.close()











