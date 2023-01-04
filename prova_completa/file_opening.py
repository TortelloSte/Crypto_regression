import numpy as np
import pandas as pd
import datetime as dt
import plotly.graph_objects as go

def datas(filepath):
    df = pd.read_csv(filepath)
    df.drop(columns=["Name", "SNo", "Symbol", "Marketcap", "Volume"], axis = 1, inplace =  True)
    df["Date"] = pd.to_datetime(df["Date"])
    df['Date_year'] = df["Date"].dt.year
    df['Date_month'] = df["Date"].dt.month
    df['Date_day'] = df["Date"].dt.day
    df.to_csv('./archive/bitcoin_update.csv')
    df1 = pd.read_csv("./archive/bitcoin_update.csv")
    df1.drop(columns=["Date"], axis = 1, inplace=True)
    df1.dropna(inplace= True)
    fig = go.Figure(data = [go.Candlestick(x = df['Date'],
            close = df1['Close'])])
    fig.show()
    return df1
