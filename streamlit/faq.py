import streamlit as st
import streamlit.components.v1 as components
from data import faq_data

# 자주묻는질문 py

# faq select함수 가져오기
# 커스텀을 위해 html/css로 구현
faq = faq_data()

# 헤더
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
</style>
<a href="http://localhost:8501" style="text-decoration:none; display:block;"
   onclick="window.location.href=this.href; return false;">
    <header>
        <p>서울특별시&nbsp;<span style="color: #FF7F00">교통&nbsp;</span>혼잡도<p>
    </header>
</a>
""",unsafe_allow_html=True)

# 질문 출력 카테고리별로 탭을 분류함
faq_html = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
<style>
    @font-face {
        font-family: 'ChangwonDangamRounded';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2511-1@1.0/ChangwonDangamRound-Regular.woff2') format('woff2');
        font-weight: normal;
    }
    .faq_title{
        color: #0054A2;
        font-family: "Roboto", sans-serif;
        font-size: 70px;
        width: 100%;
        text-align: center;
    }

    .faq_group {
        display: flex;
        flex-direction: column;
        color: black;
        width: 830px;
        margin: auto auto;
        align-items: center;
    }

    .faq_items input {
        display: none;
    }

    .faq_question_text{
        font-size: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 60px;
        display: flex;
        width: 830px;
        border-bottom: 1px solid #D3D0D0;
    }

    .q, .q_text{
        height: 70px;
        display: inline-flex;
        align-items: center;
        font-family: 'ChangwonDangamRounded';
    }

    .q{
        font-family: "Roboto", sans-serif;
        color: #0054A2; 
    }

    /*질문 css*/    
    .faq_answer {
        font-size: 18px;
        max-height: 0;
        overflow: hidden;
    }

    /*만약 label의 for값과 input의 id값이 같을 경우 답변이 보이게*/ 
    .faq_items input:checked + .faq_question_text +.faq_answer {
        max-height: 500px;
        margin-top: 20px;
        padding-bottom: 20px;
    }

    .faq_items .arrow {
        transition: transform 0.3s ease;
        color: #0054A2;
    }

    /* 각 FAQ 체크 시, 해당 label 안 .arrow만 회전 */
    .faq_items input[type="checkbox"]:checked + label .arrow {
        transform: rotate(180deg);
    }

    .tab{
        font-family: 'ChangwonDangamRounded';
        cursor: pointer;
        padding: 10px 20px;
        margin: 0px 2px;
        display: inline-block;
        border-radius: 5px 5px 0px 0px;
        background-color: #D3D0D0;
        color: #0054A2;
        width: 368px;
        font-size: 18px;
        text-align: center;
    }

    .panels{
        background-color: white;
        min-height: 200px;
        width: 830px;
        border-radius: 3px;
        overflow: hidden;
    }

    .faq_items{
        display: none;
    }

    .panel-title{
        font-size: 1.5em;
        font-weight: bold;
    }

    .radio{
        display: none;  /*체크박스 숨기기 */
    }

    /* display: none인 설명창을 각 조건에 따라 block해주기 */
    #one:checked ~ .panels #one-panel,
    #two:checked ~ .panels #two-panel
    {
        display: block;
    }

    /* 탭 선택되었을 때 */
    #one:checked ~ .tabs #one-tab,
    #two:checked ~ .tabs #two-tab{
        background-color: #0054A2;
        color: #ffffff;
    </style>
"""

faq_html += """
<div class="faq_title">
    <p>FAQ<p>
</div>
<div class="faq_tap_group">
<div class="faq_group"> 
        <input class ="radio" type="radio" name="group" id="one" checked>
        <input class ="radio" type="radio" name="group" id="two">      
        <div class="tabs">
            <label class = "tab" id= "one-tab" for="one">교통정보</label>
            <label class = "tab" id= "two-tab" for="two">혼잡통행료</label>
        </div>
        <div class="panels">
"""

# enumerate 써서 숫자 튜플 둘다 사용할 수 있게
for i, row in enumerate(faq.itertuples()):
    content = str(row.faq_contents).replace('\\n', '<br>').replace('\n', '<br>')
    if (row.faq_section == "교통정보"):
        faq_html += f"""
        <div class="faq_items" id = "one-panel">
            <input type = "checkbox" id="faq{i}" >
            <label for="faq{i}" class="faq_question_text"><div><span class="q">Q.&nbsp; &nbsp;</span><span class="q_text">{row.faq_title}</span></div>
                <span class="arrow">⌵</span>
            </label>
            <div class = "faq_answer">
                {content}
            </div>
        </div>
        """
    elif (row.faq_section == "혼잡통행료"):
        faq_html += f"""
        <div class="faq_items" id = "two-panel">
            <input type = "checkbox" id="faq{i}" >
            <label for="faq{i}" class="faq_question_text"><div><span class="q">Q.&nbsp; &nbsp;</span><span class="q_text">{row.faq_title}</span></div>
                <span class="arrow">⌵</span>
            </label>
            <div class = "faq_answer">
                {content}
            </div>
        </div>
    """
faq_html+="""</div>"""

# 만든 html 쓰게
components.html(
    faq_html,
    height = 7000,
    scrolling=False
)
