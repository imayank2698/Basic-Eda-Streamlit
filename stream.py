import streamlit as st
import pandas as pd
import plotly.express as px

gg=pd.read_csv('C:\\Users\\WolfHound\\Downloads\\wine-reviews\\winemag-data-130k-v2.csv',index_col=0)
newgg = gg.drop(columns=['region_2','taster_name','taster_twitter_handle'])
newgg = newgg.dropna()

def maxsphere(newgg,c1):
	#mean of price,points countrywise

	countrymean = newgg.groupby('country').mean().reset_index()
	sortbyoption=countrymean.sort_values(by=c1,ascending=False)
	figure=px.bar(sortbyoption,x='country',y='price')
	st.plotly_chart(figure)


def maxsphere1(newgg,c2):
	
	#countrywise
	ggs=newgg.loc[newgg['country']==c2]
	pg=ggs['province'].value_counts().reset_index()	
	figure=px.pie(pg,names='index',values='province')
	st.plotly_chart(figure)


def maxsphere2(newgg,c3,c4,c5):

	x1=newgg.loc[newgg['country']==c3]
	x2=x1.loc[x1['province']==c4]
	x3=x2.groupby('region_1').mean().reset_index().sort_values(by=c5,ascending=False)
	figure=px.line(x3,x='region_1',y=c5)
	st.plotly_chart(figure)	



st.title('EDA Analysis of Wine Reviews')


st.header('Mean price/points countrywise')

c1=st.selectbox("Choose",["price","points"])
button1=st.button("Done")

if button1 is True:
	maxsphere(newgg,c1)



st.header('Analysis countrywise/No. of winery')
c2=st.selectbox("Chooses",newgg['country'].unique())
button2=st.button("Dones")

if button2 is True:
	maxsphere1(newgg,c2)

st.header('Analysis regionwise')
c3=st.selectbox("Unique country",newgg['country'].unique())
c4=st.selectbox("Unique province",newgg.loc[newgg['country']==c3].province.unique())
c5=st.selectbox("analysis",["price","points"])
button3=st.button("Doness")

if button3 is True:
	maxsphere2(newgg,c3,c4,c5)




