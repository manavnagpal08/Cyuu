import streamlit as st

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="Streamlit Header Demo",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM HEADER (TOP BAR)
# --------------------------------------------------
st.markdown(
    """
    <style>
    .app-header {
        background: linear-gradient(90deg, #1e3a8a, #0ea5e9);
        padding: 20px 30px;
        border-radius: 12px;
        margin-bottom: 25px;
    }
    .app-header h1 {
        color: white;
        margin: 0;
        font-size: 32px;
    }
    .app-header p {
        color: #e0f2fe;
        margin: 5px 0 0;
        font-size: 16px;
    }
    </style>

    <div class="app-header">
        <h1>🚀 Streamlit Header Supported</h1>
        <p>Modern header bar using Streamlit + HTML/CSS</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# STANDARD STREAMLIT HEADERS
# --------------------------------------------------
st.title("Main Title (st.title)")
st.header("Section Header (st.header)")
st.subheader("Sub Section (st.subheader)")

st.write(
    """
    Streamlit **fully supports headers** using built-in functions  
    and also allows **custom headers** using HTML/CSS.
    """
)

# --------------------------------------------------
# LAYOUT EXAMPLE
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.header("📊 Analytics")
    st.write("Visual insights and metrics")

with col2:
    st.header("🤖 AI Engine")
    st.write("Smart resume & data processing")

with col3:
    st.header("🔒 Security")
    st.write("Secure authentication & access")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("© 2025 | Built with Streamlit")
