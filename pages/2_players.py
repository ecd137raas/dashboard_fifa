import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Times", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogadores", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])
st.write(f"**Clube:** {player_stats['Club']}")
st.image(player_stats['Flag'])

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height']}")
col3.markdown(f"**Peso:** {player_stats['Weight']}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

