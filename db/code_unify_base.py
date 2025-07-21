import os
import pandas as pd

# Caminho base onde estão os diretórios por estado
base_dir = "./data/data_datasus"

# Listar os diretórios de cada estado
estados_dirs = [os.path.join(base_dir, d) for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Função para consolidar arquivos CSV de um estado
def consolidar_estado(estado_path):
    arquivos = sorted([f for f in os.listdir(estado_path) if f.endswith(".csv")])
    dataframes = []

    # Obter todas as colunas únicas existentes entre os arquivos
    all_columns = set()
    for arquivo in arquivos:
        path = os.path.join(estado_path, arquivo)
        try:
            df_temp = pd.read_csv(path, nrows=5)
            all_columns.update(df_temp.columns)
        except Exception as e:
            print(f"Erro lendo cabeçalho de {arquivo}: {e}")

    all_columns = sorted(list(all_columns))  # manter consistência na ordem

    # Carregar todos os arquivos e alinhar colunas
    for arquivo in arquivos:
        path = os.path.join(estado_path, arquivo)
        try:
            df = pd.read_csv(path, dtype=str)  # ler tudo como texto para evitar erros de tipo
            df_alinhado = df.reindex(columns=all_columns)
            df_alinhado["ANO_ARQUIVO"] = arquivo[-8:-4]  # extrai o ano do nome do arquivo
            dataframes.append(df_alinhado)
        except Exception as e:
            print(f"Erro lendo {arquivo}: {e}")

    # Concatenar todos os anos
    df_final = pd.concat(dataframes, ignore_index=True)

    # Salvar resultado
    sigla = os.path.basename(estado_path)
    output_path = os.path.join(estado_path, f"{sigla}_unificado.csv")
    df_final.to_csv(output_path, index=False)
    print(f"[✓] Consolidado {sigla}: {len(df_final)} registros, {len(all_columns)} colunas → {output_path}")

# Executar para todos os estados
if __name__ == "__main__":
    for estado_path in estados_dirs:
        consolidar_estado(estado_path)