import streamlit as st

st.title('To-Do List')

# 初始化todo_list
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

# 輸入待辦事項，加入todo_list中
new_todo = st.text_input("What do you need to do?")
if st.button('Add new To-Do item'):    
    st.session_state.todo_list.append(new_todo)

# 顯示todo_list串列
st.subheader('To Do List:')
for item in st.session_state.todo_list:
    st.write(item)
