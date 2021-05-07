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
    if type(ncaam_bb) != str:
        st.title("NCAA Men's Basketball Point Spread")
        st.table(ncaam_bb)
    else:
        st.markdown("<h4>There are no upcoming Men's NCAA Basketball Games.<h4>", unsafe_allow_html=True)
elif page == 'Major League Baseball (MLB)':
    if type(mlb) != str:
        st.title("MLB Point Spread")
        st.table(mlb)
    else:
        st.markdown("<h4>There are no upcoming Major League Baseball Games.<h4>", unsafe_allow_html=True)
elif page == 'National Basketball Association (NBA)':
    if type(nba) != str:
        st.title("NBA Point Spread")
        st.table(nba)
    else:
        st.markdown("<h4>There are no upcoming National Basketball Association Games.<h4>", unsafe_allow_html=True)

