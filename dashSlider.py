import streamlit as st
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
st.markdown("<h1 style='text-align: center; color: #8AB3BA;'>PEACE AGREEMENTS IN EUROP FROM 1991 TO 2019</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D0D3DA;'>Gemma Garcia de la Fuente", unsafe_allow_html=True)

# Finestra parametres
st.sidebar.title("Filters")
st.sidebar.info("Here you can filter by diferent vairbales in orther to get the specific infomration you're interest about")
st.sidebar.info('1.Select the year')
any = st.sidebar.slider('Data', 1991,2019, (1997,2012) )  # min: 0, max: 23
st.sidebar.info('2.Select agreement status')
stat = st.sidebar.selectbox('Select the status of the agreement',('Multiparty signed/agreed','Unilateral document','Agreement with subsequent status','Status unclear')) 
st.sidebar.info('3.Physical aspects, select the number of pages and the amount of charaters')
lletres = st.sidebar.slider('Characters', 329,197656, (329,197656))
pag = st.sidebar.slider('Pages', 1,149, (1,100))
grups = st.sidebar.multiselect('Which groups to you whant to consider?',options=['GChRhet', 'GChSubs','GDisRhet','GDisAntid','GDisSubs','GAgeRhet','GAgeAntid','GAgeSubs','GMig','GMigSubs','GRaRhet','GRaAntid','GRaSubs','GReRhet','GReAntid','GReSubs','GOth','GOthAntid','GRefRhet','GRefSubs','GRefOth','GSoc','GSocAntid'], default=['GDisSubs','GChRhet','GReAntid','GRefRhet'])

# Grafic per veure el nombre d'acords al llarg del temps

dd = pd.read_excel('AnysRGuer.xlsx') 
fig1 = px.scatter(dd, x='Any' , y='Casos', color = 'RelGuerra',color_discrete_map={'War Related': '#B2D0EB', 'No War Related': '#8AB3BA'}, size = 'Casos',width=770, height=300)
fig1.update_layout(showlegend=False)
fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig1)


# Selecionar any i veure quins acords predominen
fig = make_subplots(rows=1, cols=2)

year = dd[(dd['Any']>=any[0])& (dd['Any']<=any[1])]
fig2 = px.bar(year, x="RelGuerra", y="Casos", color="RelGuerra",color_discrete_map={'War Related': '#B2D0EB', 'No War Related': '#8AB3BA'})
fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig2.update_layout(showlegend=False)
st.plotly_chart(fig2)

# Drets humans

#dd = pd.read_excel('DretsHum.xlsx')
#labels = ['HrfSp','HrfBor','HrfTinc','HrfOth']
#fig3 = go.Figure(go.Treemap(labels = labels,marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]))
#st.plotly_chart(fig3)

# Estat dels acords guardat per motiu de l'acords

df = pd.read_excel('Estat.xlsx')
df = df.loc[df['Status'] == stat]
fig4 = px.bar(df, x="Count", y="Contp", color='RelGuerra',color_discrete_map={'War Related': '#B2D0EB', 'No War Related': '#8AB3BA'}, orientation='h')
fig4.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
fig4.update_layout(showlegend=False)
st.plotly_chart(fig4)



# Aspecte fisic dels Acords de pau

dd = pd.read_excel('Europa2.xlsx')
dd = dd[(dd['Lgt']>=pag[0])& (dd['Lgt']<=pag[1])]
dd = dd[(dd['N_characters']>=lletres[0])& (dd['Lgt']<=lletres[1])]
# dd= dd[(dd['Dat']>=any[0])& (dd['Dat']<=any[1])] per algun motiu si considero aquest filtre em falla
fig5 = px.scatter(dd, x='Lgt' , y='N_characters', color = 'RelGuerra',color_discrete_map={'War Related': '#B2D0EB', 'No War Related': '#8AB3BA'} ,width=770, height=500)
fig5.update_layout(showlegend=False)
fig5.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig5)


# Grafic per grups
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

if __name__ == '__main__':
    main()
