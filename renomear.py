import pandas as pd
import os

planilha = pd.read_excel(r'caminho direto da planilha')

for index, linha in planilha.iterrows():
    
    nome_atual = linha['Nome Atual']
    novo_nome = linha['Nome Novo']
    
    caminho_atual = os.path.join(r'caminho dos arquivos a serem renomeados', nome_atual)
    caminho_novo = os.path.join(r'caminho onde ficarão salvo os arquivos renomeados', novo_nome)
    
    os.rename(caminho_atual, caminho_novo)
    
    print(f'Arquivo renomeado de "{nome_atual}" para "{novo_nome}"')

print('Todos os arquivos foram renomeados com sucesso!')
