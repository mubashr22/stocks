# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:34:48 2023

@author: Mudassir
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
df = pd.read_csv("stock_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Title of the web app
st.title('Stock Analysis and Visualization')

# Sidebar for selecting options
st.sidebar.title('Options')
stocks = df.columns.tolist()
selected_stocks = st.sidebar.multiselect('Select Stocks', stocks, default=stocks)

# Line plot section
st.sidebar.subheader('Closing Prices over Time')
line_chart_option = st.sidebar.checkbox('Show Line Chart', value=True)
if line_chart_option:
    plt.figure(figsize=(12, 6))
    for column in selected_stocks:
        plt.plot(df.index, df[column], label=column)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Closing Prices over Time')
    plt.legend()
    st.pyplot()

# Daily Change section
st.sidebar.subheader('Daily Change')
daily_change_df = df[selected_stocks].diff().dropna()
st.sidebar.dataframe(daily_change_df)

# Line plot for daily change
st.sidebar.subheader('Daily Change - Line Plot')
line_plot_option = st.sidebar.checkbox('Show Line Plot', value=True)
if line_plot_option:
    plt.figure(figsize=(12, 6))
    for column in daily_change_df.columns:
        plt.plot(daily_change_df.index, daily_change_df[column], label=column)
    plt.xlabel('Date')
    plt.ylabel('Daily Change')
    plt.title('Daily Change over Time')
    plt.legend()
    st.pyplot()

# Bar plot for daily change
st.sidebar.subheader('Daily Change - Bar Plot')
bar_plot_option = st.sidebar.checkbox('Show Bar Plot', value=True)
if bar_plot_option:
    plt.figure(figsize=(12, 6))
    daily_change_df.plot(kind='bar', figsize=(12, 6))
    plt.xlabel('Date')
    plt.ylabel('Daily Change')
    plt.title('Daily Change - Bar Plot')
    plt.legend()
    st.pyplot()

# Comparison charts for each stock
for stock in selected_stocks:
    st.sidebar.subheader(f'{stock} - Comparison Chart')
    comparison_chart_option = st.sidebar.checkbox(f'Show {stock} Comparison Chart', value=True)
    if comparison_chart_option:
        plt.figure(figsize=(12, 6))
        for column in selected_stocks:
            plt.plot(df.index, df[column], label=column)
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title(f'{stock} - Comparison Chart')
        plt.legend()
        st.pyplot()
