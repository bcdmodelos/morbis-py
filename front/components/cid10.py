from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
import requests

API_URL = "http://backend:8000/api/cid10"

def render_cid10_page():
    # Busca os dados da API
    try:
        response = requests.get(API_URL)
        if response.status_code != 200:
            return html.Div("Erro ao carregar dados do CID-10", style={"color": "red"})

        data = response.json().get("categorias", [])
        if not data:
            return html.Div("Nenhum dado disponível", style={"color": "orange"})

        # Layout com campo de busca e container para Accordion
        return html.Div([
            html.H3("CID-10 - Classificação Internacional de Doenças", style={"margin-bottom": "20px"}),

            dcc.Input(
                id="cid10-search",
                type="text",
                placeholder="Digite código ou descrição...",
                style={"width": "100%", "padding": "10px", "margin-bottom": "20px"}
            ),

            html.Div(id="cid10-accordion-container")
        ])

    except Exception as e:
        return html.Div(f"Erro: {e}", style={"color": "red"})


# ================================
# CALLBACK PARA FILTRAR RESULTADOS
# ================================

# Guardamos os dados carregados globalmente (poderia ser em cache também)
response = requests.get(API_URL)
DATA_CACHE = response.json().get("categorias", [])

@callback(
    Output("cid10-accordion-container", "children"),
    Input("cid10-search", "value")
)
def update_accordion(search_text):
    # Se não digitar nada, mostra todos
    search_text = (search_text or "").lower()

    filtered_data = []
    for categoria in DATA_CACHE:
        # Filtrar categoria e subcategorias
        cat_match = search_text in categoria["categoria"].lower() or search_text in categoria["descricao"].lower()
        subcats = [
            sub for sub in categoria["subcategorias"]
            if search_text in sub["cid10"].lower() or search_text in sub["descricao"].lower()
        ]

        # Incluir categoria se ela ou alguma subcategoria bater
        if cat_match or subcats:
            filtered_data.append({
                "categoria": categoria["categoria"],
                "descricao": categoria["descricao"],
                "subcategorias": subcats if not cat_match else categoria["subcategorias"]
            })

    if not filtered_data:
        return html.Div("Nenhum resultado encontrado.", style={"color": "orange"})

    accordion_items = []
    for categoria in filtered_data:
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

    return dbc.Accordion(accordion_items, always_open=False, start_collapsed=True)
