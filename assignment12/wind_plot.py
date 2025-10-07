import plotly.express as px
import plotly.data as pldata
import pandas as pd
import webbrowser
import os


df= pldata.wind (return_type='pandas')

print('first 10 rows:')
print(df.head(10))
print('\nlast 10 rows:')
print(df.tail(10))

df['strength'] = df['strength'].str.replace('[^0-9.]', '', regex=True)
df['strength'] = df['strength'].astype(float)

fig= px.scatter(
    df,
    x= 'strength',
    y='frequency',
    color='direction',
    title= 'wind strength vs frequency by direction',
    labels={'strength':'wind strength', 'frequency':'frequency'}
)
fig.write_html('wind.html')
webbrowser.open('file://' + os.path.realpath('wind.html'))