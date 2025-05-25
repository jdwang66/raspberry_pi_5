import streamlit as st

# 側邊欄加入抬頭及下拉式選單
st.sidebar.title("Layout Demo")
page = st.sidebar.selectbox("Select an item", ["Home", "OpenCV", "MediaPipe"])

def home():
	# 加入2個column
	st.subheader("Columns")
	col1, col2 = st.columns(2)
	with col1:
		st.write("Colum 1 here")    
	with col2:
		st.write("Column2 here")

	# 加入可擴展元件
	st.subheader("Expander")
	with st.expander("Expand for more details"):
		st.write("Here are additional details")

	# 加入2個選項卡
	st.subheader("Tabs")
	tab1, tab2 = st.tabs(["Tab1", "Tab 2"])
	with tab1:
		st.write("Content for Tab1")
	with tab2:
		st.write("Conent for Tab2")

if page=="Home":
	st.header("Home")
	home()
