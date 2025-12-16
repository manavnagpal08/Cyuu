import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
/* Remove default padding */
.block-container {
    padding-top: 0rem;
}

/* HEADER NAVBAR */
.header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 64px;
    background: linear-gradient(90deg, #1e3a8a, #2563eb);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 32px;
    z-index: 1000;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* LOGO */
.header-logo {
    font-size: 20px;
    font-weight: 700;
    color: white;
}

/* NAV LINKS */
.header-nav a {
    color: white;
    text-decoration: none;
    margin-left: 24px;
    font-weight: 500;
    transition: opacity 0.2s ease;
}

.header-nav a:hover {
    opacity: 0.8;
}

/* PUSH CONTENT BELOW HEADER */
.spacer {
    height: 80px;
}
</style>

<div class="header">
    <div class="header-logo">ScreenerPro</div>
    <div class="header-nav">
        <a href="?page=dashboard">Dashboard</a>
        <a href="?page=jobs">Jobs</a>
        <a href="?page=analytics">Analytics</a>
        <a href="?page=account">Account</a>
    </div>
</div>

<div class="spacer"></div>
""", unsafe_allow_html=True)
query_params = st.query_params
page = query_params.get("page", ["dashboard"])[0]

if page == "dashboard":
    st.header("📊 Dashboard")
    st.write("Dashboard content here")

elif page == "jobs":
    st.header("💼 Job Board")
    st.write("Jobs content here")

elif page == "analytics":
    st.header("📈 Analytics")
    st.write("Analytics content here")

elif page == "account":
    st.header("👤 Account")
    st.write("Account settings here")
