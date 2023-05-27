import requests  # Importa o módulo "requests" para fazer requisições HTTP

def requestJob(url: str, status_code_expected: int):
    try:
        print("Requesting...")  # Imprime uma mensagem indicando que a requisição está sendo feita
        print("URL: " + url)  # Imprime a URL da requisição
        response = requests.get(url)  # Realiza a requisição GET para a URL especificada
        if(response.status_code == status_code_expected):  # Verifica se o código de status da resposta é igual ao código esperado
            print("Request OK")  # Imprime uma mensagem indicando que a requisição foi bem-sucedida
        else:
            print("Request failed")  # Imprime uma mensagem indicando que a requisição falhou
    except Exception as e:  # Captura qualquer exceção ocorrida durante a requisição
        print(e)  # Imprime a exceção
        return False  # Retorna False para indicar que a requisição falhou
