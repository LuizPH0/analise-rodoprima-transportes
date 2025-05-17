from google.cloud import bigquery
import os
from config import *

def carregar_no_bigquery(dataset_id, tabela_id, caminho_csv):
    client = bigquery.Client.from_service_account_json(BIGQUERY_KEY_PATH)
    tabela_ref = f"{client.project}.{dataset_id}.{tabela_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    with open(caminho_csv, "rb") as source_file:
        job = client.load_table_from_file(source_file, tabela_ref, job_config=job_config)

    job.result()
    print(f"Dados carregados para {tabela_ref} com sucesso.")

carregar_no_bigquery(DATASET_ID, CTE_TABLE, "cte_tratado.csv")
carregar_no_bigquery(DATASET_ID, FRETE_TABLE, "frete_tratado.csv")