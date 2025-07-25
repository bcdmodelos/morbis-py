from dash import html
import dash_bootstrap_components as dbc

def render_sobre_page():
    # Texto sobre o projeto
    texto_sobre = """
    Este projeto tem como objetivo disseminar e fornecer informações sobre a mortalidade e morbidade da população Brasileira de uma forma simples e intuitiva, a partir de dados atualizados do Sistema de Informação sobre Mortalidade (SIM) e do Instituto Brasileiro de Geografia e Estatística (IBGE).

    O SIM é um sistema desenvolvido pelo Ministério da Saúde, que reúne dados quantitativos e qualitativos sobre óbitos ocorridos no Brasil. Criado em 1979, o sistema passou por várias atualizações e atualmente conta com mais de 70 campos, com informações sobre mortalidade infantil, mortalidade materna e mortalidade por causas específicas classificadas pela CID-10, além de mortalidade por causas externas, acidentes de trabalho e causas mal definidas.

    A Classificação Estatística Internacional de Doenças e Problemas Relacionados com a Saúde (CID), publicado pela Organização Mundial de Saúde (OMS), estabelece o padrão internacional para relatar doenças. Este sistema foi desenhado para permitir e promover a comparação da coleção, processamento, classificação e apresentação de dados e estatísticas de doenças a nível internacional. A CID é revista periodicamente e encontra atualmente na sua décima edição (CID-10).

    O Ministério da Saúde coloca à disposição dados conclusivos sobre os óbitos registrados desde 1979, de modo que qualquer pessoa pode fazer uma consulta à base de dados utilizando o aplicativo pelo Tabnet, um tabulador genérico de domínio público desenvolvido pelo DATASUS. Entretanto, este sistema é pouco intuitivo e pouco eficiente para consultas mais abrangentes.

    Acreditamos que o uso destes dados através de uma interface amigável e intuitiva, poderá auxiliar pesquisadores, profissionais de saúde e formuladores de políticas públicas a obterem dados importantes para as suas atividades. Nesta primeira versão, o usuário poderá consultar estatísticas sobre mortalidade de uma doença específica (classificada pela CID-10) para regiões, estados ou municípios brasileiros e também selecionar parâmetros populacionais como gênero, idade e raça/cor. Os resultados das consultas realizadas podem ser visualizados em gráficos ou baixados para análises posteriores.

    Este projeto é desenvolvido em parceria por pesquisadores da Universidade Federal do Rio Grande do Norte (UFRN) e Universidade Federal de Campina Grande (UFCG). O código-fonte do app pode ser acessado no GitHub.
    """

    # Lista de pesquisadores (foto, nome, descrição)
    pesquisadores = [
        {"nome": "Beatriz Stransky, DSc.", "descricao": "Professora do Departamento de Engenharia Biomédica da Universidade Federal do Rio Grande do Norte. UFRN", "foto": "/assets/team/Beatriz.jpg"},
        {"nome": "Marcus Nunes, DSc.", "descricao": "Professor do Departamento de Estatística da Universidade Federal do Rio Grande do Norte. UFRN", "foto": "/assets/team/Marcus.jpg"},
        {"nome": "Bruno Dantas, DSc.", "descricao": "Ainda falta colcar, UFCG", "foto": "/assets/team/Bruno.jpg"},
        {"nome": "Alessandro Pereira, Bach.", "descricao": "Aind afalta colocar, UFRN", "foto": "/assets/team/Alessandro.png"},
    ]


    # Layout com cards de pesquisadores
    cards = []
    for pesquisador in pesquisadores:
        cards.append(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src=pesquisador["foto"],
                            top=True,
                            style={
                                "width": "150px",
                                "height": "150px",
                                "object-fit": "cover",
                                "border-radius": "50%",
                                "margin": "20px auto 10px auto",
                                "display": "block"
                            }
                        ),
                        dbc.CardBody([
                            html.H5(pesquisador["nome"], className="card-title", style={"text-align": "center"}),
                            html.P(pesquisador["descricao"], className="card-text", style={"text-align": "center"})
                        ])
                    ],
                    style={"width": "18rem", "margin-bottom": "20px", "text-align": "center"}
                ),
                width=6
            )
        )

    return html.Div([
        html.H3("Sobre o MorbIS", style={"margin-bottom": "20px"}),
        html.P(texto_sobre, style={"text-align": "justify", "margin-bottom": "40px"}),

        html.H4("Pesquisadores", style={"margin-bottom": "20px"}),
        dbc.Row(cards[:2], justify="center"),
        dbc.Row(cards[2:], justify="center")
    ], style={"padding": "20px"})
