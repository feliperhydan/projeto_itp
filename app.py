import streamlit as st
import pandas as pd
import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

# Load spreadsheet
xls = pd.ExcelFile("Green West Dataset.xlsx")
sheet_names = xls.sheet_names
sheet = st.selectbox("Choose a sheet", sheet_names)
df = xls.parse(sheet)

# Display dataframe
st.subheader("📊 Preview of the Data")
st.dataframe(df.head())

# Ask question
st.subheader("💬 Ask a question about this data")
user_question = st.text_area("Type your question:", height=100)

if st.button("Answer"):
    if user_question:
        prompt = f"""You are a data analyst. Use the following table to answer the user's question. 
Here is the data (as CSV):

{df.head(100).to_csv(index=False)}

Question: {user_question}
Answer in a concise and professional way:"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        answer = response['choices'][0]['message']['content']
        st.markdown(f"**🧠 Answer:** {answer}")
    else:
        st.warning("Please enter a question.")
