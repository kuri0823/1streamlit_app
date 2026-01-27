import streamlit as st
import pandas as pd
import numpy as np

st.title("streamlitの基本")

st.write('streamlitの基本の性能を試します')

df=pd.DataFrame(data=np.random.randint(0,100,(3,6)),
             index=['支店A','支店B','支店C'])
colums=['1月','2月','3月','4月','5月','6月',]

st.header('1,DataFrameの表示')
st.dataframe(df)