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
# NAVIGATION BAR (HEADER)
# --------------------------------------------------
page = st_navbar(
    ["Home", "My Network", "Jobs", "Messages", "Notifications", "Profile"],
    logo_path=None,          # No image/logo
    sticky_nav=True,         # Stays at top
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
    st.write("💼 Job listings and opportunities")

elif page == "Messages":
    st.write("💬 Your messages")

elif page == "Notifications":
    st.write("🔔 Notifications")

elif page == "Profile":
    st.write("👤 Your profile")

# Dummy content to show sticky behavior
for i in range(30):
    st.write(f"Scrollable content {i+1}")
