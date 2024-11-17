import streamlit as st

st.title("session state")

st.write(st.session_state)

ss = st.session_state

if 'bujon' not in st.session_state:
    st.session_state.bujon = 0


st.write("session state is ", ss.bujon)

button = st.button("bujon")
if button:
    ss.bujon += 1
    ss['bujon'] +=3