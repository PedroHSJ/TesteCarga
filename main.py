import time
import schedule
from dotenv import load_dotenv
import os
from run_threaded import run_threaded
from main_requests import requestJob

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode usar as variáveis de ambiente como desejar
BASE_URL = os.getenv("BASE_URL")
NUMBER_OF_REQUESTS = 10
for i in range(NUMBER_OF_REQUESTS):
    print("Agendando requisicao " + str(i))
    # Função que será executada pela schedule
    schedule.every().minute.do(run_threaded, requestJob, BASE_URL, 200)

print("Iniciando o schedule")
# Loop infinito para executar a schedule
while True:
    schedule.run_pending()
    time.sleep(1)