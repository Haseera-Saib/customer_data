import streamlit as st 
import pandas as pd 
import plotly.express as px

data=pd.read_csv('/mentornow/Wholesale_customers_data.csv')
#st.write(data)

st.header('Wholesale Customer Details')

a=data['Region'].unique()
dis=['Kochi','Kollam','Kozhikod']
s= st.sidebar.selectbox("Select Region",(a),format_func=lambda y:dis[y-1])

b=data['Channel'].unique()
display=['Hotel','Retail']
s2= st.sidebar.selectbox("Select Channel",(b),format_func=lambda x:display[x-1])



c1,c2,c3=st.columns(3)
df=data[data['Region']==s]

df1=df[df['Channel']==s2]

c1.metric(label='Total Fresh ', value=round(df1['Fresh'].sum(),2))

c2.metric(label='Total Milk ', value=round(df1['Milk'].sum(),2))

c3.metric(label='Total Grocery ', value=round(df1['Grocery'].sum(),2))

cl1,cl2,cl3=st.columns(3)

cl1.metric(label='Total Frozen ', value=round(df1['Frozen'].sum(),2))
cl2.metric(label='Total Detergents Paper ', value=round(df1['Detergents_Paper'].sum(),2))
cl3.metric(label='Total Delicassen ', value=round(df1['Delicassen'].sum(),2))

#st.write(df1)
st.header('Bar chart')
totals = {
    'Fresh': round(df1['Fresh'].sum(), 2),
    'Milk': round(df1['Milk'].sum(), 2),
    'Grocery': round(df1['Grocery'].sum(), 2),
    'Frozen': round(df1['Frozen'].sum(), 2),
    'Detergents Paper': round(df1['Detergents_Paper'].sum(), 2),
    'Delicassen': round(df1['Delicassen'].sum(), 2)
}


st.bar_chart(totals)

st.header('Pie chart ')
fig = px.pie(values=list(totals.values()), 
              names=list(totals.keys()), 
              title='Distribution of Categories')

st.plotly_chart(fig)

