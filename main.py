import streamlit as st
# Make sure to install this library: pip install streamlit-option-menu
from streamlit_option_menu import option_menu

# Configuration: Select which menu example to run
# 1: Sidebar Menu (Default)
# 2: Horizontal Menu (Simple)
# 3: Horizontal Menu (Custom Styles)
EXAMPLE_NO = 1


def streamlit_menu(example: int):
    """
    Renders the Streamlit menu based on the example number provided.
    
    :param example: The example number (1, 2, or 3) to render.
    :return: The selected option string.
    """
    options = ["Home", "Projects", "Contact"]
    icons = ["house", "book", "envelope"]

    if example == 1:
        # 1. As a sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # Required
                options=options,  # Required
                icons=icons,  # Optional
                menu_icon="cast",  # Optional
                default_index=0,  # Optional
            )
        return selected

    elif example == 2:
        # 2. Horizontal menu without custom style
        selected = option_menu(
            menu_title=None,  # Not required for horizontal menu
            options=options,  # Required
            icons=icons,  # Optional
            menu_icon="cast",  # Optional
            default_index=0,  # Optional
            orientation="horizontal",
        )
        return selected

    elif example == 3:
        # 3. Horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # Not required for horizontal menu
            options=options,  # Required
            icons=icons,  # Optional
            menu_icon="cast",  # Optional
            default_index=0,  # Optional
            orientation="horizontal",
            styles={
                # Container style: sets background and removes padding
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                # Icon style: sets color and size
                "icon": {"color": "orange", "font-size": "25px"},
                # Link style: sets font size, alignment, margin, and hover color
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                # Selected link style: sets the background color for the active tab
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected
        
    else:
        st.error(f"Invalid example number: {example}. Please use 1, 2, or 3.")
        return options[0] # Return default option in case of error


# --- Main Application Logic ---
# Get the selected page from the menu function
selected = streamlit_menu(example=EXAMPLE_NO)

# Display content based on the selection
st.header(f"Page Selected: {selected}")
st.write("---")

if selected == "Home":
    st.success("Welcome to the Home page!")
    st.write("This is the default content for the 'Home' selection.")
    
elif selected == "Projects":
    st.info("Here are your exciting Projects!")
    st.write("This is the default content for the 'Projects' selection.")

elif selected == "Contact":
    st.warning("Get in touch with us!")
    st.write("This is the default content for the 'Contact' selection.")

# Add a note about the current example
st.caption(f"Currently running Menu Example No: **{EXAMPLE_NO}**")
