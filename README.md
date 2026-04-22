# 📊 Financial & Stock Insight Tool
# 1. Problem & User
This project is designed for accounting students who want a simple way to observe company performance using market data.  
While accounting focuses on financial statements, stock price trends also reflect how the market evaluates a company.
# 2. Data
The data is retrieved using the yfinance API (Yahoo Finance).  
Access date: April 2026.  
Key variable used: daily closing price.
# 3. Methods
- Retrieve stock data using Python (yfinance)
- Clean and organise time-series data
- Visualise stock price trends using Plotly
- Calculate basic indicators (average price, volatility, current price)
# 4. Key Findings
- Stock prices show different levels of volatility over time  
- The current price relative to average price can indicate recent performance  
- Visual trends help users quickly understand market behaviour  
# 5. How to Run
1. Install required packages:
   pip install streamlit yfinance plotly pandas

2. Run the app:
   python -m streamlit run app.py
# 6. Product Link / Demo
GitHub Repository:   https://financial-stock-insight-tool-xjtlu-acc102-project.streamlit.app/
This project runs locally using Streamlit.  
The app can be launched using the command above.
# 7. Project Structure
- ACC102 individual test.py: main interactive tool  
- notebook.ipynb: data exploration and testing  
- README.md: project documentation  
# 8. Limitations & Future Improvements
- Only basic indicators are included  
- No integration with financial statements yet  
- Future improvements could include financial ratios or multi-company comparison  
# 9. Notes
This tool provides simplified analysis for learning purposes and does not represent professional financial advice.
