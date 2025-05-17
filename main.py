import os

print("Iniciando RPA para baixar planilhas...")
os.system("py rpa_rodoprima.py")

print("Executando ETL nos arquivos baixados...")
os.system("py etl_rodoprima.py")

print("Carregando dados tratados no BigQuery...")
os.system("py bigquery_loader.py")