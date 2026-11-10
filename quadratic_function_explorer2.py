# 二次関数（一般形）のグラフ
# quadratic_function_explorer2.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 画面設定
# ----------------------------
st.set_page_config(
    page_title="二次関数グラフ探究",
    layout="wide"
)

st.title("二次関数グラフ探究アプリ")

st.markdown(r"""
## 使い方

スライダーを動かして

\[
y=ax^2+bx+c
\]

のグラフの変化を調べましょう。

### 注目するポイント

- \(a\)：開き方
- \(b\)：左右の移動に影響
- \(c\)：上下の移動
- 頂点座標
- 対称軸
""")

# ----------------------------
# パラメータ設定
# ----------------------------

col1, col2 = st.columns(2)

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

c = st.slider(
    "c",
    min_value=-10.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)

# ----------------------------
# 表示範囲
# ----------------------------

st.markdown("### グラフ表示範囲")

col3, col4 = st.columns(2)

with col3:
    x_range = st.slider(
        "x軸表示範囲",
        min_value=5,
        max_value=50,
        value=10
    )

with col4:
    y_range = st.slider(
        "y軸表示範囲",
        min_value=10,
        max_value=200,
        value=50
    )

st.info(
    f"表示範囲：  −{x_range} ≤ x ≤ {x_range}， −{y_range} ≤ y ≤ {y_range}"
)

# ----------------------------
# 関数
# ----------------------------

x = np.linspace(
    -x_range,
    x_range,
    1000
)

y = a * x**2 + b * x + c

# ----------------------------
# 頂点
# ----------------------------

if abs(a) > 1e-10:

    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c

else:

    xv = None
    yv = None

# ----------------------------
# タイトル用数式
# ----------------------------

formula = f"y={a:.1f}x²"

if b >= 0:
    formula += f"+{b:.1f}x"
else:
    formula += f"{b:.1f}x"

if c >= 0:
    formula += f"+{c:.1f}"
else:
    formula += f"{c:.1f}"

# ----------------------------
# グラフ描画
# ----------------------------

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    x,
    y,
    linewidth=3,
    color="blue",
    label=formula
)

# x軸・y軸

ax.axhline(
    0,
    color="black",
    linewidth=1
)

ax.axvline(
    0,
    color="black",
    linewidth=1
)

# 頂点表示

if xv is not None:

    ax.scatter(
        xv,
        yv,
        color="red",
        s=80,
        zorder=5,
        label="Vertex"
    )

    ax.axvline(
        xv,
        color="green",
        linestyle="--",
        linewidth=2,
        label="Axis of Symmetry"
    )

# グラフ範囲

ax.set_xlim(-x_range, x_range)
ax.set_ylim(-y_range, y_range)

# タイトル

ax.set_title(
    formula,
    fontsize=18
)

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.grid(True)

ax.legend()

st.pyplot(fig)

# ----------------------------
# 現在の式
# ----------------------------

st.markdown("## 現在の式")

latex_formula = (
    f"y={a:.1f}x^2"
    + (f"+{b:.1f}x" if b >= 0 else f"{b:.1f}x")
    + (f"+{c:.1f}" if c >= 0 else f"{c:.1f}")
)

st.latex(latex_formula)

# ----------------------------
# 頂点・対称軸
# ----------------------------

st.markdown("## 頂点と対称軸")

if xv is not None:

    st.success(
        f"頂点 = ({xv:.2f}, {yv:.2f})"
    )

    st.info(
        f"対称軸 : x = {xv:.2f}"
    )

else:

    st.warning(
        "a = 0 のため二次関数ではありません。"
    )

# ----------------------------
# グラフの特徴
# ----------------------------

st.markdown("## グラフの特徴")

if a > 0:
    st.write("✅ 上に開く")

elif a < 0:
    st.write("✅ 下に開く")

if abs(a) > 1:
    st.write("✅ y=x² より細い")

elif 0 < abs(a) < 1:
    st.write("✅ y=x² より広い")

elif abs(a) == 1:
    st.write("✅ y=x² と同じ開き方")

st.write(f"✅ a = {a:.1f}")
st.write(f"✅ b = {b:.1f}")
st.write(f"✅ c = {c:.1f}")

# ----------------------------
# 補足
# ----------------------------

st.markdown(r"""
### 考察してみよう

- a を大きくするとどうなるか？
- a が負になるとどうなるか？
- b を変えると頂点はどのように動くか？
- c を変えるとグラフ全体はどう動くか？

自分の予想を立ててからスライダーを動かして確認してみましょう。
""")
