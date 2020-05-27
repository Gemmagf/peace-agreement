import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from pywaffle import Waffle
import seaborn as sns
import altair as alt



# Paleta de colors :  titol:#e73575 text general: #D0D3DA relguerra: #ed6d9b  norelgerra: #8AB3BA
# streamlit run dash.py

# Titol i subtitol
st.markdown("<h1 style='text-align: center; color: #ed6d9b;font-family:verdana;font-size:250%;'>PEACE AGREEMENTS IN EUROPE FROM 1991 TO 2019</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;font-family:verdana; color: #D0D3DA;'>Gemma Garcia de la Fuente\n", unsafe_allow_html=True)
st.markdown(" ")
st.markdown("\n ")

# Finestra parametres
# st.sidebar.title("Filters")
# st.sidebar.info("Here you can filter by diferent vairbales in orther to get the specific infomration you're interest about")


# Grafic per veure el nombre d'acords al llarg del temps
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'> After wars, many issues have to be taken care of.", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #e73575;font-family:verdana;font-size:150%;'>TOTAL: 410 agreements </h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;color: #5e5e5e;font-family:verdana;font-size:90%;'> This is a dashboard to explore how Europe maintained its peace between countries from 1991 to 2019. Specifically, we will explore which type of agreements were going in this period of time. ", unsafe_allow_html=True)

dd = pd.read_excel('AnysRGuer.xlsx') 
fig1 = px.scatter(dd, x='Any' , y='Casos', color = 'RelGuerra',color_discrete_map={'War Related': '#e73575', 'No War Related': '#D0D3DA'}, size = 'Casos',width=770, height=300)
fig1.update_layout(showlegend=False)
fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig1)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'> As we can see the amount of agreements reduced with time. Also, most of them were mainly before 2000, and war-related. From this, we can extract that war led with many unclear issues that had to be taken care of. Also, we can appreciate a slight increase of non-war related agreements initiated in 2010.", unsafe_allow_html=True)


# Selecionar any i veure quins acords predominen

any = st.slider('Data', 1991,2019, (1997,2012) )  # min: 0, max: 23
fig = make_subplots(rows=1, cols=2)


year = dd[(dd['Any']>=any[0])& (dd['Any']<=any[1])]
WR = year.loc[(year['RelGuerra'] == 'War Related')]
NWR = year.loc[(year['RelGuerra'] == 'No War Related')]

ds = pd.Series({'War Related' : (len(WR)*100)/len(year), 'No War Related' : (len(NWR)*100)/len(year)})

fig2 = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=ds, 
    colors=("#ed6d9b", "#D0D3DA"),
    icons='circle', icon_size=15, icon_legend=False)
    
st.pyplot(fig2)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'> After a little exploring with the dot matrix, it is easy to see that most years have both types of agreements even in the most recent ages. Despite that, there are a few years where just one type of agreement occurred: 2003 just had war-related agreements whereas 2015 had non-war related ones.", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>", unsafe_allow_html=True)


# Estat dels acords guardat per motiu de l'acords
tipus = st.selectbox('Type of agreements',('All typs','War Related','No War Related'))
stat = st.selectbox('Select the status of the agreement',('Multiparty signed/agreed','Unilateral document','Agreement with subsequent status','Status unclear')) 

fig47 = make_subplots(
    rows=1, cols=2,
    specs=[[{}, {}]])
    
df = pd.read_excel('Estat.xlsx')
df = df.loc[(df['Status'] == stat)]
if tipus != 'All typs':
    dd = dd.loc[dd['RelGuerra'] == tipus]

fig47.add_trace(go.Bar(x=df["Count"], y=df["Contp"], orientation='h',marker_color='#e73575'), row=1, col=1)




# Aspecte fisic dels Acords de pau

pag = st.slider('Pages', 1,149, (1,10))
dd = pd.read_excel('Europa2.xlsx')
dd = dd[(dd['Lgt']>=pag[0])& (dd['Lgt']<=pag[1])]
if tipus != 'All typs':
    dd = dd.loc[dd['RelGuerra'] == tipus]
