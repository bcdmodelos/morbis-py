from dash import dcc, html
import plotly.express as px
import geopandas as gpd

# Carregar shapefile
gdf_uf = gpd.read_file("/app/data/dtb/uf/BR_UF_2022.shp").to_crs(epsg=4326)

# Criar figura inicial
fig = px.choropleth_mapbox(
    gdf_uf,
    geojson=gdf_uf.geometry,
    locations=gdf_uf.index,
    color_discrete_sequence=["#3498db"],
    center={"lat": -14.235, "lon": -51.925},
    mapbox_style="carto-positron",
    zoom=3
)

def render_map():
    return html.Div(
        dcc.Graph(id="mapa", figure=fig, style={"height": "100%", "width": "100%"}),
        style={"flex": "1", "border-right": "1px solid #ccc"}
    )
