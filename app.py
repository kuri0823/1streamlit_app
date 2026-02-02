import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ページ設定
st.set_page_config(page_title="図書館統計アプリ")

st.title("図書館統計データの可視化")
st.write("e-Stat の図書館統計データを使って作成したアプリです。")

# CSV読み込み
df = pd.read_csv("data.csv")

# 数値データの処理
for col in df.columns[3:]:
    df[col] = df[col].astype(str).str.replace(",", "")
    df[col] = pd.to_numeric(df[col], errors="coerce")

# サイドバー
st.sidebar.header("表示条件")

kind = st.sidebar.selectbox(
    "本館・分館の区分",
    ["計", "本館", "分館"]
)

area = st.sidebar.selectbox(
    "自治体区分",
    ["都道府県", "市（区）", "町", "村"]
)

# データ抽出
data = df[df["本館・分館別"] == kind]

# タブ
tab1, tab2 = st.tabs(["データ", "グラフ"])

# データ表示
with tab1:
    st.dataframe(data)

# グラフ表示
with tab2:
    if len(data) == 0:
        st.write("データがありません。")
    else:
        st.subheader("棒グラフ")
        st.bar_chart(data.iloc[0][["計", area]])

        st.subheader("折れ線グラフ")
        st.line_chart(data[area])

        st.subheader("円グラフ")
        values = data.iloc[0][["都道府県", "市（区）", "町", "村"]]

        fig, ax = plt.subplots()
        ax.pie(
        values,
        labels=values.index,
        autopct="%1.1f%%"
        )
ax.axis("equal")   # 円を正円にする
st.pyplot(fig)


st.caption("出典：e-Stat（政府統計）")


import os
st.write(os.listdir("."))
