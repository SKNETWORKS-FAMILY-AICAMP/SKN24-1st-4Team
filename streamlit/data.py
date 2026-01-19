import streamlit as st
import pandas as pd

# 여기는 db연결하는 곳
def faq_data():
    conn = st.connection('mysql', type='sql')
    faq = conn.query('SELECT * FROM tbl_faq;', ttl=600)
    return faq

# 1) 구의 월별 속도비율
# (해당 구의 월별 모든 평균속도/구별 모든 제한 속도)*100
def get_gu_congestion(gu_name, month):
    conn = st.connection('mysql', type='sql')
    query = f"""
        SELECT 
            SUM(s.speed_limit) as total_limit_speed, -- 제한 총합
            SUM(c.average_speed) as total_avg_speed, -- 평균속도 총합
            ROUND((SUM(c.average_speed) / SUM(s.speed_limit)) * 100, 1) AS gu_congestion -- 혼잡도
        FROM tbl_road r
        JOIN tbl_speed_limit s ON r.road_id = s.road_code
        JOIN tbl_congestion c ON r.road_id = c.road_code
        WHERE r.registed_region = '{gu_name}' 
        AND c.date_id = {month};
    """
    summary = conn.query(query, ttl=600)
    return summary

# 구의 월별 차량 밀도
# (해당 구의 월별 등록대수/해당구에 속하는 모든 도로의 길이)

# 구의 월별 차량 밀도 값이 잘 안나와서 각각 뽑아서 계산
# 구 안겹치게 겹치는거 카운트해서 나눠주기
# 1. (해당 구에 속하는 모든 도로의 길이)
def get_gu_total_road_length(gu_name):
    conn = st.connection('mysql', type='sql')
    query = f"""
        SELECT 
            ROUND(SUM(road_distance) / COUNT(*), 2) AS avg_distance  -- 평균 길이
        FROM (
            SELECT DISTINCT 
                road_name, 
                start_point, 
                end_point, 
                road_distance
            FROM tbl_road 
            WHERE registed_region = '{gu_name}'
        ) AS distinct_roads;
    """
    summary = conn.query(query, ttl=600)
    return summary


# 2. (해당 구의 월별 등록대수)
def get_gu_resgisted_car(gu_name, month):
    conn = st.connection('mysql', type='sql')
    query = f"""
    SELECT registed_car_num
        FROM tbl_registed_car
        WHERE registed_region = '{gu_name}'
        AND registed_month = '{month}'
    """
    summary = conn.query(query, ttl=600)
    return summary

# 도로별, 월별 혼잡도 지수
# (도로별, 월별 평균속도/도로별 제한속도)
def get_road_congestion(road_name, month):
    conn = st.connection('mysql', type='sql')
    # 1. 특정 도로의 제한속도와 그 달의 평균 속도를 가져옵니다.
    # 2. (평균속도들의 평균 / 제한속도들의 평균) * 100 으로 지수를 만듭니다.
    # 상행 하행 둘다 나옵니다.
    query = f"""
        SELECT 
            r.road_name,
            r.derection,
            ROUND(AVG(b.speed_limit), 1) AS avg_speed_limit, -- 제한속도
            ROUND(AVG(c.average_speed), 1) AS avg_average_speed, -- 평균속도
            ROUND(AVG(c.average_speed / b.speed_limit) * 100, 1) AS road_congestion
        FROM tbl_road r
        JOIN tbl_speed_limit b ON r.road_id = b.road_code
        JOIN tbl_congestion c ON r.road_id = c.road_code
        WHERE r.road_name = '{road_name}'
        AND c.date_id = {month}
        GROUP BY r.road_name, r.derection;
    """
    summary = conn.query(query, ttl=600)

    return summary


# 구별 모든 도로 출력(안겹치게 조건 넣음)
def road(gu_name):
    conn = st.connection('mysql', type='sql')
    query = f"""
        SELECT road_name
        FROM tbl_road
        WHERE registed_region = '{gu_name}'
        AND derection = '상행'
        GROUP BY registed_region, road_name, derection
    """
    summary = conn.query(query, ttl=600)
    return summary

