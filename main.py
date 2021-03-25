import streamlit as st
from get_ncaam_bb import ncaam_bb
from get_nba import nba
from get_mlb import mlb

st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/\
bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"\
 crossorigin="anonymous">', unsafe_allow_html=True)

page = st.sidebar.selectbox(
    'What sport do you want to bet on?',
    ("NCAA Men's Basketball", 'Major League Baseball (MLB)', 'National Basketball Association (NBA)')
)
if page == "NCAA Men's Basketball":
    st.title("NCAA Men's Basketball Point Spread")
    st.table(ncaam_bb)
elif page == 'Major League Baseball (MLB)':
    st.title("MLB Point Spread")
    st.table(mlb)
elif page == 'National Basketball Association (NBA)':
    st.title("NBA Point Spread")
    st.table(nba)
