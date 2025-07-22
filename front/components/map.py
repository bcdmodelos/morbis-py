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

import plotly.express as px
from dash import dcc, html
import geopandas as gpd

def render_map():
    gdf_uf = gpd.read_file("/app/data/dtb/uf/BR_UF_2022.shp").to_crs(epsg=4326)

    fig = px.choropleth_mapbox(
        gdf_uf,
        geojson=gdf_uf.geometry,
        locations=gdf_uf.index,
        color_discrete_sequence=["#3498db"],
        center={"lat": -14.235, "lon": -51.925},
        zoom=3
    )

    fig.update_layout(
        mapbox_style="white-bg",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    return html.Div([
        dcc.Graph(id="map", figure=fig, style={"height": "100%", "width": "100%"})
    ], style={"flex": "2", "border-right": "1px solid #ccc"})

