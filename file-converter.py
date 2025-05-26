import streamlit as st
import pandas as pd
from io import BytesIO
st.set_page_config(page_title="file-converter" ,layout="wide")
st.title("File Converter & cleaner")
st.write("upload csv or excel files, clean data, and convert formats.")
files = st.file_uploader("upload csv or excel files.", type=["csv","xlsx"])
if files:
    for file in files:
        ext=file.name.split(".")[-1]
        df=pd.read_csv(file) if ext=="csv" else pd.read_excel(file)
        st.subheader(f"{file.name} - preview")
        st.dataframe(df.head())