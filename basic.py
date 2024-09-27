import streamlit as st
import pandas as pd
import numpy as np

view = [100, 200, 300, 400, 500]
st.write("# This is a simple bar chart using Streamlit.")
st.write("## The data is represented as bars, where the length of each bar corresponds to the value of the data point.")
view
st.bar_chart(view)


sview = pd.Series(view, name='Views')
sview

