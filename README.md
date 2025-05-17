# Pipeline Rodoprima – Analista de Dados

Este projeto executa uma pipeline completa "end-to-end" automatizada para o teste técnico da Rodoprima Transportes.

## Etapas Automatizadas

1. **RPA (PyAutoGUI)** – Baixa as abas "CTE" e "CONTRATOS DE FRETE" do Google Sheets.
2. **ETL (Pandas)** – Padroniza colunas, remove cancelados e duplicados, trata nulos.
3. **Carga (BigQuery)** – Carrega os dados limpos para tabelas no BigQuery.

## Como usar

1. Instale os pacotes necessários:
```bash
pip install pyautogui pyperclip pandas google-cloud-bigquery
```

2. Configure o arquivo `config.py` com:
   - Caminho para a chave JSON de autenticação do BigQuery
   - Nome do projeto, dataset e tabelas

3. Execute o pipeline completo:
```bash
python main.py
```

## Observação

A parte do dashboard no Looker Studio foi feita manualmente usando os dados carregados no BigQuery.
