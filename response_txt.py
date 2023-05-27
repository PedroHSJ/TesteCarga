import requests

def gravar_resposta_em_arquivo(response, nome_arquivo):

    # Verifica se a requisição foi bem-sucedida (código 200)
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(response)
        print("Resposta gravada com sucesso!")



