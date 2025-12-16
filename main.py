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
# 🛑 CRITICAL STEP: INJECT CUSTOM CSS FOR HEIGHT FIX 🛑
# We are specifically targeting the iframe and inner div to control height.
st.markdown("""
<style>
/* 1. Target the iframe container that holds the component */
iframe[title="streamlit_navigation_bar.streamlit_navigation_bar"] {
    height: 60px !important; /* Set a specific, generous height (e.g., 60px) */
    min-height: 60px !important; 
    margin-top: -10px; /* Optional: Adjust negative margin if it sits too low */
}

/* 2. Target the main Streamlit container for the entire app body */
.stApp {
    color: black; 
}

/* 3. Target the main content area padding to ensure the navbar sits flush */
div[data-testid="stVerticalBlock"] {
    padding-top: 0 !important;
}

</style>
""", unsafe_allow_html=True)
# --------------------------------------------------


# --------------------------------------------------
# DEBUGGING SIDEBAR
# --------------------------------------------------
st.sidebar.markdown("### 🛠️ Debugging Info")
st.sidebar.write("App execution started.")

# --------------------------------------------------
# NAVIGATION BAR (HIGH-CONTRAST STYLING RETAINED)
# --------------------------------------------------

pages = ["Home", "About", "Contact"]
st.sidebar.write(f"Pages list for navbar: {pages}")

# Use high-contrast styling again for guaranteed text visibility
styles = {
    "nav": {
        "background-color": "#000000",  # BLACK background
        "height": "60px",               # Set inner element height
        "line-height": "60px",          # Center text vertically
    },
    "span": {
        "color": "#ffcccc",  # PINK text 
        "font-weight": "800",
        "font-size": "18px",
        "padding": "0 15px", # Add padding inside the text link
    },
    "active": {
        "background-color": "#ffffff",  # White background for active
        "color": "black",  # BLACK text on white background for active
        "font-weight": "bold", 
        "border-radius": "5px",
        "padding": "5px 10px",
    },
}

try:
    # Render the navigation bar with style adjustments
    page = st_navbar(
        pages,
        styles=styles,
        key="height_fixed_navbar" 
    )

    st.sidebar.write(f"st_navbar returned page: **{page}**")
    
except Exception as e:
    st.sidebar.error("Error during st_navbar call!")
    st.sidebar.exception(e)
    page = "Error"


# --------------------------------------------------
# PAGE CONTENT (Unchanged)
# --------------------------------------------------
st.header(f"Page: {page}")
st.markdown("---")

if page == "Home":
    st.markdown("## 🏠 Home Page")
    st.info("The height of the navigation bar should now be correct! We used CSS to force the `iframe` height.")

elif page == "About":
    st.markdown("## ℹ️ About This App")
    st.write("This app demonstrates debugging of component visibility and height using Streamlit's `st.markdown(..., unsafe_allow_html=True)` to inject critical CSS.")

elif page == "Contact":
    st.markdown("## 📞 Get in Touch")
    st.write("Pure single-file test.")

elif page == "Error":
    st.error("The navigation bar failed to load.")


# SCROLLABLE CONTENT
st.markdown("---")
st.subheader("Scrollable Content Test")
for i in range(1, 11):
    st.write(f"Scrollable content line {i}")
