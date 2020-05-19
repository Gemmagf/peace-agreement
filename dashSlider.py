import streamlit as st
import streamlit_theme as stt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import seaborn as sns
import altair as alt



# Paleta de colors :  titol:#8AB3BA text general: #D0D3DA relguerra: #B2D0EB  norelgerra: #8AB3BA
# streamlit run dash.py

# Titol i subtitol
st.markdown("<h1 style='text-align: center; color: #8AB3BA;'>PEACE AGREEMENTS IN EUROPE FROM 1991 TO 2019</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D0D3DA;'>Gemma Garcia de la Fuente", unsafe_allow_html=True)

# Finestra parametres
# st.sidebar.title("Filters")
# st.sidebar.info("Here you can filter by diferent vairbales in orther to get the specific infomration you're interest about")


# Grafic per veure el nombre d'acords al llarg del temps

dd = pd.read_excel('AnysRGuer.xlsx') 
fig1 = px.scatter(dd, x='Any' , y='Casos', color = 'RelGuerra',color_discrete_map={'War Related': '#B2D0EB', 'No War Related': '#8AB3BA'}, size = 'Casos',width=770, height=300)
fig1.update_layout(showlegend=False)
fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig1)


# Selecionar any i veure quins acords predominen
#st.info('1.Select the year')
stt.set_theme({'primary': '#1b3388'})
any = st.slider('Data', 1991,2019, (1997,2012) )  # min: 0, max: 23
fig = make_subplots(rows=1, cols=2)


year = dd[(dd['Any']>=any[0])& (dd['Any']<=any[1])]
WR = year.loc[(year['RelGuerra'] == 'War Related')]
NWR = year.loc[(year['RelGuerra'] == 'No War Related')]

ds = pd.Series({'War Related' : (len(WR)*100)/len(year), 'No War Related' : (len(NWR)*100)/len(year)})

Xlim = 10
Ylim = 10
Xpos = 0
Ypos = 0 ##change to zero for upwards
series = []
for name, count in ds.iteritems():
    x = []
    y = []
    for j in range(0, (int(round(count)))):
        if Xpos == Xlim:
            Xpos = 0
            Ypos -= 1 ##change to positive for upwards
        x.append(Xpos)
        y.append(Ypos)
        Xpos += 1
    series.append(go.Scatter(x=x, y=y, mode='markers', marker=dict(symbol = 'circle', size= 15, color=['#B2D0EB','#8AB3BA']), name=f'{name} ({count})'))


fig2 = go.Figure(dict(data=series, layout=go.Layout(
    paper_bgcolor='rgba(255,255,255,1)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(showgrid=False,zeroline= False, showline=False, visible=False, showticklabels=False),
    yaxis=dict(showgrid=False,zeroline= False, showline=False, visible=False, showticklabels=False),
    showlegend=False
)))
st.plotly_chart(fig2)


# Drets humans

#dd = pd.read_excel('DretsHum.xlsx')
#labels = ['HrfSp','HrfBor','HrfTinc','HrfOth']
#fig3 = go.Figure(go.Treemap(labels = labels,marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]))
#st.plotly_chart(fig3)

# Estat dels acords guardat per motiu de l'acords
# st.sidebar.info('2.Select agreement status')
stat = st.selectbox('Select the status of the agreement',('Multiparty signed/agreed','Unilateral document','Agreement with subsequent status','Status unclear')) 

df = pd.read_excel('Estat.xlsx')
df = df.loc[df['Status'] == stat]
fig4 = px.bar(df, x="Count", y="Contp", color='RelGuerra',color_discrete_map={'War Related': '#B2D0EB', 'No War Related': '#8AB3BA'}, orientation='h')
fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig4.update_layout(showlegend=False)
st.plotly_chart(fig4)



# Aspecte fisic dels Acords de pau
lletres = st.slider('Characters', 329,197656, (329,197656))
pag = st.slider('Pages', 1,149, (1,100))
dd = pd.read_excel('Europa2.xlsx')
dd = dd[(dd['Lgt']>=pag[0])& (dd['Lgt']<=pag[1])]
dd = dd[(dd['N_characters']>=lletres[0])& (dd['Lgt']<=lletres[1])]
# dd= dd[(dd['Dat']>=any[0])& (dd['Dat']<=any[1])] per algun motiu si considero aquest filtre em falla
fig5 = px.scatter(dd, x='Lgt' , y='N_characters', color = 'RelGuerra',color_discrete_map={'War Related': '#B2D0EB', 'No War Related': '#8AB3BA'} ,width=770, height=500)
fig5.update_layout(showlegend=False)
fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig5)


# Grafic per grups
grups = st.multiselect('Which groups to you whant to consider?',options=['GChRhet', 'GChSubs','GDisRhet','GDisAntid','GDisSubs','GAgeRhet','GAgeAntid','GAgeSubs','GMig','GMigSubs','GRaRhet','GRaAntid','GRaSubs','GReRhet','GReAntid','GReSubs','GOth','GOthAntid','GRefRhet','GRefSubs','GRefOth','GSoc','GSocAntid'], default=['GDisSubs','GChRhet','GReAntid','GRefRhet'])

df =pd.read_excel('agurpacions4.xlsx')
df2 = pd.DataFrame()
for i, grup in enumerate(grups):
    df2 = df2.append(df.loc[df['Grup'] == grup])
r = np.arange(1,24)
#names =['GChRhet', 'GChSubs','GDisRhet','GDisAntid','GDisSubs','GAgeRhet','GAgeAntid','GAgeSubs','GMig','GMigSubs','GRaRhet','GRaAntid','GRaSubs','GReRhet','GReAntid','GReSubs','GOth','GOthAntid','GRefRhet','GRefSubs','GRefOth','GSoc','GSocAntid']
#fig7 = go.Figure()

fig7= make_subplots(rows=1, cols=2, shared_yaxes=True)
fig7.add_trace(go.Bar(x=grups, y=df2['NWR'], name='No War Related',  marker_color='#8AB3BA'))
fig7.add_trace(go.Bar(x=grups, y=df2['WR'], name= 'War Related', marker_color='#B2D0EB'))
fig7.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
fig7.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig7.update_layout(showlegend=False)
st.plotly_chart(fig7)


# MAPA

df = pd.read_excel('geo.xlsx')
df['text'] = df['name'] + '<br>Agreements : ' + (df['pop']).astype(str)
limits = [(1,3),(4,5),(6,7)]
colors = ["#B2D0EB","#033742","#8AB3BA"]
cities = []
scale = 0.001
fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        marker = dict(
            size = df_sub['pop']/scale,
            color = colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1])))

fig.update_layout(
        showlegend = True,
        geo = dict(
            scope = 'europe',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

st.plotly_chart(fig)
