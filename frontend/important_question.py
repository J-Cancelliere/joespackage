import streamlit as st
from joespackage.lib import try_me

user_input = st.text_input("What is the answer to life, the universe, and everything?", "")

if user_input == "42":
    st.write("Correct!")
else:
    st.write("Incorrect!")
