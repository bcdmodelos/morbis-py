from dash import dcc, html

def render_header():
    link_style = {
        "margin-right": "15px",
        "color": "white",
        "text-decoration": "none"
    }

    return html.Div(
        [
            html.H2("MorbIS - Mortality Information System", style={"color": "white", "margin": "0"}),
            html.Div([
                html.A("Home", href="#", style=link_style),
                html.A("Mapa", href="/mapa", style=link_style),
                dcc.Link("CID", href="/cid", style=link_style),
                html.A("Dados", href="/dados", style=link_style),
                html.A("Sobre", href="/sobre", style={"color": "white", "text-decoration": "none"})
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
