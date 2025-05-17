import pyautogui
import pyperclip
import platform
import locale
import time
import webbrowser
import os

resolucao = pyautogui.size()
sistema = platform.system()
idioma = locale.getdefaultlocale()[0]

# URL da planilha
url = "https://docs.google.com/spreadsheets/d/1AhbsIqh6mQ8J4cKRgEkHokNo2uNmsxkYZL0hxbzxZtc"

# Abrir o navegador e acessar a planilha
webbrowser.open(url)
time.sleep(10)  # Esperar a planilha carregar
download_dir = os.path.join(os.path.expanduser("~"), "Downloads")

def renomear_csv(nome_final):
    timeout = time.time() + 30
    ultimo_csv = None

    while time.time() < timeout:
        arquivos = [f for f in os.listdir(download_dir) if f.endswith(".csv")]
        if arquivos:
            arquivos.sort(key=lambda f: os.path.getctime(os.path.join(download_dir, f)), reverse=True)
            ultimo_csv = arquivos[0]
            break
        time.sleep(1)

    if ultimo_csv:
        origem = os.path.join(download_dir, ultimo_csv)
        destino = os.path.join(download_dir, nome_final)
        try:
            os.rename(origem, destino)
            print(f"Arquivo renomeado para: {destino}")
        except Exception as e:
            print(f"Erro ao renomear: {e}")
    else:
        print("Nenhum arquivo CSV encontrado para renomear.")


# Função para exportar uma aba
def export_sheet(sheet_name, nome_arquivo_final):
   
    # Baixar como CSV
    pyautogui.hotkey('alt', 'f')  # Abre o menu "Arquivo"
    time.sleep(1)
    pyautogui.press('d')          # Baixar
    time.sleep(1)
    pyautogui.press('c')      # CSV
    time.sleep(5)
    renomear_csv(nome_arquivo_final)
    time.sleep(2)


# Exportar as duas abas
time.sleep(2)
export_sheet("CONTRATOS DE FRETE", "CONTRATOS_DE_FRETE.csv")
pyautogui.hotkey('alt', 'down')
export_sheet("CTE", "CTE.csv")