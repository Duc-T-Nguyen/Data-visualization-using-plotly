
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go


df = pd.read_csv('./ecu_data.csv')
app = Dash(__name__)

app.layout = html.Div([
    html.H4('Powertrain Histogram:'),
    dcc.Graph(id="histogram"),
])

@app.callback(
    Output('histogram', 'figure' ),
    [Input('histogram', 'id')]
)
def update_histogram(n):
    fig = go.Figure(data=[go.Histogram(x=df['RPM'], nbinsx=7)])
    fig.update_layout(
        bargap = .1,
        xaxis_title='RPM',
        yaxis_title='Frequency',
        title='RPM Histogram',
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

