import streamlit as st
st.title("Simple addition calculator")
def addition(a,b):
  return a+b
a = st.number_input("first")
b = st.number_input("second")

st.write('this is a : ',a)
