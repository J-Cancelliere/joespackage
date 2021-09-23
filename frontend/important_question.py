import streamlit as st
from joespackage.lib import try_me
from PIL import Image

image = Image.open("deep_thought.jpg")

st.image(image,"What is the answer to life, the universe, and everything?")

buff, user_input, buff2 = st.columns([1,3,1])

user_input = user_input.text_input("","")

if user_input == "42":
    st.markdown("""
    <h1 style='text-align: center; color: green;'>Correct!</h1>
    """, unsafe_allow_html = True)
else:
    st.markdown("""
    <h1 style='text-align: center; color: red;'>Incorrect!</h1>
    """, unsafe_allow_html = True)
