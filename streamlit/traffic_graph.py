import streamlit as st
import pandas as pd
import plotly.express as px
from data import get_gu_congestion, get_road_congestion, road, get_gu_total_road_length, get_gu_resgisted_car
import base64

# 이미지 경로 base64로 변경 url로 넣으면 인식 x
with open("../src/traffic_level.png", "rb") as f:
    img_bytes = f.read()
img_base64 = base64.b64encode(img_bytes).decode()

# URL 파라미터 받기
gu_id = st.query_params.get("gu_id", ["없음"])
gu = st.query_params.get("gu", ["없음"])


roads = road(f'{gu}')
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<style>
    @font-face {
        font-family: 'ChangwonDangamRounded';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2511-1@1.0/ChangwonDangamRound-Regular.woff2') format('woff2');
        font-weight: normal;
    }
    
    a {
        text-decoration: none;
        color: inherit;       
    }

    header {
        color: #0054A2;
        font-family: 'ChangwonDangamRounded';
        height: 60px;
        display: flex;
        align-items: center;
        font-size: 24px;
        width: 100%;
        justify-content: center;
        border-bottom: 1px solid #D3D0D0;
        margin-left: 0px;
    }
            
    header p {
        margin-left: -10px;
    }
            
    .st-emotion-cache-1c87b1z{
        font-family: 'ChangwonDangamRounded';
        color: #0054A2;
        font-size: 18px;
    }
            
    div[data-testid="stSelectbox"] {
        font-family: 'ChangwonDangamRounded';
        width: 170px;
        height: 65px;
        font-size: 32px;
        margin-top: 50px;
        margin-left: 120px;
        padding-bottom: 120px;
    }

    .st-an{
        background-color: #fff;
        color: black;
        border: 1px solid #0054A2;
    }
            
    .st-cy{
        background-color: #ffffff;
        border: none !important;
    }
            
    .st-bt {
        color: black;
    }
            
    .st-cy div div li div, st-emotion-cache-qiev7j, stTooltipHoverTarget{
        color: black !important;
        border: none !important;
    }
            
</style>
<a href="http://localhost:8501" style="text-decoration:none; display:block;"
   onclick="window.location.href=this.href; return false;">
    <header>
        <p>서울특별시&nbsp;<span style="color: #FF7F00">교통&nbsp;</span>혼잡도<p>
    </header>
</a>
""",unsafe_allow_html=True)

st.markdown(f"""
<style>
    .gu {{
        font-family: 'ChangwonDangamRounded';
        color: black;
        font-size: 24px;
        margin-top: 50px;
        margin-left: 120px;
    }}
            
    .st-emotion-cache-qiev7j, stTooltipHoverTarget, ul.st-c8 div, div.st-ao div {{
        color: black !important;
        border: none !important;
    }}
