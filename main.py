import streamlit as st
from streamlit_navigation_bar import st_navbar

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Navbar Visibility Test",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# FORCE NAVBAR TEXT VISIBILITY (NO HIDING)
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* Make navbar area visible */
    [data-testid="stNavBar"] {
        background-color: #ffffff !important;
        border-bottom: 1px solid #e5e7eb;
    }

    /* Force text color */
    [data-testid="stNavBar"] span {
        color: #000000 !important;
        font-size: 15px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# NAVIGATION BAR
# --------------------------------------------------
pages = ["Home", "About", "Contact"]
page = st_navbar(pages)

# --------------------------------------------------
# SUCCESS CONFIRMATION
# --------------------------------------------------
st.success(
    "✅ Navigation bar is rendered ABOVE this message. "
    "If you can click tabs and see text, it is working."
)

# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------
st.title(page)

if page == "Home":
    st.write("🏠 You are on the Home page.")
    st.info("Click another tab to confirm navigation works.")

elif page == "About":
    st.write("ℹ️ You are on the About page.")
    st.info("Navbar selection updated correctly.")

elif page == "Contact":
    st.write("📞 You are on the Contact page.")
    st.info("Navigation bar is fully functional.")

# --------------------------------------------------
# SCROLL TEST
# --------------------------------------------------
for i in range(10):
    st.write(f"Scrollable content line {i + 1}")
