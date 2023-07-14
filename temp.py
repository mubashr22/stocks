# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('E:\Downloads\stocks.csv')  # Replace 'your_dataset.csv' with the actual filename/path of your dataset

# Set the 'Date' column as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Create a Streamlit app to display the results
st.title('Stock Price Analysis')
st.subheader('Closing Prices over Time')

# Select the companies to plot
companies = ['AAPL', 'BA', 'T', 'MGM', 'AMZN']

# Line chart for each selected company
for company in companies:
    st.line_chart(df[company])

# Table showing the data
st.subheader('Stock Price Data')
st.dataframe(df)

# Additional analysis and visualizations
st.subheader('Additional Analysis and Visualizations')

# 1. Daily Returns
returns = df.pct_change()
st.subheader('Daily Returns')
st.line_chart(returns[companies])

# 2. Moving Averages
window_sizes = [50, 200]
for company in companies:
    for window in window_sizes:
        rolling_mean = df[company].rolling(window).mean()
        st.line_chart(rolling_mean)

# 3. Volatility Analysis
volatility = df[companies].std()
st.subheader('Volatility Analysis')
st.bar_chart(volatility)

# 4. Candlestick Charts
st.subheader('Candlestick Charts')
fig, ax = plt.subplots()
ax.xaxis_date()
ax.set_title('Candlestick Chart - AAPL')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.plot(df.index, df['AAPL'], 'k-', color='blue')
ax.xaxis.set_major_locator(plt.MaxNLocator(6))
ax.grid(True)
st.pyplot(fig)

# 5. Rolling Window Analysis
window_size = st.slider('Select Window Size', 5, 100, 20)
rolling_mean = df[companies].rolling(window=window_size).mean()
st.subheader('Rolling Window Analysis')
st.line_chart(rolling_mean)


# 7. Stock Performance Comparison
normalized_prices = df[companies] / df[companies].iloc[0]
st.subheader('Stock Performance Comparison')
st.line_chart(normalized_prices)

# 8. Trading Strategies
# Add your trading strategy implementation and results display here

# 9. Risk-Return Analysis
st.subheader('Risk-Return Analysis')
st.scatter_plot(volatility, returns[companies])
