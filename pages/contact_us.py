import streamlit as sg
from sending_emali import send_email

sg.title(" contact customer care ")

sg.header("contact me")
with sg.form(key="your values"):
    email=sg.text_input("Your Email Address")
    message=sg.text_area("Your Message")
    messages=f"""
Subject=New Email from{email}
Form:{email}
{message}
    """

    button=sg.form_submit_button("submit")
    if button:
        send_email(messages)
        sg.info("your email was sent successfully")
