from dash import html

def render_sobre_page():
    return html.Div([
        html.H3("Sobre o MorbIS"),
        html.P("O MorbIS é um sistema para análise de mortalidade baseado em dados do SIM (DATASUS).")
    ])
