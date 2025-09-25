import pandas as pd 
import streamlit as st
import plotly.express as px 
# st.title('Google play exploratory Data Analysis')
st.markdown(
    "<h1 style='text-align: center; color: white;'>Google play exploratory Data Analysis</h1>", 
    unsafe_allow_html=True
)

st.image('D:/New folder (31)/Google_Play_Store_badge_EN.svg.webp')
df=pd.read_csv('D:/New folder (31)/cleaned_df.csv',index_col=0)
st.set_page_config(page_title='Google Play EDA',layout='wide')
page=st.sidebar.radio('pages',['Introduction','Analysis Questions','Reporting'])
if page=='Introduction':
    st.dataframe(df.head())
    st.header('Data Description')
    st.write("""
 Category: Category the app belongs to


    Rating: Overall user rating of the app (as when scraped)


    Reviews:Number of user reviews for the app (as when scraped)

    Size: Size of the app (as when scraped)


    Installs: Number of user downloads/installs for the app (as when scraped)


    Type: Paid or Free

    Price: Price of the app (as when scraped)


    Content Rating: Age group the app is targeted at - Children / Mature 21+ / Adult


    Genres: An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.
""")
elif page=='Analysis Questions':
    st.header('what is the most expensive App ')
    st.write(df.sort_values(by='Price',ascending=False)[['App','Price']].head(1))
    st.header('How many apps that has more than 50K reviews.')
    if st.button('Check Answer'):
            st.write(df[df['Reviews']>50000]['App'].nunique())
            
            
    st.header('what is the average Revirews per content Rating per type ?')
    content_type_review=df.groupby(['Content Rating','Type'])['Reviews'].mean().reset_index()
    st.plotly_chart(px.bar(content_type_review,x='Content Rating',y='Reviews',
            labels={'Reviews':'Avg_numbers_of_reveiws'},text_auto=True,color='Type',barmode='group'))
elif page=='Reporting':
     year=st.sidebar.selectbox('Year',df.Last_updated_year.unique())
     df_2=df[df['Last_updated_year']==year]
     st.dataframe(df_2)