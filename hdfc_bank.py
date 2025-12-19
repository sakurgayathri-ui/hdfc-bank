import streamlit as st
import pandas as pd
from supabase import create_client
SUPABASE_URL = "https://tzowlzjkbemspbxhpwmf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR6b3dsemprYmVtc3BieGhwd21mIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYxMTM4MzMsImV4cCI6MjA4MTY4OTgzM30.wpO0z0uUguDIRA2vI-D7QFR1rzkU8N-lZMPLArPgxoM"

supabase = create_client(SUPABASE_URL , SUPABASE_KEY)
st.title("HDFC BANK (supabase)")

menu=["REGISTER","VIEW"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "REGISTER":
   name=st.text_input("enter name")
   age=st.number_input("AGE",min_value=18)
   account=int(st.number_input("ACCOUNT NUMBER"))
   bal=st.number_input("BALANCE",min_value=500)
   if st.button("SAVE"):
         supabase.table("users").insert({
             "name":name,
             "age":age,
             "account":account,
             "balance":bal}).execute()
         st.sucess("user added successfully")
if choice =="VIEW":
         st.subheader("view users")
         data=supabase.table("users").select("*").execute()
         df=pd.DataFrame(data.data)
         st.dataframe(df)
