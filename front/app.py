import dash
from dash import html
import dash_bootstrap_components as dbc
from components.header import render_header
from components.map import render_map
from components.dashboard import render_dashboard

app = dash.Dash(
    __name__,
    title="MorbIS",
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div([
    render_header(),
    html.Div([
        render_map(),
        render_dashboard()
    ],
    style={
        "display": "flex",
        "flex-direction": "row",
        "height": "calc(100vh - 60px)"
    })
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=False)
