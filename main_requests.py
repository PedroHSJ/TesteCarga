import datetime
import requests

from excel import adicionar_dados_excel  # Importa o módulo "requests" para fazer requisições HTTP

def requestJob(url: str, status_code_expected: int, number_of_requests: int, data: dict = {}):
    try:
        inicio = datetime.datetime.now()  # Obtém a data e hora atuais
        print("Requesting...")  # Imprime uma mensagem indicando que a requisição está sendo feita
        print("URL: " + url)  # Imprime a URL da requisição
        
        response = requests.get(url)  # Realiza a requisição GET para a URL especificada
        if(response.status_code == status_code_expected):  # Verifica se o código de status da resposta é igual ao código esperado
            fim = datetime.datetime.now()        
            tempo = fim - inicio
            #tempo = tempo.seconds
            print(tempo)
            adicionar_dados_excel(arquivo_excel="./output/dados.xlsx", volume_de_dados=number_of_requests, tempo=tempo, url=url)
            
            print("Request OK")  # Imprime uma mensagem indicando que a requisição foi bem-sucedida
        else:
            print(response)
            print("Request failed")  # Imprime uma mensagem indicando que a requisição falhou
    except Exception as e:  # Captura qualquer exceção ocorrida durante a requisição
        print(e)  # Imprime a exceção
        return []  
