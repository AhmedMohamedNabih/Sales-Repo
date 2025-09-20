
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

# df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
# df_2 = df[
#     (df['state'] == state) &
#     (df['city'] == city) &
#     (df['Order Date'].dt.date >= Start_date) &
#     (df['Order Date'].dt.date <= End_date)
# ]
# st.dataframe(df_2)
# prod_count=df_2['Product'].value_counts().reset_index().head(top_n)
# st.plotly_chart(px.bar(prod_count,x='Product',y='count',title=f'the nmost popular {top_n}'))

import pandas as pd 
import streamlit as st
import plotly.express as px 
import numpy as np

st.set_page_config(layout='wide', page_title='Sales EDA', initial_sidebar_state='expanded')

# اقرأ الملف
df = pd.read_csv('cleaning_df.csv', index_col=0)

# حوّل التاريخ قبل أي date_input
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# قيم حدود التاريخ من العمود نفسه
min_d = df['Order Date'].min().date()
max_d = df['Order Date'].max().date()

# SIDEBAR
state = st.sidebar.selectbox('State', df['state'].dropna().unique())
# فلترة قائمة المدن حسب الولاية (أدق)
city_list = df.loc[df['state'] == state, 'city'].dropna().unique()
city = st.sidebar.selectbox('City', city_list)

Start_date = st.sidebar.date_input('Start Date', min_value=min_d, max_value=max_d, value=min_d)
End_date   = st.sidebar.date_input('End Date',   min_value=min_d, max_value=max_d, value=max_d)

top_n = st.sidebar.slider('Top N', min_value=1, max_value=int(df['Product'].nunique()), value=5)

# فلترة البيانات
df_2 = df[
    (df['state'] == state) &
    (df['city'] == city) &
    (df['Order Date'].dt.date >= Start_date) &
    (df['Order Date'].dt.date <= End_date)
]

st.dataframe(df_2)

# أشهر المنتجات
prod_count = df_2['Product'].value_counts().reset_index().head(top_n)
prod_count.columns = ['Product', 'count']

st.plotly_chart(px.bar(prod_count, x='Product', y='count', title=f'The most popular {top_n}'),
                use_container_width=True)
