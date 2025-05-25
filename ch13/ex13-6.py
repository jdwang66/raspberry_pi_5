import streamlit as st

st.title("Session State Demo")

# 初始化counter
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# 加入Add按鈕，增加 counter值
if st.button('Add'):
    st.session_state.counter += 1

# 加入Dec按鈕，減少 counter值
if st.button('Dec'):
    st.session_state.counter -= 1

# 顯示 counter 值
st.write(f"Counter: {st.session_state.counter}")
