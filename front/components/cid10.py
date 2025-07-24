from dash import html
import dash_bootstrap_components as dbc
import requests

API_URL = "http://backend:8000/api/cid10"

def render_cid10_page():
    try:
        response = requests.get(API_URL)
        if response.status_code != 200:
            return html.Div("Erro ao carregar dados do CID-10", style={"color": "red"})

        data = response.json().get("categorias", [])
        if not data:
            return html.Div("Nenhum dado disponível", style={"color": "orange"})

        accordion_items = []
        for categoria in data:
            sub_itens = [
                html.Li(f"{item['cid10']} - {item['descricao']}") 
                for item in categoria["subcategorias"]
            ]

            accordion_items.append(
                dbc.AccordionItem(
                    [
                        html.H5(f"{categoria['categoria']} - {categoria['descricao']}", style={"margin-bottom": "10px"}),
                        html.Ul(sub_itens)
                    ],
                    title=f"{categoria['categoria']} - {categoria['descricao']}"
                )
            )

        return html.Div([
            html.H3("CID-10 - Classificação Internacional de Doenças", style={"margin-bottom": "20px"}),
            dbc.Accordion(accordion_items, always_open=False, start_collapsed=True)
        ])

    except Exception as e:
        return html.Div(f"Erro: {e}", style={"color": "red"})
