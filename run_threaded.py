import threading


def run_threaded(job_func, *args, ):
        #visualizando numero da thread
        job_thread = threading.Thread(target=job_func , args=args)
        job_thread.start()