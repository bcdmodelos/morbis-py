from dash import html
import dash_bootstrap_components as dbc

#API_DOWNLOAD_URL = "http://backend:8000/download/cid10"
API_DOWNLOAD_URL = "http://localhost:8000/api/download/cid10"

def render_dados_page():
    return html.Div([
        html.H3("Download de dados", style={"margin-bottom": "20px"}),
        html.P("O MorbIS disponibiliza os dados utilizados para download.", style={"margin-bottom": "20px"}),

        dbc.Card(
            dbc.CardBody([
                html.H5("CID-10 - Classificação Internacional de Doenças", className="card-title"),
                html.P("Arquivo com a lista completa de categorias e subcategorias CID-10.", className="card-text"),

                dbc.Button(
                    [html.I(className="fas fa-download", style={"margin-right": "10px"}), "Baixar CSV"],
                    color="primary",
                    href=API_DOWNLOAD_URL,
                    external_link=True,
                    style={"margin-top": "10px"}
                )

            ]),
            style={"width": "50%", "padding": "20px"}
        )
    ], style={"padding": "20px"})

