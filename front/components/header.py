from dash import html

def render_header():
    return html.Div(
        style={
            "backgroundColor": "#2c3e50",
            "color": "white",
            "padding": "15px",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-between"
        },
        children=[
            html.H2("MorbIS", style={"margin": "0"}),
            html.Div(
                children=[
                    html.A("Home", href="/", style={"color": "white", "marginRight": "15px"}),
                    html.A("Mapa", href="/map", style={"color": "white", "marginRight": "15px"}),
                    html.A("Relatórios", href="/reports", style={"color": "white"})
                ]
            )
        ]
    )
