import streamlit as st
import pandas as pd

st.title("蔵書冊数別 図書館数の可視化")

# ① 先にCSVを読む
df = pd.read_csv(
    "FEH_00400004_260126233600.csv",
    encoding="utf-8-sig",
    engine="python",
    on_bad_lines="skip"
)


# ② dfができてから列名を確認
st.write("列名一覧:", df.columns)

# ③ 年度を作る
df["年度"] = df["時間軸（年度次）コード"].astype(str).str[:4].astype(int)

# ④ UI
year = st.selectbox("年度を選択", sorted(df["年度"].unique()))
pref = st.selectbox("都道府県を選択", df["地域"].unique())

# ⑤ 絞り込み
filtered = df[(df["年度"] == year) & (df["地域"] == pref)]

st.write("絞り込み件数:", len(filtered))

# ⑥ 数値化（重要）
filtered["値"] = pd.to_numeric(filtered["値"], errors="coerce")

# ⑦ グラフ
st.bar_chart(
    filtered.set_index("蔵書冊数区分")["値"]
)
