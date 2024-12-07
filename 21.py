import streamlit as st
import function

col1,col2= st.columns(2)


vinay=function.clean()
def old():
    todo=st.session_state["hello"]+"\n"
    vinay.append(todo)
    function.bag(vinay)


with col2:
    st.title("ROYAL CHALLENGERS BENGALURU")
    st.subheader("playing 11 squad")
    st.write("players")
    for index,todos in enumerate(vinay):
        checkbox=st.checkbox(todos)
        if checkbox:
            vinay.pop(index)
            function.bag(vinay)

    st.text_input(placeholder="Rasikh Dar Salam",label="Impact player",on_change=old,key="hello")
with col1:
    st.title("ROYAL CHALLENGERS BENGALURU ")
    st.subheader("bench player")
    content="""
    1Devdutt Padikal 
    
    2Jacob Bethell
    
    3 Swapnil Singh
    
    4 Manoj Bhandage
    
    5 Lingi Ngidi
    
    """


    st.write(content)


st.session_state