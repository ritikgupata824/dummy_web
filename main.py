import  streamlit as st

# import pandas as pd

name = st.text_input("Enter your name")
fathername =st.text_input("Enter your father name")
adr = st.text_area("Enter your text : ")
classdata = st.selectbox("Enter your class:", [1, 2, 3, 4, 5, 6])

button = st.button("Done")
if button :
    st.markdown (f"""
name : {name}
father name :{fathername}
address : {adr}
class : {classdata}""")