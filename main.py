import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="BridgeSign", page_icon="🧏‍♀️", layout="centered")

# ---- CUSTOM CSS to make background white ----
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    .stApp {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Sidebar ----
with st.sidebar:
    st.header("BridgeSign")
    st.markdown("**Empowering Communication**")

# ---- Main Title ----
st.markdown(
    """
    <h1 style='text-align: center; color: #20522e;'>The AI Sign Language Trainer for Healthcare</h1>
    <h4 style='text-align: center; color: #444;'>An interactive platform helping professionals build essential ASL skills through AI-driven practice.</h4>
    """,
    unsafe_allow_html=True
)

# ---- Centered Call to Action: SIGN UP Button ----
st.markdown("<div style='text-align: center; padding: 100;'>", unsafe_allow_html=True)

if st.button("Sign Up", key="signup_button"):
    st.switch_page("pages/sign_up.py")

st.markdown("</div>", unsafe_allow_html=True)

# ---- Trust Section ----
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px; color: #888;'>
        Backed by <img src='https://upload.wikimedia.org/wikipedia/commons/6/69/Y_Combinator_logo.svg' width='90'>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Footer ----
st.markdown("<br><br>", unsafe_allow_html=True)
