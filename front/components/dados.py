from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

API_BASE_URL = "http://localhost:8000/api"

estados = [
    {"label": "Acre", "value": "acre"},
    {"label": "Alagoas", "value": "alagoas"},
    {"label": "Amapá", "value": "amapa"},
    {"label": "Amazonas", "value": "amazonas"},
    {"label": "Bahia", "value": "bahia"},
    {"label": "Ceará", "value": "ceara"},
    {"label": "Distrito Federal", "value": "distrito_federal"},
    {"label": "Espírito Santo", "value": "espirito_santo"},
    {"label": "Goiás", "value": "goias"},
    {"label": "Maranhão", "value": "maranhao"},
    {"label": "Mato Grosso", "value": "mato_grosso"},
    {"label": "Mato Grosso do Sul", "value": "mato_grosso_do_sul"},
    {"label": "Minas Gerais", "value": "minas_gerais"},
    {"label": "Pará", "value": "para"},
    {"label": "Paraíba", "value": "paraiba"},
    {"label": "Paraná", "value": "parana"},
    {"label": "Pernambuco", "value": "pernambuco"},
    {"label": "Piauí", "value": "piaui"},
    {"label": "Rio de Janeiro", "value": "rio_de_janeiro"},
    {"label": "Rio Grande do Norte", "value": "rio_grande_do_norte"},
    {"label": "Rio Grande do Sul", "value": "rio_grande_do_sul"},
    {"label": "Rondônia", "value": "rondonia"},
    {"label": "Roraima", "value": "roraima"},
    {"label": "Santa Catarina", "value": "santa_catarina"},
    {"label": "São Paulo", "value": "sao_paulo"},
    {"label": "Sergipe", "value": "sergipe"},
    {"label": "Tocantins", "value": "tocantins"},
]


def render_dados_page():
    return html.Div([
        html.H3("Download de dados", style={"margin-bottom": "20px"}),

        dbc.Row([
            # Coluna Esquerda
            dbc.Col([
                # Card CID-10
                dbc.Card(
                    dbc.CardBody([
                        html.H5("CID-10", className="card-title"),
                        html.P("Arquivo com categorias e subcategorias CID-10.", className="card-text"),
                        dbc.Button(
                            [html.I(className="fas fa-download", style={"margin-right": "10px"}), "Baixar CSV"],
                            color="primary",
                            href=f"{API_BASE_URL}/download_cid10",
                            external_link=True
                        )
                    ]),
                    style={"margin-bottom": "20px"}
                ),

                # Card Óbitos por Estado
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Óbitos por Estado (CID-10)", className="card-title"),
                        html.P("Selecione um estado para baixar os dados de óbitos (CID-10).", className="card-text"),
                        dcc.Dropdown(
                            id="dropdown-estado-1",
                            options=estados,
                            placeholder="Selecione um estado...",
                            style={"margin-bottom": "15px"}
                        ),
                        dbc.Button(
                            [html.I(className="fas fa-download", style={"margin-right": "10px"}), "Baixar CSV"],
                            color="primary",
                            id="btn-download-1",
                            href="#",
                            external_link=True,
                            disabled=True
                        )
                    ])
                )
            ], width=6),

            # Coluna Direita
            dbc.Col([
                # Card CID-9
                dbc.Card(
                    dbc.CardBody([
                        html.H5("CID-9", className="card-title"),
                        html.P("Arquivos com categorias CID-9 e CID-9-BR.", className="card-text"),
                        dbc.Button(
                            [html.I(className="fas fa-download", style={"margin-right": "10px"}), "Baixar CID-9"],
                            color="primary",
                            href="#",  # Ajustar depois para API
                            external_link=True,
                            style={"margin-right": "10px"}
                        ),
                        dbc.Button(
                            [html.I(className="fas fa-download", style={"margin-right": "10px"}), "Baixar CID-9-BR"],
                            color="primary",
                            href="#",  # Ajustar depois para API
                            external_link=True
                        )
                    ]),
                    style={"margin-bottom": "20px"}
                ),

                # Card Óbitos por Estado (CID-9)
                dbc.Card(
                    dbc.CardBody([
                        html.H5("Óbitos por Estado (CID-9)", className="card-title"),
                        html.P("Selecione um estado para baixar os dados de óbitos (CID-9).", className="card-text"),
                        dcc.Dropdown(
                            id="dropdown-estado-2",
                            options=estados,
                            placeholder="Selecione um estado...",
                            style={"margin-bottom": "15px"}
                        ),
                        dbc.Button(
                            [html.I(className="fas fa-download", style={"margin-right": "10px"}), "Baixar CSV"],
                            color="primary",
                            id="btn-download-2",
                            href="#",
                            external_link=True,
                            disabled=True
                        )
                    ])
                )
            ], width=6),
        ])
    ], style={"padding": "20px"})

