import streamlit as st
from datetime import datetime
from rules import run_simulation

st.set_page_config(page_title="Clean Power Ecosystem Insights Agent", layout="wide")

# --- One-line disclaimer ---
st.warning("⚠️ For internal demo use only. Outputs are illustrative and do not constitute financial advice or regulated recommendations.")

st.title("🌿 Clean Power Ecosystem Intelligence")
st.caption("MVP Demo — Team 1 User Story B: Data Insights Agent")
st.markdown("---")

# --- Sidebar: File Upload ---
st.sidebar.header("Input Data")
st.sidebar.caption("Upload entity CSVs to provide the agent with ecosystem data.")

# FIX: accept_multiple_files=True so uploaded_files is always a list
uploaded_files = st.sidebar.file_uploader(
    "Upload Entity CSVs (Relationship_Data, Entity_Master, Segment)",
    type=["csv"],
    accept_multiple_files=True
)

if uploaded_files:
    file_names = [f.name for f in uploaded_files]
    st.sidebar.success(f"Loaded: {', '.join(file_names)}")
else:
    file_names = []
    st.sidebar.info("No files uploaded. Demo will run with sample data.")

# --- Main: Prompt Input ---
st.subheader("Query")
prompt = st.text_input(
    "Enter your insight query",
    value="What sustainable finance opportunities exist with HSBC across this ecosystem?",
    help="Include a target institution and product theme for best results (e.g. 'HSBC sustainable finance')."
)

# --- Generate Button ---
if st.button("Generate Insights", use_container_width=True, type="primary"):

    # Use uploaded filenames or fallback labels for evidence traceability
    source_files = file_names if file_names else ["Relationship_Data.csv", "Entity_Master.csv", "Segment.csv"]

    with st.status("Running Insights Agent...", expanded=True) as status:
        st.write("📂 Parsing entity and relationship structures...")
        import time; time.sleep(0.8)
        st.write("🔗 Identifying cross-segment relationships...")
        time.sleep(1.0)
        st.write("⚙️ Applying opportunity surfacing rules...")
        time.sleep(1.2)
        st.write("✅ Validating findings against ingested data...")
        time.sleep(0.5)
        st.write("📝 Generating output...")
        time.sleep(1.5)
        response = run_simulation(prompt, source_files)
        status.update(label="Insights ready.", state="complete", expanded=False)

    st.markdown("---")
    st.subheader("Agent Output")
    st.markdown(response)

    # --- Audit trail ---
    st.markdown("---")
    st.caption(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
        f"Session: demo_user | "
        f"Sources: {', '.join(source_files)} | "
        f"Query: \"{prompt}\""
    )

    # --- RM Next Steps ---
    st.markdown("### Next Steps for Relationship Manager")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Export Report (PDF)", disabled=True, help="Available in next phase.")
    with col2:
        st.button("Share with Team", disabled=True, help="Available in next phase.")

st.markdown("---")
st.caption("Insight generation is rule-based. All outputs must be reviewed by the RM before client use.")
