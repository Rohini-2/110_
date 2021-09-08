import pandas as pd
import plotly.express as px
df=pd.read_csv("data.csv")
figure=px.scatter(df,x="level",y="attempt")
figure.show()