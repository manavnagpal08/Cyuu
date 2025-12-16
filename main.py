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

# --- DEBUG 1: Displaying a simple message to confirm the file is running ---
st.sidebar.markdown("### 🛠️ Debugging Info")
st.sidebar.write("App execution started.")

# --------------------------------------------------
# NAVIGATION BAR (MINIMAL)
# --------------------------------------------------
pages = ["Home", "About", "Contact"]

st.sidebar.write(f"Pages list for navbar: {pages}")

try:
    # Attempt to render the navigation bar
    page = st_navbar(pages)

    # --- DEBUG 2: Check if st_navbar was called and returned a value ---
    st.sidebar.write(f"st_navbar returned page: **{page}**")
    
    if page not in pages:
        st.sidebar.warning("Warning: Returned page not in the list of defined pages.")

except Exception as e:
    # --- DEBUG 3: Catch an exception if the function call fails (e.g., if the library wasn't imported correctly) ---
    st.sidebar.error("Error during st_navbar call!")
    st.sidebar.exception(e)
    # Set a default page if there was an error
    page = "Error"


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

elif page == "Error":
    st.error("The navigation bar failed to load. Please check the **Debugging Info** in the sidebar for details on the error.")

# Scroll content to test layout
for i in range(10):
    st.write(f"Scrollable content {i + 1}")
