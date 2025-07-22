from dash import html

def render_header():
    return html.Div(
        [
            html.H2("MorbIS - Mortality Information System", style={"color": "white", "margin": "0"}),
            html.Div([
                html.A("Home", href="#", style={"margin-right": "15px", "color": "white"}),
                html.A("Mapa", href="#", style={"margin-right": "15px", "color": "white"}),
                html.A("Relatórios", href="#", style={"color": "white"})
            ], style={"display": "flex"})
        ],
        style={
            "background-color": "#2c3e50",
            "padding": "10px 20px",
            "display": "flex",
            "justify-content": "space-between",
            "align-items": "center"
        }
    )
