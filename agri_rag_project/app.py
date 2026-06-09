import streamlit as st
from rag_logic import get_answer

st.title("AgriRAG - Agricultural Policy Chatbot")
st.write("Ask any question about government agricultural schemes and policies.")

with st.sidebar:
    st.header("Your Profile (optional)")
    income = st.number_input("Annual Income (₹)", min_value=0, value=0, step=10000)
    land = st.number_input("Land Size (hectares)", min_value=0.0, value=0.0, step=0.5)
    use_profile = st.checkbox("Use profile for recommendations")

query = st.text_input("Enter your question:", placeholder="e.g. What is PM-Kisan eligibility?")

if st.button("Ask") and query:
    with st.spinner("Searching policies..."):
        try:
            inc = income if use_profile else None
            lnd = land if use_profile else None
            answer, citations, rule_tips = get_answer(query, inc, lnd)

            st.subheader("Answer")
            st.write(answer)

            if rule_tips:
                st.subheader("Policy Recommendations Based on Your Profile")
                for tip in rule_tips:
                    st.success(tip)

            if citations:
                st.subheader("Sources")
                for c in citations:
                    st.caption(c)

        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Make sure you ran ingest_policies.py first and your API key is set.")