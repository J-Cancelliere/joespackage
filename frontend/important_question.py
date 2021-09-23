import streamlit as st
from joespackage.lib import try_me
from PIL import Image

#Display image of Deepthought
image = Image.open("deep_thought.jpg")
st.image(image,)

# Ask the user the question
st.markdown("""
    <h1 style='text-align: center;'>What is the answer to life, the universe, and everything?</h1>
    """, unsafe_allow_html = True)

# Get the user's answer
buff, col, buff2 = st.columns([1,1,1])
user_input = col.text_input("","")

# Show whether the answer is correct or incorrect
correct_answers = ["42","forty two","forty-two"] 
if user_input.lower().strip() in correct_answers:
    st.markdown("""
    <h1 style='text-align: center; color: green;'>Correct!</h1>
    """, unsafe_allow_html = True)
else:
    st.markdown("""
    <h1 style='text-align: center; color: red;'>Incorrect!</h1>
    """, unsafe_allow_html = True)
