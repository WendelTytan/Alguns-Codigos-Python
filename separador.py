import shutil

def mover_arquivos(pasta_origem, pasta_destino, lista_nomes_arquivos):
    for nome_arquivo in lista_nomes_arquivos:
        origem = f'{pasta_origem}/{nome_arquivo}'
        destino = f'{pasta_destino}/{nome_arquivo}'
        try:
            shutil.move(origem, destino)
            print(f'Arquivo {nome_arquivo} movido com sucesso de {pasta_origem} para {pasta_destino}.')
        except FileNotFoundError:
            print(f'Arquivo {nome_arquivo} não encontrado na pasta de origem {pasta_origem}.')
        except shutil.Error:
            print(f'Falha ao mover o arquivo {nome_arquivo}.')

nomes_arquivos1 = []
with open(r'caminho direto para .txt do primeiro para separar', 'r') as arquivo1:
    for linha in arquivo1:
        nomes_arquivos1.append(linha.strip())

nomes_arquivos2 = []
with open(r'caminho direto para .txt do segundo para separar', 'r') as arquivo2:
    for linha in arquivo2:
        nomes_arquivos2.append(linha.strip())

pasta_origem1 = r'caminho onde estão os arquivos origem 1'
pasta_destino1 = r'caminho onde serão salvos 1'
mover_arquivos(pasta_origem1, pasta_destino1, nomes_arquivos1)

pasta_origem2 = r'caminho onde estão os arquivos origem 2'
pasta_destino2 = r'caminho onde serão salvos 2'
mover_arquivos(pasta_origem2, pasta_destino2, nomes_arquivos2)

print('Todos os arquivos foram movidos.')
