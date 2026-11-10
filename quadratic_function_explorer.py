# 二次関数の（一般形）のグラフ
# quadratic_function_explorer.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# 画面設定
# --------------------------------
st.set_page_config(
    page_title="二次関数（一般形）のグラフ",
    layout="wide"
)

st.title("二次関数（一般形）のグラフ")

st.markdown(r"""
## 使い方

スライダーを動かして

\[
y=ax^2+bx+c
\]

のグラフがどのように変化するか調べましょう。

### 注目するポイント

- \(a\)：グラフの開き方
- \(b\)：頂点の左右移動
- \(c\)：上下移動
- 頂点座標
- 対称軸
""")

# --------------------------------
# スライダー
# --------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    a = st.slider(
        "a",
        min_value=-5.0,
        max_value=5.0,
        value=1.0,
        step=0.1
    )

with col2:
    b = st.slider(
        "b",
        min_value=-10.0,
        max_value=10.0,
        value=0.0,
        step=0.1
    )

with col3:
    c = st.slider(
        "c",
        min_value=-10.0,
        max_value=10.0,
        value=0.0,
        step=0.1
    )

# --------------------------------
# 関数
# --------------------------------
x = np.linspace(-10, 10, 1000)
y = a*x**2 + b*x + c

# --------------------------------
# 頂点計算
# --------------------------------
if abs(a) > 1e-8:
    xv = -b/(2*a)
    yv = a*xv**2 + b*xv + c
else:
    xv = None
    yv = None

# --------------------------------
# タイトル用の式
# --------------------------------
formula = rf"$y={a:.1f}x^2"

if b >= 0:
    formula += rf"+{b:.1f}x"
else:
    formula += rf"{b:.1f}x"

if c >= 0:
    formula += rf"+{c:.1f}$"
else:
    formula += rf"{c:.1f}$"

# --------------------------------
# グラフ
# --------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    x,
    y,
    linewidth=3,
    color="blue",
    label=formula
)

# 軸
ax.axhline(0, color="black")
ax.axvline(0, color="black")

# 頂点
if xv is not None:

    ax.scatter(
        xv,
        yv,
        color="red",
        s=80,
        zorder=5
    )

    ax.axvline(
        xv,
        color="green",
        linestyle="--",
        label="Axis of Symmetry"
    )

# グリッド
ax.grid(True)

# タイトル
ax.set_title(
    formula,
    fontsize=18
)

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend(fontsize=10)

st.pyplot(fig)

# --------------------------------
# 現在の式
# --------------------------------
st.markdown("## 現在の式")

st.latex(
    f"y={a:.1f}x^2"
    + (f"+{b:.1f}x" if b >= 0 else f"{b:.1f}x")
    + (f"+{c:.1f}" if c >= 0 else f"{c:.1f}")
)

# --------------------------------
# 頂点情報
# --------------------------------
st.markdown("## 頂点と対称軸")

if xv is not None:

    st.success(
        f"頂点：({xv:.2f}, {yv:.2f})"
    )

    st.info(
        f"対称軸：x = {xv:.2f}"
    )

else:

    st.warning(
        "a=0 のため二次関数ではありません。"
    )

# --------------------------------
# 学習用解説
# --------------------------------
st.markdown("## グラフの特徴")

if a > 0:
    st.write("✅ 上に開く放物線")

elif a < 0:
    st.write("✅ 下に開く放物線")

if abs(a) > 1:
    st.write("✅ 標準形 y=x² より細い")

elif 0 < abs(a) < 1:
    st.write("✅ 標準形 y=x² より広い")

elif abs(a) == 1:
    st.write("✅ 標準形 y=x² と同じ開き方")

st.write(f"✅ b = {b:.1f}")
st.write(f"✅ c = {c:.1f}")
