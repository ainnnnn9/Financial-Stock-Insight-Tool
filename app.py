import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("📊 Financial & Stock Insight Tool")

st.write(
    "This tool helps accounting students observe company performance trends "
    "and basic risk indicators using stock market data."
)

# 输入股票代码
ticker = st.text_input("Enter Stock Ticker (e.g. AAPL, MSFT, TSLA)", "AAPL")

# 获取公司信息
stock = yf.Ticker(ticker)
company_name = ticker.upper()

company_name = info.get("longName", "Unknown Company")

st.subheader(f"🏢 {company_name}")

# 时间选择
period_option = st.selectbox(
    "Select Time Period",
    ["6 months", "1 year", "5 years", "Custom"]
)

# 获取数据
if period_option == "Custom":
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    if start_date and end_date:
        hist = stock.history(start=start_date, end=end_date)
    else:
        st.warning("Please select both start and end dates.")
        hist = None
else:
    if period_option == "6 months":
        period = "6mo"
    elif period_option == "1 year":
        period = "1y"
    else:
        period = "5y"

    hist = stock.history(period=period)

# 如果数据有效
if hist is not None and not hist.empty:

    # 当前价格
    current_price = hist['Close'][-1]

    st.metric("Current Price", f"{current_price:.2f}")

    # Plotly图表
    st.subheader("📈 Stock Price Trend")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['Close'],
        mode='lines',
        name='Close Price'
    ))

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis=dict(
            tickformat="%Y-%m",
            tickangle=45
        ),
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    # 指标
    avg_price = hist['Close'].mean()
    volatility = hist['Close'].std()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average Price", f"{avg_price:.2f}")

    with col2:
        st.metric("Volatility", f"{volatility:.2f}")

    # 简洁解释
    st.subheader("📊 Basic Interpretation")

    if volatility > 20:
        st.write("⚠️ The stock shows relatively high volatility.")
    else:
        st.write("✅ The stock appears relatively stable.")

    if current_price > avg_price:
        st.write("📈 Current price is above average level.")
    else:
        st.write("📉 Current price is below average level.")

    # 小免责声明
    st.caption("Note: This is a simplified interpretation for basic understanding.")

else:
    st.error("No data available. Please check the ticker or date selection.")
