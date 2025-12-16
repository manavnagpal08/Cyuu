import streamlit as st

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="LinkedIn Style Header",
    page_icon="💼",
    layout="wide"
)

# --------------------------------------------------
# LINKEDIN STYLE HEADER
# --------------------------------------------------
st.markdown("""
<style>

/* FIX TOP HEADER */
.header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 64px;
    background-color: white;
    border-bottom: 1px solid #e5e7eb;
    display: flex;
    align-items: center;
    padding: 0 40px;
    z-index: 9999;
}

/* LOGO */
.logo {
    font-size: 26px;
    font-weight: 800;
    color: #0a66c2;
    margin-right: 20px;
}

/* SEARCH BAR */
.search-box input {
    width: 280px;
    padding: 8px 12px;
    border-radius: 6px;
    border: 1px solid #d1d5db;
    background-color: #eef3f8;
    outline: none;
}

/* NAV ITEMS */
.nav {
    display: flex;
    gap: 28px;
    margin-left: auto;
    align-items: center;
}

.nav-item {
    text-align: center;
    font-size: 12px;
    color: #374151;
    cursor: pointer;
}

.nav-item i {
    font-size: 18px;
    display: block;
}

/* PROFILE */
.profile img {
    width: 32px;
    height: 32px;
    border-radius: 50%;
}

/* PAGE OFFSET */
.page-content {
    margin-top: 90px;
}

</style>

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<div class="header">
    <div class="logo">in</div>

    <div class="search-box">
        <input type="text" placeholder="Search">
    </div>

    <div class="nav">
        <div class="nav-item">
            <i class="fa-solid fa-house"></i>
            Home
        </div>
        <div class="nav-item">
            <i class="fa-solid fa-user-group"></i>
            My Network
        </div>
        <div class="nav-item">
            <i class="fa-solid fa-briefcase"></i>
            Jobs
        </div>
        <div class="nav-item">
            <i class="fa-solid fa-comment-dots"></i>
            Messaging
        </div>
        <div class="nav-item">
            <i class="fa-solid fa-bell"></i>
            Notifications
        </div>
        <div class="profile">
            <img src="https://i.pravatar.cc/150?img=3">
        </div>
    </div>
</div>

<div class="page-content"></div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN PAGE CONTENT
# --------------------------------------------------
st.header("Dashboard Content")
st.write("This content appears **below** the LinkedIn-style header.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Profile Views", 124)

with col2:
    st.metric("Connections", 512)

with col3:
    st.metric("Job Alerts", 7)

st.write("Scroll down to see header stay fixed 👆")

for i in range(20):
    st.write(f"Sample content row {i+1}")
