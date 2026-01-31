import streamlit as st
import pandas as pd
from pathlib import Path

# =========================
# ページ設定
# =========================
st.set_page_config(
    page_title="Library Statistics App",
    layout="wide"
)

st.title("📚 図書館統計データの可視化")

# =========================
# CSV 読み込み（Cloud対応）
# =========================
BASE_DIR = Path(__file__).parent
csv_path = BASE_DIR / "data.csv"

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error("❌ data.csv が見つかりません。GitHubにアップされているか確認してください。")
    st.stop()

# =========================
# データ確認
# =========================
st.subheader("データの先頭")
st.dataframe(df.head())

# =========================
# 数値列の前処理
# =========================
# カンマ付き数値を数値型に変換
for col in df.columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

numeric_cols = df.columns[3:]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# =========================
# グラフ表示
# =========================
st.subheader("設置者別 図書館数")

chart_data = df.iloc[0, 3:]

st.bar_chart(chart_data)

# =========================
# 補足
# =========================
st.caption("※ データ出典：日本の図書館統計（CSV加工）")
