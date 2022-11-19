import streamlit as st
import yfinance as yahooFinance
import plotly.graph_objs as go

# Selectores
with st.sidebar:
    cia = st.text_input(label = "Introduce compañía", value = 'AAPL')
    interval = st.selectbox(label = "Intervalo a coger de la BD", options = ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'])
    period = st.selectbox(label = "Periodo", options = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'])

# Datos
tickets = yahooFinance.Ticker(cia)
stocks = tickets.history(period = period, interval = interval)

if len(stocks) > 0:

    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=stocks.index, open = stocks.Open, high=stocks.High, low=stocks.Low, close=stocks.Close, name = 'market data'))
    fig.update_layout(title = f'Stocks para {cia}', yaxis_title = 'Valor', width=1000, height=700)
    st.plotly_chart(fig)

else:
    st.info("El nombre de la compañía o la combinación 'Intervalo-Periodo' no se encuentra disponible en Yahoo Finance")
