import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico",
    layout="wide"
)

def main():
    datacsv = pd.read_csv("data/channidae_7.csv")
    st.dataframe(datacsv)
    
if __name__ == '__main__':
    main()

    #footer aplikasi
    footer_style = """
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117;
    color: #FAFAFA;
    text-align: center;
    padding: 10px;
    """

    st.markdown(
        """
        <footer style='{}'>
            © 2023, Synchronize Team
        </footer>
        """.format(footer_style),
        unsafe_allow_html=True
    )