</style>
""",unsafe_allow_html=True)

# 월 리스트

# 2023은 02월부터 있기때문에
months = []
for year in range(2023, 2025):  # 2023, 2024
    if year == 2023:
        months.extend([f"{i:02d}" for i in range(2, 13)]) 
    else:
        months.extend([f"{i:02d}" for i in range(1, 13)])  

years = [f"{i:02d}" for i in range(2023, 2025)]

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
cola, colb, colc, cold, colf = st.columns([0.6, 3, 0.2, 2.2, 4])
# selectbox
with col1:
    selected_years = st.selectbox("연도 선택", years)
with col2:
    selected_month = st.selectbox("월 선택", months)
with col3:
    selected_roads = st.selectbox("도로명 선택", roads)

str_month = selected_years+selected_month
int_month = str_month
db_month = selected_years + ". " + selected_month

# 구별 혼잡도(월별)
gu_congestion_month = get_gu_congestion(f'{gu}', int_month)

# 도로명별 혼잡도(월벌)
road_title_congestion = get_road_congestion(f'{selected_roads}', int_month)

# 해당 구에 속하는 모든 도로의 길이
gu_total_road = get_gu_total_road_length(f'{gu}')
# 해당 구의 월별 등록대수
registed_car = get_gu_resgisted_car(f'{gu}', f'{db_month}')
# 위에 것을 각각 변수에 넣어서
a = gu_total_road.avg_distance.iloc[0]
b = registed_car.registed_car_num.iloc[0]

# 밀도 계산 (해당 구에 속하는 모든 도로의 길이/해당 구의 월별 등록대수)
mil = round(int(b/a), 2)

# 구별 혼잡도 계산식
gu_con_r = round(100 - gu_congestion_month.gu_congestion.iloc[0], 2)

# 차량혼합밀집도
car_mix = round(mil * (gu_con_r / 100), 2)

# 기본 상행 상행과 하행의 차이가 크지 않아 그래프 변화가 없는 것처럼 보일 수 있음
with cold:
    st.markdown("""
    <style>
        .st-emotion-cache-9nevt8 p {
            font-family: 'ChangwonDangamRounded';
            color: black;
        }
        label.st-cz>div.st-d4{
            background-color: blue;
        }
    </style>
    """,unsafe_allow_html=True)
    # 상행 하행 선택
    direction = st.radio("방향 선택", ["상행", "하행"])
# 만약 상행 선택하면 2번째 데이터이기 때문에
if direction == "상행":
    r_avg = road_title_congestion.avg_average_speed.iloc[1]
    r_speed = road_title_congestion.avg_speed_limit.iloc[1]
    r_congestion = 100-road_title_congestion.road_congestion.iloc[1]
else:
    r_avg = road_title_congestion.avg_average_speed.iloc[0]
    r_speed = road_title_congestion.avg_speed_limit.iloc[0]
    r_congestion = 100-road_title_congestion.road_congestion.iloc[0]

# 혼합도 지수
if r_congestion < 20:
    congestion_text = "대체로 원할합니다."
elif 20 <= r_congestion < 40:
    congestion_text = "지체/서행 구간이 자주 발생합니다."
elif 40 <= r_congestion < 60:
    congestion_text = "혼잡이 뚜렷하고 체감상 막힐 수 있습니다."
else: 
    congestion_text = "상시 혼잡 상태입니다."

# 그래프
with colb:
    data = {
        '항목': ['평균속도', '제한속도'],
        '속도': [r_avg, r_speed]
    }
    df = pd.DataFrame(data)

    fig = px.bar(df, x='항목', y='속도', color='항목')

    fig.update_layout(
        height=400,
        width=200,
        showlegend=False,
        bargap=0.7  # 막대 얇게
    )

    st.plotly_chart(fig)
    st.markdown(f"""
    <style>
        div.wrap_hon22{{
            margin-top:50px;
            font-family: 'ChangwonDangamRounded';
            color: black;
            font-size: 24px
        }}
    </style>
    <div class = "wrap_hon22">
            <p style="color: #0054A2;">❗참고사항</p>
            <p>{gu} 차량밀도는 {mil}대/km {car_mix}</p>
    </div>
        """,unsafe_allow_html=True)

# 계산 결과들 도출
with colf:
    st.markdown(f"""
    <style>
        div.wrap_hon{{
            margin-top:-100px;
        }}
        div.hon, div.hon2{{
            color: #0054A2;
            font-size: 32px;
            font-family: 'ChangwonDangamRounded';
            margin-left: -200px;
            text-align:center;
        }}   
        div.hon2{{
            margin-bottom: 50px;

        }}
        div.hon p:nth-child(2){{
            text-align:center;
            font-size: 50px;
            color: #FF7F00;
        }}   
        img.level{{
            margin-top: 100px;
        }}
    </style>
    <div class = "wrap_hon">
        <div class="hon2">
            <p>{selected_years}년 {selected_month}월의</p>
            <p>{gu}의 혼잡도는 <span style="color: #FF7F00">{gu_con_r}%</span>입니다.</p>
        </div>
        <div class="hon">
            <p><span style="color: #FF7F00">{selected_roads}</span>의 혼잡도 수치는?</p>
            <p>{r_congestion}%</p>
            <p>{congestion_text}</p>
            <img src = "data:image/png;base64,{img_base64}" class="level">
        </div>
    </div>
    """,unsafe_allow_html=True)