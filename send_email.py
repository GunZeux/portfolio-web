import os
import smtplib
import ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    try:
        password = os.getenv("PASSWORD")

    except Exception as ex:
        password = st.secrets["PASSWORD"]

    user_mail = "gunzeux71@gmail.com"
    reciever_mail = "gunzeux71+portfolio@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_mail, password)
        server.sendmail(user_mail, reciever_mail, message)
    print("completed")