#dd = dd[(dd['N_characters']>=lletres[0])& (dd['Lgt']<=lletres[1])]

#hola = go.Scatter(x=dd['Lgt'] , y=dd['N_characters'],mode='markers', marker=dict(symbol = 'circle', size= 5, color='#B2D0EB'))

#fig47.add_trace(hola, row=1, col=2)
fig47.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig47.update_layout(showlegend=False)
fig47.add_trace(go.Histogram2dContour(x=dd['Lgt'] , y=dd['N_characters'], nbinsx=5, nbinsy=5,colorscale = 'PuRd'), row=1, col=2)



#hola = plt.hexbin(x=dd['Lgt'] , y=dd['N_characters'],color='#e73575',gridsize=20 )
#fig47.add_trace(hola, row=1, col=2)
fig47.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig47.update_layout(showlegend=False)
st.plotly_chart(fig47)


st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>It seems like the main reasons why the agreements are done in both cases are:", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #e73575;font-family:verdana;font-size:150%;'>Territorial and also Governmental", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>Once the content of the agreements have been briefly analyzed, we can take a look at the physical aspects. Many of the agreements, regardless of the type, are short in terms of the number of pages. ", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #e73575;font-family:verdana;font-size:150%;'>The mean number of pages is 3,89 ", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>When focusing on the filter, the non-war related agreements seem to be longer, or at least some of them seem to be, than the war-related ones, with just one exception are all under the 50 pages.", unsafe_allow_html=True)
st.markdown(" ")
st.markdown("\n ")

# Grafic per grups

grups = st.multiselect('Which groups to you whant to consider?',options=['Children/Youth','Disabled persons','Elderly/Age','Migrant workers','Racial/ethnic/national groups','Religious groups','Other groups','Refugees/ displaced persons','Social Class'], default=['Children/Youth','Migrant workers','Racial/ethnic/national groups'])
st.markdown(" ")
st.markdown("\n ")

df =pd.read_excel('agurpacions4.xlsx')
df2 = pd.DataFrame()
for i, grup in enumerate(grups):
    df2 = df2.append(df.loc[df['Grup'] == grup])
r = np.arange(1,24)

fig7 = go.Figure()
fig7.add_trace(go.Scatter(
    x=grups, y=df2["NWR"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#D0D3DA'),
    stackgroup='one' # define stack group
))
fig7.add_trace(go.Scatter(
    x=grups, y=df2["WR"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#e73575'),
    stackgroup='one'
))
fig7.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',width=770,height=500)
fig7.update_layout(showlegend=False)
st.plotly_chart(fig7)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>Most popular groups being considered in the agreements are refugees (preambular and comprehensive commitment) and Racial/ethnic/national groups.", unsafe_allow_html=True)
st.markdown(" ")
st.markdown("\n ")


# MAPA

df = pd.read_excel('geo2.xlsx')

fig = go.Figure(go.Choropleth(
    locations = df['name'],
    locationmode = "country names",
    z = df['pop'],
    colorscale = 'PuRd',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='#5e5e5e',
    marker_line_width=0.1
    )
)
 
fig.update_layout(
    showlegend = False,
    geo = dict(
        scope='europe',
        resolution=110,
        projection_type='miller',
        showcoastlines=True,
        showocean=True,
        showcountries=True,
        landcolor = 'rgb(255, 255, 255)',
        oceancolor='#fff',
        lakecolor='#fff',
        coastlinecolor='#dadada'
    )
)
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',width=900,height=500)
# paquet per fer gratics plotinum
st.plotly_chart(fig)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>Finally, in this graph we can appreciate not only which countries had more agreements going on or done, but also which of them had made more agreements.For example, we can see that ", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #e73575;font-family:verdana;font-size:150%;'>Former Yugoslavia, Russia and Georgia", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>Were the countries with more agreements going on whereas countries such as:", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #e73575;font-family:verdana;font-size:150%;'>Afghanistan, Spain and Macedonia ", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;color: #5e5e5e; font-family:verdana;font-size:90%;'>had made just one agreement that period.", unsafe_allow_html=True)

