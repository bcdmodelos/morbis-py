from dash import html, dcc

def render_dashboard():
    return html.Div([
        html.H2("Dashboard"),
        html.P("Clique em um estado para ver os dados"),
        dcc.Graph(id="dashboard-graph")
    ], style={"flex": "1", "padding": "20px"})