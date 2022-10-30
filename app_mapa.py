import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(500, 2) / [1.2, 1.2] + [40.4165, -3.70256],
    columns=['lat', 'lon'])

st.map(df)