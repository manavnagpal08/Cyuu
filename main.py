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
