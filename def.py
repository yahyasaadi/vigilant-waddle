import streamlit as st
import pandas as pd
# import openpyxl
# import numpy as np
from streamlit.components.v1 import html
import pyrebase
import time


st.set_page_config(page_title='Election Analysis',page_icon="chart_with_upwards_trend",)

st.write("<h2 style='margin-top:-20px;'>Garissa Township MP - 2023 By-Election.</h2>",unsafe_allow_html=True)
col1, col2 = st.columns(2)
dfward = pd.read_excel("Book1.xlsx",sheet_name='Sheet2')
dfpoling=pd.read_excel("Book1.xlsx",sheet_name='df')

with st.form("my_form"):


	ward_select = col1.selectbox('Choose your ward',dfward)

	dfpolingFl = dfpoling[dfpoling['WARDS'].str.match(ward_select)]

	poling_select = col2.selectbox('Choose your poling station',dfpolingFl['POLING_STATION'])

	col3, col4,col5,col6,col7 = st.columns(5)

	regNo = col3.number_input("Registered Voters",min_value=0)
	rejVotes = col4.number_input("Rejected Voters",min_value=0)
	desValues = col5.number_input("Desputed Votes",min_value=0)
	valid = col6.number_input("Valid Votes Casted",min_value=0)
	###waiting for confirmation
	rejOb = col7.number_input("Rejection Objected",min_value=0)
	st.markdown(" ")
	st.markdown(" ")



	st.subheader("Data for Candidates.")
	col8, col9, col10 = st.columns(3)

	hon_osman = col8.number_input("Hon. Abdikarim Rati", min_value=0)
	hon_dekow = col9.number_input("Hon. Dekow Barrow", min_value=0)
	hon_jofle = col10.number_input("Hon. Nassir Dolal", min_value=0)
	hon_malow = col8.number_input("Hon. Ibrahim Malow", min_value=0)
	hon_muhiadin = col9.number_input("Hon. Muhiadin Abdirashid", min_value=0)
	hon_feisal = col10.number_input("Hon. Abdifeisal Amin", min_value=0)
	st.markdown('')
	st.markdown('')

	submitted = st.form_submit_button("Submit")
	if submitted:
		dfup = pd.read_excel("Book3.xlsx",sheet_name='general')
		regNo >= (rejVotes + desValues+ valid +rejOb )
		valid == (hon_osman+hon_dekow+hon_jofle+hon_malow+hon_feisal+hon_muhiadin)
		infoo = [ward_select,poling_select, regNo, rejVotes, desValues, valid , rejOb, hon_osman, hon_dekow, hon_jofle]

		# path = 'Book3.xlsx'
		columns = ['ward','poling','Registered','Rejected','Desputed','Valid','Rejection', 'hon_osman', 'hon_dekow', 'hon_jofle']
		df = pd.DataFrame([infoo],columns=columns)
		df2 = pd.read_excel("dday.xlsx",sheet_name='general')

		
		frames = [df, df2]
		result = pd.concat(frames)
		
		myerror ="""
		
			alert('Error Occured!');
		
		"""
		my_html = f"<script>{myerror}</script>"
		##saving logics
		if (regNo >= (rejVotes + desValues+ valid +rejOb )) & (valid == (hon_osman+hon_dekow+hon_jofle+hon_malow+hon_feisal+hon_feisal)):
			# writer = pd.ExcelWriter("dday.xlsx", engine='xlsxwriter')
			# result.to_excel(writer,sheet_name = 'general', index=False)
			# writer.save()
			# writer.close()
			firebaseConfig = {
				"apiKey": "AIzaSyCqNrGX_lYodiORKQrtRIr5CUZtudl-hTU",
                "authDomain": "aor-election.firebaseapp.com",
                'databaseURL': "https://aor-election-default-rtdb.firebaseio.com",
                "projectId": "aor-election",
                'storageBucket': "aor-election.appspot.com",
                "messagingSenderId": "173943917022",
                "appId": "1:173943917022:web:be60dff753ea723038b54f",
                "measurementId": "G-XRSDKRXW2G",
                "serviceAccount":'aor-election-firebase-adminsdk-4js4d-6fe3fcd536.json'
            }
			firebase = pyrebase.initialize_app(firebaseConfig)
			db = firebase.database()
			data = {
			'time':time.ctime(),
			'ward': ward_select,
			'pollingStation': (poling_select),
			'registerdVoters': regNo,
			'rejected': rejVotes,
			'rejectedObj': rejOb,
			'disputed': desValues,
			'valid': valid, 
			'jofle': hon_jofle,
			'dekow': hon_dekow, 
			'osman': hon_osman,
			'malow': hon_malow,
			'feisal': hon_feisal,
			'muhiadin': hon_muhiadin
			}
			result = db.child('Official').child(poling_select).set(data)

		else:
			html(my_html) 

			refresh = """
				if ( window.history.replaceState ) {
	        		window.history.replaceState( null, null, window.location.href );
	    		}
			"""
			my_html1 = f"<script>{refresh}</script>"
			html(my_html1)

footer="""
 <style>
 @import url('https://fonts.googleapis.com/css2?family=Cormorant+SC:wght@700&display=swap');
 .css-12ttj6m{
 border:none;
 }
 
 .css-10trblm{
 text-align:center;
 font-family: 'Cormorant SC', serif;
 margin-bottom:34px;
 margin-top:-35px;

 }
 </style>
 """
st.markdown(footer,unsafe_allow_html=True) 

footer="""<style>
body{
	background-color:#FD8A8A;
}
a:link , a:visited{
color: blue;
background-color: #243763;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #243763;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;color:white;' href="http://networkia-tech.ga/" target="_blank">Networkia IT Solutions</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)