import threading  # Importa o módulo "threading" para trabalhar com threads

def run_threaded(job_func, *args):
        # Visualizando número da thread
        job_thread = threading.Thread(target=job_func, args=args)  # Cria uma nova thread com a função "job_func" e os argumentos fornecidos
        job_thread.start()  # Inicia a execução da thread
