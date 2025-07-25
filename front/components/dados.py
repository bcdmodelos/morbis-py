from dash import html

def render_dados_page():
    return html.Div([
        html.H3("Download de dados"),
        html.P("O MorbIS disponibiliza os dados utilizados para download.")
    ])
