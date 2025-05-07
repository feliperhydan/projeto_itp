import streamlit as st
import pandas as pd
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPEN_AI_API_KEY")
print(openai.api_key)

#Carregando spreadsheet
xls = pd.ExcelFile("Green West Dataset.xlsx")
sheet_names = xls.sheet_names
print(sheet_names)
#sheet = st.selectbox("Choose a sheet", sheet_names)
#df = xls.parse(sheet)   

#Display Dataframe
#st.subheader("Preview of the Data")
#st.dataframe(df.head())

