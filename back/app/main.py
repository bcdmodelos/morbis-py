from fastapi import FastAPI

app = FastAPI(title="MORBIS API")

@app.get("/api/test")
def test():
    return {"message": "API funcionando com sucesso!"}
