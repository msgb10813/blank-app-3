import streamlit as st

# 앱 제목 설정
st.title("🍿 영화관 세트 메뉴 고르기")
st.markdown("파이썬의 반복문 로직을 활용한 메뉴 판별기입니다.")

# 기존 데이터 구조 유지
popcorn_options = ['기본', '카라멜', '어니언']
drink_options = ['생수', '탄산음료']

st.header("1. 전체 세트 메뉴 라인업")
st.caption("기존 print() 문 로직을 그대로 활용해 전체 조합을 출력합니다.")

# 💡 기존의 nested for loop 로직을 그대로 유지한 채, st.write()로 화면에 출력
for popcorn in popcorn_options:
    for drink in drink_options:
        st.write(f"🎬 **세트메뉴:** {popcorn} 팝콘 + {drink}")

st.markdown("---")

st.header("2. 내 맘대로 주문하기")
st.caption("위 옵션을 활용해 사용자가 직접 메뉴를 선택할 수 있는 인터페이스입니다.")

# 스트림릿의 셀렉트박스 위젯에 기존 옵션 리스트 적용
selected_popcorn = st.selectbox("팝콘을 선택하세요:", popcorn_options)
selected_drink = st.selectbox("음료를 선택하세요:", drink_options)

# 사용자가 고른 조합 출력
st.success(f" 주문하신 메뉴: **{selected_popcorn} 팝콘**과 **{selected_drink}** 조합이 완료되었습니다!")