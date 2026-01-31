import pandas as pd
import streamlit as st

df = pd.read_csv("data(修正版).csv")

st.dataframe(df)
