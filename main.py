import streamlit as st
from streamlit_option_menu import option_menu

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="Streamlit Navigation Test",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# SELECT MENU TYPE
# 1 = Sidebar menu
# 2 = Horizontal menu (header)
# 3 = Horizontal menu with custom style
# --------------------------------------------------
EXAMPLE_NO = 2   # 🔁 change 1 / 2 / 3 to test

# --------------------------------------------------
# NAVIGATION MENU FUNCTION
# --------------------------------------------------
def streamlit_menu(example=1):

    if example == 1:
        # SIDEBAR MENU
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Projects", "Contact"],
                icons=["house", "book", "envelope"],
                menu_icon="cast",
                default_index=0,
            )
        return selected

    elif example == 2:
        # HORIZONTAL MENU (HEADER)
        selected = option_menu(
            menu_title=None,
            options=["Home", "Projects", "Contact"],
            icons=["house", "book", "envelope"],
            default_index=0,
            orientation="horizontal",
        )
        return selected

    elif example == 3:
        # HORIZONTAL MENU WITH CUSTOM STYLE
        selected = option_menu(
            menu_title=None,
            options=["Home", "Projects", "Contact"],
            icons=["house", "book", "envelope"],
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#ffffff",
                    "border-bottom": "1px solid #e5e7eb",
                },
                "icon": {
                    "color": "#2563eb",
                    "font-size": "20px"
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#f3f4f6",
                },
                "nav-link-selected": {
                    "background-color": "#2563eb",
                    "color": "white",
                },
            },
        )
        return selected

# --------------------------------------------------
# RENDER MENU
# --------------------------------------------------
selected = streamlit_menu(EXAMPLE_NO)

# --------------------------------------------------
# SUCCESS CONFIRMATION
# --------------------------------------------------
st.success("✅ Navigation menu is working. Selection detected.")

# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------
st.title(f"You have selected: {selected}")

if selected == "Home":
    st.write("🏠 Welcome to the Home page")

elif selected == "Projects":
    st.write("📁 This is the Projects page")

elif selected == "Contact":
    st.write("📞 This is the Contact page")

# --------------------------------------------------
# SCROLL TEST
# --------------------------------------------------
for i in range(8):
    st.write(f"Scrollable content line {i + 1}")
