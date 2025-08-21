from datetime import datetime
from research_crew.crew import ResearchPaperCrew
import warnings
warnings.filterwarnings("ignore")
import streamlit as st

def run_crew():
    """Run The Crew"""
    inputs = {
        'date':datetime.now().strftime("%Y-%m-%d")
    }

    try:
        with st.spinner('Finding the best paper'):

            result = ResearchPaperCrew().crew().kickoff(inputs=inputs)
            return result

    except Exception as e:
        raise Exception(f"An error occured while running the crew: {e}")


st.title("Find the trending today's AI Agents research paper with summary ")

if st.button("Find Paper"):
    result = run_crew()

    if result:
        st.success("Analysis Completed")

        with st.expander("Research Paper Analysis Results", expanded=True):
            st.markdown("### Final Report")
            st.write(result.raw)
    else:
        st.error("Failed to generate analysis.")
