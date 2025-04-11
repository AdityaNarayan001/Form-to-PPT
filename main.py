import streamlit as st
from utils.ppt_gen import generate_presentation
from utils.llm import llm

st.set_page_config(page_title="Seed Fund Form", layout="centered")
st.title("Startup India Seed Fund Scheme Application Form")

enable_LLM = st.checkbox("**Enable LLM to re-write your answers for better clarity.**")

# Initialize session state variables
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

if "show_download" not in st.session_state:
    st.session_state.show_download = False

# Show form if not submitted
if not st.session_state.form_submitted:
    with st.form("user_form"):
        ppt_heading = st.text_area("**Project Title.**", height=100, placeholder="Enter Project Title Here...")
        explain_problem_you_are_solving = st.text_area("**Explain the problem you are solving.**", height=100, placeholder="Enter Problem You Are Solving Here...")
        target_market = st.text_area("**Target Market.**", height=100, placeholder="Enter Target Market Here...")
        your_product_service = st.text_area("**Overview of your product/service.**", height=100, placeholder="Enter Product Service Overview Here...")
        competetive_landscape = st.text_area("**Competetive Landscape.**", height=100, placeholder="Enter Competetive Landscape Here...")
        market_validation = st.text_area("**Market Validation.**", height=100, placeholder="Enter Market Validation Here...")
        revenue_model = st.text_area("**Revenue Model.**", height=100, placeholder="Enter Revenue Model Here...")
        market_strategy = st.text_area("**Market Strategy.**", height=100, placeholder="Enter Market Strategy Here...")
        team = st.text_area("**Talk about your Team.**", height=100, placeholder="Enter Team Details Here...")
        financials = st.text_area("**Talk about your Financials.**", height=100, placeholder="Enter Financials Here...")
        fund_requirement_deployment_plan = st.text_area("**Talk about your Fund Requirement and Deployment Plan.**", height=100, placeholder="Enter Fund Requirement and Deployment Plan Here...")

        submitted = st.form_submit_button("Submit", type="primary")

        if submitted:
            # Validate all fields
            if not all([
                ppt_heading.strip(),
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
                # Save to session state
                st.session_state.ppt_heading = ppt_heading
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

                st.session_state.form_submitted = True
                st.session_state.show_download = True
                st.rerun()

# After form is submitted...
elif st.session_state.show_download:
    st.success("Form submitted successfully! 🎉")

    if enable_LLM:
        with st.spinner("Generating presentation..."):
            generate_presentation(st.session_state.ppt_heading, llm(st.session_state.explain_problem_you_are_solving))
    else:
        with st.spinner("Generating presentation..."):
            generate_presentation(st.session_state.ppt_heading, st.session_state.explain_problem_you_are_solving)

    ppt_path = "/Users/aditya.narayan/Desktop/form-to-ppt/output/auto-generated-ppt.pptx" 

    try:
        with open(ppt_path, "rb") as f:
            ppt_bytes = f.read()

        # Center the download button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Download Your PowerPoint Presentation",
                data=ppt_bytes,
                file_name="Seed_Fund_Application.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                use_container_width=True
            )
    except FileNotFoundError:
        st.error("PowerPoint file not found. Please check the path.")

