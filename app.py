import streamlit as st
from services.summarizer import generate_summary

st.title("Smart Meeting Summary Generator")

meeting_text = st.text_area("Paste meeting notes here", height=220)

if st.button("Generate Summary"):
    if not meeting_text.strip():
        st.warning("Please enter meeting notes")
    else:
        try:
            summary = generate_summary(meeting_text)

            st.subheader("Topics Discussed")
            for t in summary.topics:
                st.write("-", t)

            st.subheader("Key Decisions")
            for d in summary.decisions:
                st.write("-", d)

            st.subheader("Action Items")
            for a in summary.action_items:
                owner = a.owner if a.owner else "Not mentioned"
                due = a.due_date if a.due_date else "Not mentioned"
                st.write(f"- Task: {a.task}, Owner: {owner}, Due: {due}")

        except Exception as e:
            st.error("Failed to generate summary")
            st.exception(e)
