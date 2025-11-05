"""
This file contains the features of the english materials
"""

import csv
import os
import pandas as pd
import uuid
from tabulate import tabulate

# para caminhos
base_dir = os.path.dirname(__file__)
PASTA_DATA = 'data'

ARQUIVOS = {
    'aulas': os.path.join(base_dir, PASTA_DATA, 'aulas.csv'),
    'exercicios': os.path.join(base_dir, PASTA_DATA, 'exercicios.csv'),
    'textos': os.path.join(base_dir, PASTA_DATA, 'textos.csv')
}

# Criação automática dos CSVs se não existirem SVSVSVSV
def verificar_csvs_materiais():
    os.makedirs(PASTA_DATA, exist_ok=True)
    for nome, caminho in ARQUIVOS.items():
        if not os.path.exists(caminho):
            with open(caminho, "w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["ID", "Nome", "Nível"])
            print(f"[+] Criado arquivo: {caminho}")

def inputs_cadastro_material():

    # Cria id com uuid e da slice na string, deixando o mesmo com apenas 8 caracteres
    id_material = (str(uuid.uuid4())[:8])

def visualizar_material(tipo):

    # Abre e faz a leitura do .csv
    with open(caminho_csv, newline='') as arquivocsv:

        leitor_csv = csv.DictReader(arquivocsv)

        headers = ['ID','Nome', 'Status', 'Aulas Assistidas', 'Dia do Pagamento', 'Nível']
        table = [] # Lista Vazia

        # Insere cada campo da linha especifica dentro da tabela
        for linha in leitor_csv:
            table.append([linha['ID'], linha['Nome'], linha['Status'], linha['Aulas'], linha['Dia do Pagamento'], linha['Nivel']]) 

        print(tabulate(table, headers=headers, tablefmt="fancy_grid")) # Usa o cabecalho headers que definimos anteriormente
        # Dispensa o uso de loop, printa cada linha uma vez assim como o cabecalho