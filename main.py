import streamlit as st

st.title("Startup India Seed Fund Scheme Application Form")

# Initialize session state variable
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

# Show the form only if not submitted
if not st.session_state.form_submitted:
    with st.form("user_form"):
        explain_problem_you_are_solving = st.text_area(
            "**Explain the problem you are solving.**", 
            height=100, 
            placeholder="Write your problem here..."
        )
        target_market = st.text_area(
            "**Target Market.**", 
            height=100, 
            placeholder="Write your target market here..."
        )
        your_product_service = st.text_area(
            "**Overview of your product/service.**", 
            height=100, 
            placeholder="Write your overview of your product/service here..."
        )
        competetive_landscape = st.text_area(
            "**Competetive Landscape.**", 
            height=100, 
            placeholder="Write who are your competetiors here..."
        )
        market_validation = st.text_area(
            "**Market Validation.**", 
            height=100, 
            placeholder="Write your market validation here..."
        )
        revenue_model = st.text_area(
            "**Revenue Model.**", 
            height=100, 
            placeholder="Write your revenue model here..."
        )
        market_strategy = st.text_area(
            "**Market Strategy.**", 
            height=100, 
            placeholder="Write your market strategy here..."
        )
        team = st.text_area(
            "**Talk about your Team.**", 
            height=100, 
            placeholder="Write about your team here..."
        )
        financials = st.text_area(
            "**Talk about your Financials.**", 
            height=100, 
            placeholder="Write about your financials here..."
        )
        fund_requirement_deployment_plan = st.text_area(
            "**Talk about your Fund Requirement and Deployment Plan.**", 
            height=100, 
            placeholder="Write about your fund requirement and deployment plan here..."
        )


        submitted = st.form_submit_button("Submit", type="primary")

        if submitted:
            if not all([
                explain_problem_you_are_solving.strip(),
                target_market.strip(),
                your_product_service.strip(),
                competetive_landscape.strip(),
                market_validation.strip(),
                revenue_model.strip(),
                market_strategy.strip(),
                team.strip(),
                financials.strip(),
                fund_requirement_deployment_plan.strip()
            ]):
                st.error("Please fill out all required fields before submitting.")
            else:
                st.session_state.form_submitted = True
                st.session_state.explain_problem_you_are_solving = explain_problem_you_are_solving
                st.session_state.target_market = target_market
                st.session_state.your_product_service = your_product_service
                st.session_state.competetive_landscape = competetive_landscape
                st.session_state.market_validation = market_validation
                st.session_state.revenue_model = revenue_model
                st.session_state.market_strategy = market_strategy
                st.session_state.team = team
                st.session_state.financials = financials
                st.session_state.fund_requirement_deployment_plan = fund_requirement_deployment_plan
                st.success("Form submitted successfully!")
else:
    st.info("You have already submitted the form.")
    st.write("**Explain the problem you are solving:**")
    st.write(st.session_state.explain_problem_you_are_solving)
    st.write("**Target Market:**")
    st.write(st.session_state.target_market)
    st.write("**Overview of your product/service:**")
    st.write(st.session_state.your_product_service)
    st.write("**Competetive Landscape:**")
    st.write(st.session_state.competetive_landscape)
    st.write("**Market Validation:**")
    st.write(st.session_state.market_validation)
    st.write("**Revenue Model:**")
    st.write(st.session_state.revenue_model)
    st.write("**Market Strategy:**")
    st.write(st.session_state.market_strategy)
    st.write("**Team:**")
    st.write(st.session_state.team)
    st.write("**Financials:**")
    st.write(st.session_state.financials)
    st.write("**Fund Requirement and Deployment Plan:**")
    st.write(st.session_state.fund_requirement_deployment_plan)
