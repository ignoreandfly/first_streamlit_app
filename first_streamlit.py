import streamlit as st

st.header('st.button')

if print(st.button('Say hello')):
     st.write('Why hello there')

else:
     st.write('Goodbye')