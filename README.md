## MORBIS – Sistema de Gestão e Análise de Dados do SIM (DATASUS)

#### Backend

```bash
cd back
```

```bash
cp default.env .env
# then modify it in your text editor of choosing
```
Configurar o .env do back

```bash
Rodar docker-compose --env-file back/.env up -d

ou 

Rodar docker-compose --env-file back/.env up --build -d

```

```bash
Rodar python3 db/create_tables.py
```

```bash
Rodar python3 db/load_data.py
```

```bash
Criar base no docker

docker exec -it morbis_backend bash

python db/create_cid_table.py

```