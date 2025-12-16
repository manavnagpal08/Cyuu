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
# DEBUGGING SIDEBAR
# --------------------------------------------------
st.sidebar.markdown("### 🛠️ Debugging Info")
st.sidebar.write("App execution started.")

# --------------------------------------------------
# NAVIGATION BAR (WITH EXPLICIT STYLING FOR VISIBILITY)
# --------------------------------------------------

pages = ["Home", "About", "Contact"]
st.sidebar.write(f"Pages list for navbar: {pages}")

# Explicitly define styles to ensure text and buttons are clearly visible
styles = {
    "nav": {
        "background-color": "#e0e0e0",  # Light grey background for the entire bar
    },
    "span": {
        "color": "black",  # IMPORTANT: Ensures text is black and not invisible
        "margin": "0 10px", # Add a little horizontal spacing between links
        "font-weight": "500",
    },
    "active": {
        "background-color": "#ffffff",  # White background for the active button
        "color": "darkred",  # Highlight active text with dark red
        "font-weight": "bold", # Make the active text bold
        "border-radius": "10px",
    },
    # You can also style the button when it's hovered over
    "hover": {
        "background-color": "#cccccc", # Slightly darker grey on hover
    }
}

try:
    # Attempt to render the navigation bar with explicit styles
    page = st_navbar(
        pages,
        styles=styles,
        key="custom_navbar_with_style" # Use a key to prevent re-rendering issues
    )

    # Debug check
    st.sidebar.write(f"st_navbar returned page: **{page}**")
    
except Exception as e:
    # Fallback if the component fails (e.g., if the library is missing)
    st.sidebar.error("Error during st_navbar call!")
    st.sidebar.exception(e)
    page = "Error"


# --------------------------------------------------
# PAGE CONTENT (BASED ON NAVBAR SELECTION)
# --------------------------------------------------
st.header(f"Page: {page}")
st.markdown("---")


if page == "Home":
    st.markdown("## 🏠 Welcome Home")
    st.write("**Confirmation:** The navigation bar is working if you can switch between the 'Home', 'About', and 'Contact' sections above.")
    st.write("This application uses the `streamlit-navigation-bar` component to create a multi-page interface within a single file.")

elif page == "About":
    st.markdown("## ℹ️ About This App")
    st.write("This minimal test confirms the functionality of the custom navigation bar component.")
    st.write("We used explicit styling in the code to ensure the link text is visible (black on a light grey bar).")

elif page == "Contact":
    st.markdown("## 📞 Get in Touch")
    st.write("Feel free to reach out for more Streamlit tips!")
    st.code("email = 'test@example.com'", language="python")

elif page == "Error":
    st.error("The navigation bar failed to load. Please check the **Debugging Info** in the sidebar for details on the error.")
    st.warning("If an error occurred, you likely need to install the library: `pip install streamlit-navigation-bar`")

# --------------------------------------------------
# SCROLLABLE CONTENT
# --------------------------------------------------
st.markdown("---")
st.subheader("Scrollable Content Test")
for i in range(1, 11):
    st.write(f"Scrollable content line {i} to test the 'wide' layout and scrolling.")
