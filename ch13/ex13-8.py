import streamlit as st

# 建立導航頁面
pages = {
    "Streamlit 文字及多媒體元素" : [
        st.Page("ex13-2.py", title="文字元素", default=True),
        st.Page("ex13-3.py", title="多媒體元素", icon=":material/play_circle:")
    ],    
    "Streamlit 互動與佈局元素": [
        st.Page("ex13-4.py", title="互動元素", icon=":material/thumb_up:"),
        st.Page("ex13-5.py", title="佈局元素", icon=":material/grid_view:")
    ],
    "Streamlit Session State": [
        st.Page("ex13-6.py", title="counter 變數", icon=":material/counter_1:"),
        st.Page("ex13-7.py", title="todo_list 變數", icon=":material/list_alt:")
    ]
}

# 加入導航頁面
pg=st.navigation(pages)

# 執行選擇的頁面
pg.run()
