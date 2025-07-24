from fastapi import FastAPI
from app.routes import (estados,
                        municipios,
                        obitos_totais,
                        obitos_ano,
                        obitos_causa,
                        obitos_maior_causa,
                        obitos_top10,
                        obitos_bottom10,
                        obitos_regiao,
                        obitos_regiao_causa,
                        cid10)

app = FastAPI(title="MORBIS API")

app.include_router(estados.router, prefix="/api")
app.include_router(municipios.router, prefix="/api")
app.include_router(obitos_totais.router, prefix="/api")
app.include_router(obitos_ano.router, prefix="/api")
app.include_router(obitos_causa.router, prefix="/api")
app.include_router(obitos_maior_causa.router, prefix="/api")
app.include_router(obitos_top10.router, prefix="/api")
app.include_router(obitos_bottom10.router, prefix="/api")
app.include_router(obitos_regiao.router, prefix="/api")
app.include_router(obitos_regiao_causa.router, prefix="/api")
app.include_router(cid10.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend funcionando!"}
