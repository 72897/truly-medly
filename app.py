import streamlit as st
from agents.planner import create_plan
from agents.executor import ExecutorAgent
from agents.verifier import verify

st.set_page_config(page_title="AI Operations Assistant")

st.title("AI Operations Assistant")
st.caption("Planner → Executor → Verifier | Powered by Gemini")

task = st.text_area(
    "Enter your task",
    placeholder="Find top Python GitHub repos and weather in Delhi"
)

if st.button("Run"):
    if not task.strip():
        st.warning("Please enter a task.")
    else:
        with st.spinner("Planning..."):
            plan = create_plan(task)

        with st.spinner("Executing..."):
            executor = ExecutorAgent()
            results = executor.execute(plan)

        with st.spinner("Verifying..."):
            final_output = verify(task, results)

        st.subheader("Final Output")
        st.json(final_output)
