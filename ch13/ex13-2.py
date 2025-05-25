import streamlit as st

st.title('Hello, Streamlit')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a simple text')
st.write('This is your first Streamlit app.')

# 超連結
st.markdown("[Streamlit](https://www.streamlit.io)")

# HTML
html_page="""
<div style="background-color:blue;padding:20px; color:white; font-size: 20px">
Hello Streamlit!
</div>
<p></p>
"""
st.markdown(html_page, unsafe_allow_html=True)

# 彩色文字
st.success("Success!")
st.info("Information.")
st.warning("This is a warning!")
st.error("This is an error!")
