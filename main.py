import time  # Importa o módulo "time" para trabalhar com tempo
import schedule  # Importa o módulo "schedule" para agendamento de tarefas
from dotenv import load_dotenv  # Importa a função "load_dotenv" do módulo "dotenv" para carregar as variáveis de ambiente
import os  # Importa o módulo "os" para trabalhar com variáveis de ambiente
from run_threaded import run_threaded  # Importa a função "run_threaded" do módulo "run_threaded"
from main_requests import requestJob  # Importa a função "requestJob" do módulo "main_requests"

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode usar as variáveis de ambiente como desejar
BASE_URL = os.getenv("BASE_URL")  # Obtém o valor da variável de ambiente "BASE_URL"
NUMBER_OF_REQUESTS = 10  # Define o número de requisições a serem agendadas

for i in range(NUMBER_OF_REQUESTS):
    print("Agendando requisição " + str(i))
    # Função que será executada pela schedule
    schedule.every().minute.do(run_threaded, requestJob, BASE_URL, 200)

print("Iniciando o schedule")
# Loop infinito para executar a schedule
while True:
    schedule.run_pending()  # Executa as tarefas agendadas
    time.sleep(1)  # Aguarda 1 segundo antes de verificar novamente
