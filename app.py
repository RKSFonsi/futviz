import streamlit as st
from data.global_stats import get_global_stats, get_table_data


def input_page():
    # Add input elements here
    table_data = get_table_data()
    with open("templates/team_select.html", "r") as f:
        html = f.read()
        html = html.replace("{{variable}}", "Select a team")
        html = html.replace("{{table_data", table_data)
        st.markdown(html, unsafe_allow_html=True)
    with open("design/style.css", "r") as f:
        css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    team = st.text_input("Enter your team: ")
    if st.button("Submit"):
        st.session_state.team = team
        st.experimental_set_query_params(page="output")
        st.experimental_rerun()


def output_page():
    # Load input data from session state
    team = st.session_state.get("team", default=None)
    team = get_global_stats(team)
    if team:
        # Display output using input data
        with open("templates/selected_team.html", "r") as f:
            html = f.read()
            html = html.replace("{{variable}}", team[0])
            st.markdown(html, unsafe_allow_html=True)
        with open("design/style.css", "r") as f:
            css = f.read()
            css = css.replace("--color", team[1])
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.experimental_set_query_params(page="input")
        st.experimental_rerun()


def main():
    # Define page routing based on URL query parameters
    st.set_page_config(layout="wide")
    page = st.experimental_get_query_params().get("page", ["input"])[0]
    if page == "input":
        input_page()
    elif page == "output":
        output_page()


if __name__ == "__main__":
    main()
