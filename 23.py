import streamlit as sg
import pandas


col1,col2=sg.columns(2)
with col1:
    sg.image(".jpg")

with col2:
    sg.title("niranjan ")
    content="""my name is NIRANJAN C iam completed BE in MECHANICAL Engineering 2024 but iam interested software engineering ima learn PYTHON language"
             """
    sg.write(content)

sg.write("hello everyone this my web app")

col3,col,col4=sg.columns([1.5,0.5,1.5])

df=pandas.read_csv("data .csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        sg.header(row["title"])
        sg.write(row["description"])
        sg.image("images/"+row["image"])
        sg.write(f"[source code]{row["url"]}")

with col4:
    for index,row in df[10:].iterrows():
        sg.header(row["title"])
        sg.write(row["description"])
        sg.image("images/"+row["image"])
        sg.write(f"source code({row["url"]})")

