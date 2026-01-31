import os
import streamlit as st
import pandas as pd

st.title("CSV確認")

file_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(file_path)

st.dataframe(df)