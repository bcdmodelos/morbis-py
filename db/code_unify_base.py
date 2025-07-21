import os
import pandas as pd

# Caminho base onde estão os diretórios por estado
base_dir = "./data/data_datasus"

# Listar os diretórios de cada estado
estados_dirs = [os.path.join(base_dir, d) for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# ============================================
# 1) Descobrir TODAS as colunas globais
# ============================================
print("🔍 Coletando todas as colunas globais...")
all_columns_global = set()

for estado_path in estados_dirs:
    arquivos = [f for f in os.listdir(estado_path) if f.endswith(".csv")]
    for arquivo in arquivos:
        path = os.path.join(estado_path, arquivo)
        try:
            df_temp = pd.read_csv(path, nrows=5)  # lê só as primeiras linhas
            all_columns_global.update(df_temp.columns)
        except Exception as e:
            print(f"⚠ Erro lendo cabeçalho de {arquivo}: {e}")

# Ordena colunas para consistência
all_columns_global = sorted(list(all_columns_global))

# Adiciona colunas extras
all_columns_global += ["ANO_ARQUIVO"]

print(f"✅ Total de colunas globais: {len(all_columns_global)}")

# ============================================
# 2) Processar cada estado e gerar um arquivo único
# ============================================
for estado_path in estados_dirs:
    sigla = os.path.basename(estado_path)
    output_path = os.path.join(estado_path, f"{sigla}_unificado.csv")
    arquivos = sorted([f for f in os.listdir(estado_path) if f.endswith(".csv")])

    print(f"\n▶ Processando estado {sigla} ({len(arquivos)} arquivos)...")

    # Cria arquivo vazio com cabeçalho
    pd.DataFrame(columns=all_columns_global).to_csv(output_path, index=False)

    for arquivo in arquivos:
        path = os.path.join(estado_path, arquivo)
        try:
            # Lê arquivo completo como texto (evita erros de tipo)
            df = pd.read_csv(path, dtype=str)

            # Padroniza colunas
            df_alinhado = df.reindex(columns=all_columns_global[:-1])  # sem ANO_ARQUIVO
            df_alinhado["ANO_ARQUIVO"] = arquivo[-8:-4]  # extrai ano do nome

            # Salva no arquivo do estado em modo append
            df_alinhado.to_csv(output_path, mode="a", index=False, header=False)

            print(f"   [+] Adicionado {arquivo} ({len(df_alinhado)} registros)")
        except Exception as e:
            print(f"⚠ Erro lendo {arquivo}: {e}")

    print(f"✅ Estado {sigla} consolidado → {output_path}")

print("\n✅ Todos os estados foram processados!")