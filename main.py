import streamlit as st
from streamlit_navigation_bar import st_navbar

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="Navbar Example",
    page_icon="💼",
    layout="wide"
)

# --------------------------------------------------
# NAVIGATION BAR
# --------------------------------------------------
page = st_navbar(
    ["Home", "My Network", "Jobs", "Messages", "Notifications", "Profile"],
    logo_path=None,
    hide_streamlit_markers=True
)

# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------
st.header(page)

if page == "Home":
    st.write("🏠 Welcome to Home")

elif page == "My Network":
    st.write("👥 Your professional network")

elif page == "Jobs":
    st.write("💼 Job listings")

elif page == "Messages":
    st.write("💬 Messages")

elif page == "Notifications":
    st.write("🔔 Notifications")

elif page == "Profile":
    st.write("👤 Profile page")

# Demo scrolling
for i in range(25):
    st.write(f"Content line {i+1}")
