import streamlit as st
st.title("Simple addition calculator")

a = st.number_input("first")
b = st.number_input("second")
def addition(a,b):
  return a+b

