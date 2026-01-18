import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host='localhost', 
    user='ohgiraffers',
    password='ohgiraffers',
    database='traffic'
)

cursor = connection.cursor()

# 엑셀 1시트 읽기
data = pd.read_excel("car1.xlsx", header=None)

# 지역 구분
region = pd.read_excel("car1.xlsx", usecols="B", skiprows=5, nrows=24)

# 1. 날짜별로, 2. 지역별, 차량대수 구하기 중첩 for문
for month_idx in range(24):
    col_index = 2 + (month_idx * 23)
    
    months = data.iloc[0, col_index] #iloc(행,열)
    
    for i in range(24):
        regions = region.iloc[i, 0]
        nums = data.iloc[5 + i, col_index]  
        
        if pd.isna(nums) or nums == '-': # 총계가 -이므로 결측값 대체
            continue
        
        nums = int(nums) # My SQL connector에서 문제자료형에서 추출 가능하도록
        
        sql = 'INSERT INTO tbl_registed_car (registed_region, registed_month, registed_car_num) VALUES (%s, %s, %s)'
        values = (regions, months, nums)
        
        cursor.execute(sql, values)
    
connection.commit() #커밋 후 종료
cursor.close()
connection.close()
