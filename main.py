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
# 🛑 CRITICAL STEP: INJECT CUSTOM CSS FOR MAX VISIBILITY 🛑
# This uses st.markdown to inject CSS that sets the global text color to black
st.markdown("""
<style>
/* This targets all main text elements globally */
.stApp {
    color: black; 
}
/* This targets the navigation bar component itself */
iframe[title="streamlit_navigation_bar.streamlit_navigation_bar"] {
    background-color: #f0f8ff !important; /* Extremely light blue background for the bar */
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
# NAVIGATION BAR (HIGH-CONTRAST STYLING)
# --------------------------------------------------

pages = ["Home", "About", "Contact"]
st.sidebar.write(f"Pages list for navbar: {pages}")

# Use ultra-high contrast styling to guarantee visibility
styles = {
    "nav": {
        "background-color": "#000000",  # BLACK background for the entire bar
    },
    "span": {
        "color": "#ffcccc",  # PINK text (very visible on black)
        "margin": "0 10px", 
        "font-weight": "800", # Extra bold
        "font-size": "18px", # Larger size
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
    # Attempt to render the navigation bar with high-contrast styles
    page = st_navbar(
        pages,
        styles=styles,
        key="ultra_contrast_navbar" 
    )

    # Debug check
    st.sidebar.write(f"st_navbar returned page: **{page}**")
    
except Exception as e:
    st.sidebar.error("Error during st_navbar call!")
    st.sidebar.exception(e)
    page = "Error"


# --------------------------------------------------
# PAGE CONTENT (BASED ON NAVBAR SELECTION)
# --------------------------------------------------
st.header(f"Page: {page}")
st.markdown("---")


if page == "Home":
    st.markdown("## 🏠 Welcome Home (Text Should Be Visible!)")
    st.write("If you see **PINK** text on a **BLACK** bar, the fix worked.")
    
# ... (The rest of your page content remains the same)
elif page == "About":
    st.markdown("## ℹ️ About This App")
    st.write("This test now uses custom CSS and ultra-high-contrast colors to ensure the navigation bar text is not hidden by theme settings.")

elif page == "Contact":
    st.markdown("## 📞 Get in Touch")
    st.write("Pure single-file test.")

elif page == "Error":
    st.error("The navigation bar failed to load. Please check the **Debugging Info** in the sidebar.")


# SCROLLABLE CONTENT
st.markdown("---")
st.subheader("Scrollable Content Test")
for i in range(1, 11):
    st.write(f"Scrollable content line {i} to test the 'wide' layout and scrolling.")
