# 수영님이 주신 것

import pandas as pd
from sqlalchemy import create_engine

# 1) 엑셀 파일 경로
EXCEL_PATH = "car_reg_20260116.xlsx"   
SHEET_NAME = '데이터'                     

# 2) MySQL 접속 정보
USER = "ohgiraffers"
PASSWORD = "1234"             
HOST = "localhost"             
PORT = 3306
DB = "cardb"

# 3) 엑셀 읽기
df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

# 4) 컬럼명 정리 (엑셀 헤더에 공백 있으면 제거)
df.columns = df.columns.str.strip()

# 여기서 엑셀 컬럼명을 MySQL 컬럼으로 맞추기
# 예시) 엑셀 컬럼이 ['자치구','등록월','등록차량수'] 
rename_map = {
    "자치구": "registed_region",
    "등록 월": "registed_month",
    "등록월": "registed_month",
    "등록 차량 수": "registed_car_num",
    "등록차량수": "registed_car_num",
}
df = df.rename(columns=rename_map)

# 5) 필요한 컬럼만 남기기
df = df[["registed_region", "registed_month", "registed_car_num"]]

# 6) 자료형 정리
df["registed_region"] = df["registed_region"].astype(str).str.strip()
df["registed_month"] = df["registed_month"].astype(str).str.strip()

# 숫자에 쉼표 있는 경우 대비
df["registed_car_num"] = (
    df["registed_car_num"].astype(str).str.replace(",", "", regex=False)
)
df["registed_car_num"] = pd.to_numeric(df["registed_car_num"], errors="coerce").fillna(0).astype(int)

# 7) 중복 제거 (PK 충돌 방지)
df = df.drop_duplicates(subset=["registed_region", "registed_month"], keep="last")

# 8) MySQL로 적재
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}?charset=utf8mb4")

# if_exists:
# - 'append' : 계속 추가
# - 'replace': 테이블 통째로 갈아엎음(주의)
df.to_sql("tbl_registed_car", con=engine, if_exists="append", index=False)

print("업로드 완료! 행 개수:", len(df))
