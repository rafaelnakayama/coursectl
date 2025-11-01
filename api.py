"""
This file contains the API features
"""

import os
from google.auth.transport.requests import Request  # Requiscoes http
from google.oauth2.credentials import Credentials # Gerencia o token de Acesso
from google_auth_oauthlib.flow import InstalledAppFlow # controla o fluxo do OAuth (autenticacao via navegador)

from googleapiclient.discovery import build


# Define o Escopo (O que o programa pode fazer no drive) da API, neste caso apenas leitura
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

caminho_token = os.path.join(os.path.dirname(__file__), "data", "token.json")

camninho_cred = os.path.join(os.path.dirname(__file__), "data", "credenciais.json")

# SIU

def autenticar():
    credenciais = None

    # Se ja existir
    if os.path.exists(caminho_token):
        # Carrega as credenciais salvas
        credenciais = Credentials.from_authorized_user_file(caminho_token, SCOPES)

    # Se nao existir ou nao houverem credenciais validas disponiveis, o usuario ira logar.
    if not credenciais or not credenciais.valid:
        if credenciais and credenciais.expired and credenciais.refresh_token:
            credenciais.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(camninho_cred, SCOPES)
            credenciais = flow.run_local_server(port=0)
        # Salvar as credenciais para a proxima autenticacao
        with open(caminho_token, 'w') as token:
            token.write(credenciais.to_json())

    return credenciais

credenciais = autenticar()
service = build('drive', 'v3', credentials=credenciais)