import streamlit as st

# 페이지들은 로드하는 메인 .py
st.set_page_config(layout="wide")

st.markdown("""
<style>
@font-face {
    font-family: 'ChangwonDangamRounded';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2511-1@1.0/ChangwonDangamRound-Regular.woff2') format('woff2');
    font-weight: normal;
}
            
header[data-testid="stHeader"] {
    display: none;
}
            
.stApp {
    background-color: #ffffff;
    height: 100vh;
    margin: 0px;
    overflow: hidden;
}
            
.stMainBlockContainer {
    padding: 0 0 0 0;
    width: 100%;
    height: auto;
}
</style>
""", unsafe_allow_html=True)

# 화면을 넓게(wide) 설정으로 헤더 삭제
st.set_page_config(layout="wide")

# 페이지 경로 등록
main = st.Page("main.py", default=True)
faq = st.Page("faq.py")
graph = st.Page("traffic_graph.py")

# 네비게이션 메뉴는 숨김 처리
pg = st.navigation([main, faq, graph], position="hidden")
pg.run()