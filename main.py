import streamlit as st

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="Navbar Header",
    page_icon="💼",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE FOR NAVIGATION
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

def navigate(page):
    st.session_state.page = page

# --------------------------------------------------
# NAVBAR HEADER
# --------------------------------------------------
st.markdown("""
<style>
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 64px;
    background: white;
    border-bottom: 1px solid #e5e7eb;
    display: flex;
    align-items: center;
    padding: 0 40px;
    z-index: 10000;
    font-family: Inter, sans-serif;
}

/* LOGO */
.logo {
    font-size: 26px;
    font-weight: 800;
    color: #0a66c2;
    margin-right: 30px;
}

/* NAV ITEMS */
.nav-items {
    display: flex;
    gap: 24px;
}

.nav-link {
    font-size: 14px;
    color: #374151;
    cursor: pointer;
    padding: 6px 10px;
    border-radius: 6px;
}

.nav-link:hover {
    background: #f3f4f6;
}

/* ACTIVE */
.nav-active {
    color: #0a66c2;
    font-weight: 600;
}

/* RIGHT SIDE */
.right {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 20px;
}

.search input {
    padding: 6px 10px;
    border-radius: 6px;
    border: 1px solid #d1d5db;
    background: #eef3f8;
}

/* PAGE OFFSET */
.content {
    margin-top: 90px;
}
</style>

<div class="navbar">
    <div class="logo">in</div>

    <div class="nav-items">
        <div class="nav-link" onclick="document.getElementById('nav-home').click()">Home</div>
        <div class="nav-link" onclick="document.getElementById('nav-network').click()">My Network</div>
        <div class="nav-link" onclick="document.getElementById('nav-jobs').click()">Jobs</div>
        <div class="nav-link" onclick="document.getElementById('nav-messages').click()">Messages</div>
    </div>

    <div class="right">
        <div class="search">
            <input placeholder="Search" />
        </div>
        <img src="https://i.pravatar.cc/150?img=5"
             style="width:32px;height:32px;border-radius:50%">
    </div>
</div>

<div class="content"></div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HIDDEN STREAMLIT BUTTONS (NAV LOGIC)
# --------------------------------------------------
col = st.columns(4)

with col[0]:
    st.button("Home", key="nav-home", on_click=navigate, args=("Home",), help="Home")
with col[1]:
    st.button("Network", key="nav-network", on_click=navigate, args=("Network",))
with col[2]:
    st.button("Jobs", key="nav-jobs", on_click=navigate, args=("Jobs",))
with col[3]:
    st.button("Messages", key="nav-messages", on_click=navigate, args=("Messages",))

# --------------------------------------------------
# PAGE CONTENT
# --------------------------------------------------
st.header(st.session_state.page)

if st.session_state.page == "Home":
    st.write("🏠 Welcome to Home")
elif st.session_state.page == "Network":
    st.write("👥 My Network Page")
elif st.session_state.page == "Jobs":
    st.write("💼 Jobs Page")
elif st.session_state.page == "Messages":
    st.write("💬 Messages Page")

for i in range(20):
    st.write(f"Scrollable content line {i+1}")
