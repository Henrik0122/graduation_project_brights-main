import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_excel('silver\silver_kantarell.xlsx')

app = dash.Dash(__name__)

map_graph = dcc.Graph(
        id='map-graph',
        figure=px.scatter_mapbox(
            df,
            lat='Nordkoordinat',
            lon='Østkoordinat',
            title='Observasjoner av sopp i Norge',
            mapbox_style='open-street-map',  
            zoom=3, 
        ),
        style={'height': '700px', 'width': '700px'}
    )

app.layout = html.Div([map_graph])

if __name__ == '__main__':
    app.run_server(debug=True)

