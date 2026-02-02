import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# =========================
# ページ設定
# =========================
st.set_page_config(
    page_title="図書館統計ダッシュボード",
    layout="wide"
)

st.title("📚 日本の図書館統計データ可視化アプリ")

# =========================
# CSV 読み込み
# =========================
BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / "data.csv")

# =========================
# 前処理
# =========================
for col in df.columns:
    df[col] = df[col].astype(str).str.replace(",", "", regex=False)

numeric_cols = df.columns[3:]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# =========================
# サイドバー
# =========================
with st.sidebar:
    st.header("🔧 表示条件")

    building_type = st.selectbox(
        "本館・分館の区分",
        ["計", "本館", "分館"]
    )

    target_col = st.selectbox(
        "自治体区分",
        ["都道府県", "市（区）", "町", "村"]
    )

# =========================
# データ抽出
# =========================
filtered_df = df[df["本館・分館別"] == building_type]

# =========================
# タブ
# =========================
tab1, tab2, tab3 = st.tabs(["📊 概要", "📈 可視化", "📝 考察"])

# =========================
# 概要
# =========================
with tab1:
    st.dataframe(filtered_df)

# =========================
# 可視化
# =========================
with tab2:
    if filtered_df.empty:
        st.warning("該当データがありません")
    else:
        st.subheader(f"{building_type} × 自治体別")

        # --- 棒グラフ ---
        bar_data = filtered_df.iloc[0][["計", target_col]]
        st.bar_chart(bar_data)

        # --- 折れ線 ---
        st.line_chart(filtered_df[target_col])

        # --- 円グラフ（追加） ---
        st.subheader("自治体別 構成比")

        pie_data = filtered_df.iloc[0][["都道府県", "市（区）", "町", "村"]]

        fig, ax = plt.subplots()
        ax.pie(
            pie_data,
            labels=pie_data.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.axis("equal")

        st.pyplot(fig)

# =========================
# 考察
# =========================
with tab3:
    st.write(f"""
    円グラフより、{building_type}においては
    市（区）に設置されている図書館の割合が最も高いことが分かる。
    """)

st.caption("データ出典：e-Stat（政府統計）")
