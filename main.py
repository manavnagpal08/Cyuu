import streamlit as st
from streamlit_navigation_bar import st_navbar

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Navbar Test",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# NAVIGATION BAR (MINIMAL)
# --------------------------------------------------
pages = ["Home", "About", "Contact"]

page = st_navbar(pages)

# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------
st.title(page)

if page == "Home":
    st.write("🏠 This is the Home page")
    st.write("Navbar is working if you can switch pages.")

elif page == "About":
    st.write("ℹ️ This is the About page")
    st.write("No external files, no styles.")

elif page == "Contact":
    st.write("📞 This is the Contact page")
    st.write("Pure single-file test.")

# Scroll content to test layout
for i in range(10):
    st.write(f"Scrollable content {i + 1}")
