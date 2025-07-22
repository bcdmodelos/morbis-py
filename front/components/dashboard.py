from dash import html, dcc

def render_dashboard():
    return html.Div([
        html.H3("Dashboard", style={"color": "#2c3e50"}),
        html.P("Clique em um estado para ver os dados", style={"margin-bottom": "20px"}),
        dcc.Graph(id="grafico", figure={})
    ],
    style={"flex": "1", "padding": "20px"})
