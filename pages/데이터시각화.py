import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

# 폰트 설정
font_path = 'fonts/NotoSansKR-Bold.ttf'
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'Noto Sans KR'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

st.title("데이터 시각화")

st.header("그래프 섹션")
st.write("여기에 그래프를 표시합니다. 데이터를 넣어주세요.")

# 예시 그래프 (사용자가 데이터를 넣을 자리)
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 15, 25])
ax.set_title("예시 그래프")
ax.set_xlabel("X축")
ax.set_ylabel("Y축")
st.pyplot(fig)

st.header("표 섹션")
st.write("여기에 표를 표시합니다. 데이터를 넣어주세요.")

# 예시 표 (사용자가 데이터를 넣을 자리)
data = {
    '항목': ['A', 'B', 'C'],
    '값': [100, 200, 150]
}
df = pd.DataFrame(data)
st.dataframe(df)

st.write("추가 그래프나 표를 원하시면 이 형식을 확장하세요.")