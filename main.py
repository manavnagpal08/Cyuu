import streamlit as st
from streamlit_navigation_bar import st_navbar

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Navbar Working Test",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# NAVIGATION BAR
# --------------------------------------------------
pages = ["Home", "About", "Contact"]
page = st_navbar(pages)

# --------------------------------------------------
# SUCCESS / WORKING INDICATOR
# --------------------------------------------------
st.success("✅ Navigation bar is WORKING. Page switching is active.")

# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------
st.title(page)

if page == "Home":
    st.write("🏠 You are on the **Home** page.")
    st.info("If clicking tabs changes this title, navbar is working.")

elif page == "About":
    st.write("ℹ️ You are on the **About** page.")
    st.info("Navigation state updated successfully.")

elif page == "Contact":
    st.write("📞 You are on the **Contact** page.")
    st.info("Navigation bar selection detected.")

# --------------------------------------------------
# EXTRA CONTENT (SCROLL TEST)
# --------------------------------------------------
for i in range(8):
    st.write(f"Scrollable content {i + 1}")
