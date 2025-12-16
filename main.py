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
# NAVIGATION BAR (BASIC API)
# --------------------------------------------------
page = st_navbar([
    "Home",
    "My Network",
    "Jobs",
    "Messages",
    "Notifications",
    "Profile"
])

# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------
st.header(page)

if page == "Home":
    st.write("🏠 Welcome to Home")

elif page == "My Network":
    st.write("👥 Network page")

elif page == "Jobs":
    st.write("💼 Jobs page")

elif page == "Messages":
    st.write("💬 Messages page")

elif page == "Notifications":
    st.write("🔔 Notifications")

elif page == "Profile":
    st.write("👤 Profile page")

for i in range(20):
    st.write(f"Scrollable content {i+1}")
