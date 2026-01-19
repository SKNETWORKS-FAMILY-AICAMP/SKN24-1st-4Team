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
    print("@@@ mysql 서버 연결 성공!!! @@@")

sql = """
insert into tbl_congestion (
    road_code, 
    date_id,
    average_speed)
values (%s ,%s ,%s)
ON DUPLICATE KEY UPDATE
  average_speed = VALUES(average_speed);;
"""
# folder_path = '../../data/*.xlsx'
data_dir = "../../data"
excel_files = glob.glob(os.path.join(data_dir, "*서울시 차량통행속도.xlsx"))

for path in excel_files:
    filename = os.path.basename(path)
    year = int(filename.split("년")[0])
    month = int(filename.split("년")[1].split("월")[0].strip())

    suffix = f"{str(year)[2:]}{month}"
    print(f"처리중: {os.path.basename(path)} suffix={suffix}")

    ars_df = pd.read_excel(path)

    df = pd.DataFrame(ars_df)
    df["일자"] = df["일자"].astype(int)
    first_day = int(df["일자"].min())
    
    if month == 28:
        result = -2
    elif month == 29:
        result = -1
    elif month == 30:
        result = 0
    elif month == 31:
        result = 1
    
    result = []
    for s in range(len(df[df["일자"] == first_day])):
        sum_speed = 0
        for r in range(30 + month): # 날짜
            
            day = first_day + r
            day_df = df[df["일자"] == day]
            
            if s >= len(day_df): # 해당 날짜가 없으면 스킵
                continue
            
            for h in range(1,24):
                col = f"{h:02d}시"
                sum_speed += day_df[col].iloc[s]
        date_id_tag = int(str(df.iloc[s]["일자"])[:6])        
        avg_speed = sum_speed/(30 + month) / 24
        road_code_tag = int(f"{int(df.iloc[s]['링크아이디'])}{suffix}")
        
        values = (int(road_code_tag), date_id_tag, float(avg_speed.round(2)))
        result.append(values)
        
    cursor.executemany(sql, result)
    connection.commit()
    print(f"  → {len(result)}건 저장 완료 (suffix={suffix})")


cursor.close() # 캐시 반환
connection.close() # 종료

