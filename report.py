
import pandas as pd 
import streamlit as st
import plotly.express as px 
import numpy as np
df=pd.read_csv('E:/preprocessing 8/cleaning_df.csv',index_col=0)
st.set_page_config(layout='wide')
state=st.sidebar.selectbox('State',df.state.unique())
city=st.sidebar.selectbox('city',df.city.unique())
Start_date=st.sidebar.date_input('Staer Date',min_value=df['Order Date'].min(),max_value=df['Order Date'].max(),value=df['Order Date'].min())
End_date=st.sidebar.date_input('End Date',min_value=df['Order Date'].min(),max_value=df['Order Date'].max(),value=df['Order Date'].max())
top_n=st.sidebar.slider('Top N',min_value=1,max_value=df['Product'].nunique(),value=5)

df_2 = df[(df['state'] == state) & (df['city'] == city) & (df['Order Date'] >= str(Start_date)) & (df['Order Date'] <= str(End_date))]
st.dataframe(df_2)
prod_count=df_2['Product'].value_counts().reset_index().head(top_n)
st.plotly_chart(px.bar(prod_count,x='Product',y='count',title=f'the nmost popular {top_n}'))
