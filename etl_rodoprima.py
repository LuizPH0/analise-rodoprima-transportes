import pandas as pd
import os

# Caminho da pasta Downloads
download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# Caminhos completos dos arquivos baixados
cte_path = os.path.join(download_dir, "CTE.csv")
frete_path = os.path.join(download_dir, "CONTRATOS_DE_FRETE.csv")

# Verificação de existência
if not os.path.exists(cte_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {cte_path}")
if not os.path.exists(frete_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {frete_path}")

# Leitura dos dados
cte = pd.read_csv(cte_path)
frete = pd.read_csv(frete_path)

# Padronização
cte.columns = cte.columns.str.strip().str.upper().str.replace(" ", "_")
frete.columns = frete.columns.str.strip().str.upper().str.replace(" ", "_")

# Limpeza
cte = cte[cte['STATUS'] != 'Cancelado'].drop_duplicates().fillna(0)
frete = frete[frete['STATUS'] != 'Cancelado'].drop_duplicates().fillna(0)

# Exportação para os arquivos tratados
cte.to_csv("cte_tratado.csv", index=False)
frete.to_csv("frete_tratado.csv", index=False)

print("✅ ETL concluído. Arquivos tratados salvos com sucesso.")
