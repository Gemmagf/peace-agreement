import streamlit as st
import plotly.graph_objects as go 
import pandas as pd
import webbrowser



st.markdown("<h1 style='text-align: center; color: #2f8b90;font-family:verdana;font-size:200%;'>Gemma Garcia de la Fuente</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;font-family:verdana; color: #D0D3DA;'>Email: gemmagdlf@gmail.com\n", unsafe_allow_html=True)
st.write("# ")
st.write("# ")


tipus = st.selectbox('Select area of interest',('Education','Language Study','Design','Programing','Databases'))
dd = pd.read_excel('Crono_estudis.xlsx') 
 
dd2 = dd.loc[(dd['Type']==tipus)]
color = ['#245d60','#2e7c81','#18a0a7','#4eb5ba','#6adbe1','#9fdcdf']

st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #000000;font-size:100%'>You are looking at the different aspects I have been working on, and also appreciate the amount of time I have spent on each of them:", unsafe_allow_html=True)
fig = go.Figure(go.Pie(values = dd2['Label'], labels = dd2['Study'],texttemplate = "%{label} ", textposition = "outside", hole=.5,marker_colors=color))

fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig.update_layout(showlegend=False)
st.plotly_chart(fig)

if tipus == 'Education':
    st.markdown("<h1 style='text-align: justify;color: #2f8b90;font-family:verdana;font-size:100%;'>Highlights", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #000000;font-size:100%'>There are several things worth noting regarding my official studies. Starting with Pycology is worth mentioning 2 facts:", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> 1- I graduated in a Social Mencion, which means the study of group behavior.  This psychology branch is directly related and useful when it comes to analyzing and understands the results of data regarding humans routines, movements, the decisions, evolution,...", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> 2- My final project was Data analysis related, although I had no programing lectures during the degree. The project consist in simulating a network between contacts on Facebook and analyze the different agents and roles. The project was graded with an excellent and really well appreciated by the teachers' court ", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #000000;font-size:100%'> While studying psychology I realize I miss Maths, so I decided to start simultaneously a Statistics degree. During my studies in here I'lll mention 3 facts:  ", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> 1- Programing become one of my hobbies. My interest on it help me to get an honor as a subject grade, in the programing related classes ", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> 2- I collaborated with some teacher with an article which we manage to publish in a really well known Journal. The link to the article inn which I appear as a co-author is this one:  ", unsafe_allow_html=True)
    
    url = 'https://www.sciencedirect.com/science/article/pii/S0933365719311595'

    if st.button('Article'):
        webbrowser.open_new_tab(url)
        st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'>   ", unsafe_allow_html=True)
    st.image('cita.jpg')  

if tipus == 'Language Study':
    st.markdown("<h1 style='text-align: justify;color: #2f8b90;font-family:verdana;font-size:100%;'>Highlights", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #000000;font-size:100%'> My main way of learning languages has been traveling and staying for long periods of times in the different locations.  ", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> * English: I've been in the united states a period of a month or a month and a half for 6 different summers. Apart from that I've also been in the different academies in with I finally end up getting a Cambridge certification  ", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> * French: In this particular case I spend a whole school year living with a host family in France in which I attempted school as a local. Also, I got a certification in a B2 level.  ", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> * Italian: I spend two summers in Milan, Where I attended language school, but also I work as a waitress in an ice-cream house.  ", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'> * Chinese: After a whole year studying the language I spend a month an a half living in Beijing and attending language school there  ", unsafe_allow_html=True)
    
if tipus == 'Desing':
    st.markdown("<h1 style='text-align: justify;color: #2f8b90;font-family:verdana;font-size:100%;'>Highlights", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'>   ", unsafe_allow_html=True)


st.markdown("<h3 style='text-align: justify;font-family:verdana; color: #565656;font-size:100%'>   ", unsafe_allow_html=True)
