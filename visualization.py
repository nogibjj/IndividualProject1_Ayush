import pandas as pd
import plotly.express as px


df = pd.read_csv("World University Rankings 2023.csv")

result1= df.groupby(['country'])['finalWorth'].mean().reset_index()
fig = px.bar(result1, x='country', y='finalWorth')
fig.show()
