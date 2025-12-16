import streamlit as st

# -------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# -------------------------------------------------
st.set_page_config(
    page_title="ScreenerPro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# HEADER NAVBAR (HTML + CSS)
# -------------------------------------------------
st.markdown("""
<style>
/* Remove default top padding */
.block-container {
    padding-top: 0rem;
}

/* Hide Streamlit menu & footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* HEADER BAR */
.sp-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 68px;
    background: linear-gradient(90deg, #1e3a8a, #2563eb);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 36px;
    z-index: 9999;
    box-shadow: 0 6px 18px rgba(0,0,0,0.2);
}

/* LOGO */
.sp-logo {
    font-size: 22px;
    font-weight: 800;
    color: white;
    letter-spacing: 0.4px;
}

/* NAV LINKS */
.sp-nav a {
    color: white;
    text-decoration: none;
    margin-left: 28px;
    font-weight: 500;
    font-size: 15px;
    transition: all 0.2s ease;
}

.sp-nav a:hover {
    opacity: 0.8;
    transform: translateY(-1px);
}

/* SPACE BELOW HEADER */
.spacer {
    height: 90px;
}
</style>

<div class="sp-header">
    <div class="sp-logo">ScreenerPro</div>
    <div class="sp-nav">
        <a href="?page=dashboard">Dashboard</a>
        <a href="?page=jobs">Jobs</a>
        <a href="?page=analytics">Analytics</a>
        <a href="?page=account">Account</a>
        <a href="?page=logout">Logout</a>
    </div>
</div>

<div class="spacer"></div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# NAVIGATION HANDLER
# -------------------------------------------------
query_params = st.query_params
page = query_params.get("page", ["dashboard"])[0]

# -------------------------------------------------
# PAGES
# -------------------------------------------------
def dashboard_page():
    st.title("📊 Dashboard")
    st.write("Welcome to ScreenerPro AI Hiring Platform.")
    st.metric("Resumes Screened", "500,000+")
    st.metric("Accuracy", "97%")

def jobs_page():
    st.title("💼 Job Board")
    st.write("Create, publish, and manage hiring campaigns.")
    st.button("➕ Create New Job")

def analytics_page():
    st.title("📈 Analytics")
    st.write("AI-powered candidate insights & skill match scores.")
    st.bar_chart({"Shortlisted": 120, "Rejected": 340, "Interviewed": 75})

def account_page():
    st.title("👤 Account Settings")
    st.write("Manage profile, security, and preferences.")

def logout_page():
    st.title("👋 Logged Out")
    st.success("You have been logged out successfully.")
    st.write("Thank you for using ScreenerPro.")

# -------------------------------------------------
# ROUTER
# -------------------------------------------------
if page == "dashboard":
    dashboard_page()

elif page == "jobs":
    jobs_page()

elif page == "analytics":
    analytics_page()

elif page == "account":
    account_page()

elif page == "logout":
    logout_page()

else:
    st.error("Page not found")
