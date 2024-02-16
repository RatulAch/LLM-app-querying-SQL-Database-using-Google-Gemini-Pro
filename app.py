from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function to load Load google gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

#function to retrive query from SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


#define ur prompt
prompt = [
    """
You are an expert in converting English questions to SQL query.
The SQL database has the name STUDENT and has the floowing columns- NAME, CLASS, SECTION and MARKS \n
\n for example, \n Example 1 - How many entries of records are present in the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
\n EXAMPLE 2 - TELL me all the students studying in data science class?, the SQL command will be something like SELECT * FROM STUDENT where CLASS="Data Science";
also sql code should not have ''' in beginning or end and sql word in output
"""
]


#streamlit app
st.set_page_config(page_title = "I can retrieve any SQL query")
st.header("Gemini app to query SQL data")

question = st.text_input("Input:", key = "input")

submit = st.button("Ask the question")

#if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("the response is")
    for row in data:
        print(row)
        st.header(row)

