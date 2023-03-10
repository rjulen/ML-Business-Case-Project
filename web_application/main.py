"""Main module for the streamlit app"""
import streamlit as st

import altair as alt
import src.pages.data_analysis
import src.pages.modeling
from src.utils import _override_color_styles, _streamlit_theme, _load_image

PAGES = {
    "Statistical Analysis on Sales": src.pages.data_analysis,
    "Sales Forecast and Insights": src.pages.modeling,
}


def init():
    """Runs init scripts (color theme and changes)"""
    alt.themes.register("streamlit", _streamlit_theme)
    alt.themes.enable("streamlit")


def main():
    """Main function of the App"""
    init()
    st.sidebar.image(_load_image(), use_column_width=True)
    st.sidebar.title("Navigation Panel")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        page.write()

    st.sidebar.title("Context")
    st.sidebar.info(
        """This an open source project for the Machine Learning Business Case course 
        with the [Wavestone data-lab 👨‍🔬](https://www.wavestone.com/en/). 
        \n Our client is 
        handling around 3 000 stores in 7 different countries and wants to forecast 
        up to 6-weeks of sales given historical data and various features.
        """
    )
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by a team of 5 contributors 💪. You can learn more and
        check out the source code [on Github](https://github.com/SushiFou/ML-Business-Case-Project).
        """
    )


if __name__ == "__main__":
    main()
