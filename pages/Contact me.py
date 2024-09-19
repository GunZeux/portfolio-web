import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form("send message"):
    user_mail = st.text_input("Email")
    raw_text = st.text_area("Enter your Message")
    send = st.form_submit_button("Submit")

    if send:
        message = f"""Subject: new message from {user_mail} at web portfolio
        
user email : {user_mail}
message : {raw_text}"""
        send_email(message)
        st.info("email sent successfully".title())