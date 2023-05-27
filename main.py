import time  # Importa o módulo "time" para trabalhar com tempo
import schedule  # Importa o módulo "schedule" para agendamento de tarefas
from dotenv import load_dotenv  # Importa a função "load_dotenv" do módulo "dotenv" para carregar as variáveis de ambiente
import os  # Importa o módulo "os" para trabalhar com variáveis de ambiente
from run_threaded import run_threaded  # Importa a função "run_threaded" do módulo "run_threaded"
from main_requests import requestJob  # Importa a função "requestJob" do módulo "main_requests"
from load_dotenv import get_dotenv  # Importa a função "get_dotenv" do módulo "load_dotenv"


BASE_URL_CARDIO = get_dotenv("BASE_URL_CARDIO")
data_cardio={
"pacientes": [
            {
                "id": 0,
                "cid": "I10",
                "imc": 29.8487,
                "sexo": "feminino",
                "colesterolTotal": 264.0,
                "hdl": 61.0,
                "ldl": 190.0,
                "idade": 62,
                "hipertenso": True,
                "diabetico": True,
                "tabagista": False,
                "obeso": True,
                "pressaoSistolica": 140.0,
                "pressaoDiastolica": 100.0
            }
        ]
    }

BASE_URL_IRA = get_dotenv("BASE_URL_IRA")
data_ira={
"pacientes": [
    {
      "id": 0,
      "spo2": 0.94
    }
]
}

BASE_URL_IH = get_dotenv("BASE_URL_IH")
data_ih={
"pacientes": [
    {
        "id": 0,
        "vulnerabilidades": False,
        "spo2": 0.95, 
        "temperatura": 38, 
        "frequenciaRespiratoria": 13, 
        "sitioVulneravel": False
    }
]
}

NUMBER_OF_REQUESTS = 200  # Define o número de requisições a serem agendadas

for i in range(NUMBER_OF_REQUESTS):
    print("Agendando requisição " + str(i))
    # Função que será executada pela schedule
    schedule.every().second.do(run_threaded, requestJob, BASE_URL_CARDIO, 200, NUMBER_OF_REQUESTS, data_cardio)
    schedule.every().second.do(run_threaded, requestJob, BASE_URL_IRA, 200, NUMBER_OF_REQUESTS, data_ira)
    schedule.every().second.do(run_threaded, requestJob, BASE_URL_IH, 200, NUMBER_OF_REQUESTS, data_ih)

print("Iniciando o schedule")
# Loop infinito para executar a schedule
while True:
    schedule.run_pending()  # Executa as tarefas agendadas
    time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente

# run_threaded(requestJob, BASE_URL, 200, NUMBER_OF_REQUESTS, data)