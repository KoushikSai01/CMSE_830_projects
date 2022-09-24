import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df_i=sns.load_dataset("iris")
scatter=px.scatter_3d(data_frame=df_i,x="sepal_length",y="sepal_width",z="petal_width",color="species")
fig=px.violin(df_i, x="species", y="sepal_width")

df_pl=sns.load_dataset("planets")
fig1, ax=plt.subplots()
ax.plot(df_pl['method'],df_pl['year'])
ax.plot(df_pl['method'],df_pl['distance'])
ax.legend()
plt.show()

st.write("Scatter Plot")
st.plotly_chart(scatter,use_container_width=True)
