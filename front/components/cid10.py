from dash import html
import dash_bootstrap_components as dbc
import requests

API_URL = "http://backend:8000/api/cid10"  # Docker: nome do serviço

def render_cid10_page():
    try:
        response = requests.get(API_URL)
        if response.status_code != 200:
            return html.Div("Erro ao carregar dados do CID-10", style={"color": "red"})

        data = response.json().get("categorias", [])
        if not data:
            return html.Div("Nenhum dado disponível", style={"color": "orange"})

        accordion_items = []
        for i, categoria in enumerate(data):
            sub_itens = [html.Li(f"{item['subcat']} - {item['descricao']}") for item in categoria["itens"]]

            accordion_items.append(
                dbc.AccordionItem(
                    [
                        html.H5(f"Categoria {categoria['categoria']}", style={"margin-bottom": "10px"}),
                        html.Ul(sub_itens)
                    ],
                    title=f"Categoria {categoria['categoria']}"
                )
            )

        return html.Div([
            html.H3("CID-10 - Classificação Internacional de Doenças", style={"margin-bottom": "20px"}),
            dbc.Accordion(accordion_items, always_open=False, start_collapsed=True)
        ])

    except Exception as e:
        return html.Div(f"Erro: {e}", style={"color": "red"})
