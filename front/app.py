import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from components.header import render_header
from components.map import render_map
from components.dashboard import render_dashboard
from components.cid10 import render_cid10_page
from components.sobre import render_sobre_page
from components.dados import render_dados_page

app = dash.Dash(
    __name__,
    title="MorbIS",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://use.fontawesome.com/releases/v5.15.4/css/all.css"
    ]
)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    render_header(),
    html.Div(id='page-content', style={"padding": "20px"})
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/mapa':
        return html.Div([
            html.H3("Mapa e Dashboard"),
            html.Div([
                render_map(),
                render_dashboard()
            ], style={"display": "flex", "flex-direction": "row", "height": "calc(100vh - 120px)"})
        ])
    elif pathname == '/cid10':
        return render_cid10_page()
    elif pathname == '/dados':
        return render_dados_page()
    elif pathname == '/sobre':
        return render_sobre_page()
    else:
        return html.H3("Bem-vindo ao MorbIS! Selecione uma página acima.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=False)
