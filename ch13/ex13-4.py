import streamlit as st
import datetime
from time import sleep

st.title("互動元件")

# 加入單行文字輸入框
st.subheader("text input")
name=st.text_input("Enter you name:")
st.write(f"Hello, {name}")

# 加入多行文字輸入框
message=st.text_area("Enter your message:")
st.write("Your message:")
st.write(message)

# 加入數值輸入框
st.subheader("number input")
age=st.number_input("Enter your age:", min_value=0, max_value=120)
st.write(f"Your age is {age}")

# 加入按鈕
st.subheader("Button")
if st.button('Click Me'):
    st.write("Button clicked!")

# 加入單選鈕
st.subheader("Radio and checkbox")
gender = st.radio("Select your gender:", ["Male", "Female", "Other"], 
	horizontal=True)
st.write(f"You selected {gender}")

# 加入複選框
agree= st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")

# 加入下拉式選單
st.subheader("select box")
fruit = st.selectbox("Your favorite fruit:", ["Apple", "Banana", "Cherry"])
st.write(f"You selected {fruit}")

# 加入可複選的下拉式選單
options = st.multiselect("Your favorite colors:", ["Red", "Green", "Blue"])
st.write(f"You selected {options}")

# 加入滑桿
st.subheader("slider")
value = st.slider("Select a value:", 0, 100, 50)
st.write(f"Selected value: {value}")

# 加入值範圍滑桿
range_value = st.slider("Select a range of value:", 0, 100, (20, 80))
st.write(f"Selected range: {range_value}")

# 加入日期選擇器
st.subheader("date and time")
date = st.date_input("Select a date:", datetime.datetime.now())
st.write(f"Selected data: {date}")

# 加入時間選擇器
time = st.time_input("Select a time:", datetime.time(12,30))
st.write(f"Selected time: {time}")

# 加入進度條
st.subheader("progress and spinner")
progress_bar=st.progress(0)
for value in range(101):
    progress_bar.progress(value)
    sleep(0.1)
st.write("Done")

# 加入旋轉指示器
with st.spinner("等待中..."):
    sleep(10)
st.success('Done')
