
# import pandas as pd 
# import streamlit as st
# import plotly.express as px 
# import numpy as np
# df = pd.read_csv('cleaning_df.csv', index_col=0)
# st.set_page_config(layout='wide')
# state=st.sidebar.selectbox('State',df.state.unique())
# city=st.sidebar.selectbox('city',df.city.unique())
# Start_date=st.sidebar.date_input('Staer Date',min_value=df['Order Date'].min(),max_value=df['Order Date'].max(),value=df['Order Date'].min())
# End_date=st.sidebar.date_input('End Date',min_value=df['Order Date'].min(),max_value=df['Order Date'].max(),value=df['Order Date'].max())
# top_n=st.sidebar.slider('Top N',min_value=1,max_value=df['Product'].nunique(),value=5)

# df_2 = df[(df['state'] == state) & (df['city'] == city) & (df['Order Date'] >= str(Start_date)) & (df['Order Date'] <= str(End_date))]
# st.dataframe(df_2)
# prod_count=df_2['Product'].value_counts().reset_index().head(top_n)
# st.plotly_chart(px.bar(prod_count,x='Product',y='count',title=f'the nmost popular {top_n}'))
# --------------------------------------------------------------------------

import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# لازم الأول
st.set_page_config(layout='wide', page_title='Sales EDA', initial_sidebar_state='expanded')

# اقرأ الملف
df = pd.read_csv('cleaning_df.csv', index_col=0)

# حوّل التاريخ قبل استخدامه
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
min_d = df['Order Date'].min().date()
max_d = df['Order Date'].max().date()

# --- SIDEBAR ---
state = st.sidebar.selectbox('State', df['state'].dropna().unique())
# خلي المدن تعتمد على الولاية المختارة
city_list = df.loc[df['state'] == state, 'city'].dropna().unique()
city = st.sidebar.selectbox('City', city_list)

Start_date = st.sidebar.date_input('Start Date', min_value=min_d, max_value=max_d, value=min_d)
End_date   = st.sidebar.date_input('End Date',   min_value=min_d, max_value=max_d, value=max_d)

top_n = st.sidebar.slider('Top N', min_value=1, max_value=int(df['Product'].nunique()), value=5)

# --- فلترة صحيحة بالتاريخ ---
mask = (
    (df['state'] == state) &
    (df['city'] == city) &
    (df['Order Date'].dt.date >= Start_date) &
    (df['Order Date'].dt.date <= End_date)
)
df_2 = df.loc[mask].copy()
st.dataframe(df_2)

# --- أشهر المنتجات ---
prod_count = df_2['Product'].value_counts().reset_index().head(top_n)
prod_count.columns = ['Product', 'count']  # إعادة تسمية للعمود
st.plotly_chart(px.bar(prod_count, x='Product', y='count',
                       title=f'The most popular {top_n}'),
                use_container_width=True)
