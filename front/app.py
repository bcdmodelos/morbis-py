import dash
from dash import html
from components.header import render_header

app = dash.Dash(
    __name__,
    title="MorbIS",
    assets_folder="assets")

app.layout = html.Div([
    render_header(),
    html.H1("MorbIS - Mortality Information System"),
    html.P("Aplicação inicial com Dash está rodando!")
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=False)