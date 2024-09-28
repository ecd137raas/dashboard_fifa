import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets\FIFA23_official_data.csv")
    #df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value"] > "0"]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.write("# FIFA23 OFFICIAL DATASET ⚽")
st.write("""Dataset The dataset contains +17k unique players and more than 60 columns, 
            general information and all KPIs the famous videogame offers. As the esport 
            scene keeps rising espacially on FIFA, I thought it can be useful for the community (kagglers and/or gamers)""")
st.sidebar.markdown("Desenvolvido por: [Emerson Duarte](https://github.com/ecd137raas)")