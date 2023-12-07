import streamlit as st
st.title("Simple addition calculator Amruta")

a = st.number_input("first")
b = st.number_input("second")
def addition(a,b):
  return a+b
st.write("this is my a : ", a)
st.write("this is my b : ", b)
st.write("this is my sum : ", addition(a,b))
