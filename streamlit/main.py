import streamlit as st
import streamlit.components.v1 as components
import base64

# 이미지 경로 base64로 변경
with open("../src/map.png", "rb") as f:
    img_bytes = f.read()
img_base64 = base64.b64encode(img_bytes).decode()

main_html = """
<style>
    @font-face {
        font-family: 'ChangwonDangamRounded';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2511-1@1.0/ChangwonDangamRound-Regular.woff2') format('woff2');
        font-weight: normal;
    }

    .stMainBlockContainer {
        width: 1920px;
        overflow: hidden;
    }

    .main_group {
        position: relative;
        width: 1920px;
        font-family: 'ChangwonDangamRounded', sans-serif;
    }

    .main_group_items{
        display: flex;
    }    

    .main_title {
        color: #0054A2;
        font-size: 110px;
        text-align: left;
        margin-left: 100px;
    }
                
    .main_title p:nth-child(2) {
        font-family: 'ChangwonDangamRounded', sans-serif;
        color: #FF7F00;
        font-size: 32px;
        margin-left: 0px;
        text-align: left;
        margin-top: -85px;
    }

    .main_title p:nth-child(3) {
        font-family: 'ChangwonDangamRounded', sans-serif;
        color: black;
        font-size: 24px;
        margin-left: 0px;
        text-align: left;
        margin-top: 165px;
    }
                
    .main_map {
        width: 65%;
    }

    .main_map img {
        width: 90%;
        float: right;
        margin-right:0px;
    }

    .main_group_buttons{
        background-color: black;
    }    

    .main_group_buttons button{
        font-family: 'ChangwonDangamRounded', sans-serif;
        position: absolute;
        display:flex;
        justify-content: center; 
        align-items: center;    
        background-color: #0054A2;
        width: 120px;
        height: 50px;
        font-size: 24px;
        color: white;             
        border-radius: 7px;      
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        border: none;
        outline: none;
    }
    .main_group_buttons .gray_btn {
        background-color: #EFEFEF;
        color: #0054A2;
    }
    .faq_btn { 
        margin-top: -80px;
    }
    .faq_btn button {
        background-color: #0054A2; 
        color: white;
        border-radius: 7px;
        padding: 10px 20px;
        border: none;
        font-family: 'ChangwonDangamRounded';
        font-size: 18px;
        height: 50px;
    }
            
    faq_btn button:hover {
        color: #0054A2; 
        background-color: #EFEFEF;
        border-radius: 7px;
        padding: 10px 20px;
        border: none;
    }
</style>
"""

# 서울시 지도 구 이름 및 버튼 위치
gu_arr = {
    "도봉구": {"id": "dobong", "top": "95px", "right": "376px"},
    "노원구": {"id": "nowon", "top": "150px", "right": "270px"},
    "강북구": {"id": "gangbuk", "top": "180px", "right": "445px"},
    "은평구": {"id": "eunpyeong", "top": "263px", "right": "660px"},
    "성북구": {"id": "seongbuk", "top": "315px", "right": "415px"},
    "중랑구": {"id": "jungnang", "top": "330px", "right": "215px"},
    "종로구": {"id": "jongno", "top": "335px", "right": "540px"},
    "서대문구": {"id": "seodaemun", "top": "400px", "right": "635px"},
    "동대문구": {"id": "dongdaemun", "top": "380px", "right": "325px"},
    "강서구": {"id": "gangseo", "top": "440px", "right": "955px"},
    "마포구": {"id": "mapo", "top": "460px", "right": "690px"},
    "중구": {"id": "jung", "top": "450px", "right": "480px"},
    "성동구": {"id": "seongdong", "top": "478px", "right": "354px"},
    "광진구": {"id": "gwangjin", "top": "495px", "right": "225px"},
    "강동구": {"id": "gangdong", "top": "490px", "right": "70px"},
    "양천구": {"id": "yangcheon", "top": "580px", "right": "855px"},
    "영등포구": {"id": "yeongdeungpo", "top": "600px", "right": "710px"},
    "용산구": {"id": "yongsan", "top": "538px", "right": "510px"},
    "구로구": {"id": "guro", "top": "670px", "right": "850px"},
    "동작구": {"id": "dongjak", "top": "650px", "right": "600px"},
    "서초구": {"id": "seocho", "top": "740px", "right": "420px"},
    "강남구": {"id": "gangnam", "top": "690px", "right": "280px"},
    "송파구": {"id": "songpa", "top": "650px", "right": "150px"},
    "금천구": {"id": "geumcheon", "top": "772px", "right": "740px"},
    "관악구": {"id": "gwanak", "top": "760px", "right": "610px"}
}

# main 타이틀 설명
main_html += f"""   
<div class="main_group">
    <div class="main_group_items">
        <div class="main_title">
            <p>서울특별시</br>
            교통 혼잡도</p>
            <p>구를 클릭해서 교통 혼잡도를 확인해보세요!</p>
            <p>자주묻는 질문을 확인해보세요!</p>
            <div class="faq_btn">
                <a href="/faq" target="_self">
                    <button>FAQ 페이지 열기</button>
                </a> 
            </div>
        </div>
        <div class="main_map">
            <img src="data:image/png;base64,{img_base64}">
        </div>
    </div>

    <div class="main_group_buttons">
"""
# enumerate써서 int와 튜플값 같이
for i, (name, info) in enumerate(gu_arr.items()):
    btn_id = info['id']
    top = info['top']
    right = info['right']
    # 색깔별로 다르게 출력
    if(i%2==0):
        main_html += f"""<button class="blue_btn" onclick="window.location.href='/traffic_graph?gu_id={btn_id}&gu={name}'" style="top:{top}; right:{right};">{name} +</button>"""
    else:
        main_html += f"""<button class="gray_btn" onclick="window.location.href='/traffic_graph?gu_id={btn_id}&gu={name}'" style="top:{top}; right:{right};">{name} +</button>"""
# 3. 하단 HTML (부모 div 닫기)
main_html += '</div>'
main_html += """  
</div>
"""

# html 실행
components.html(
    main_html,
    height = 920,
    scrolling=False
)
