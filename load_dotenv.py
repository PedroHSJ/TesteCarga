import os
from dotenv import load_dotenv


def get_dotenv():
    try:
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Agora você pode usar as variáveis de ambiente como desejar
        return os.getenv("BASE_URL")  # Obtém o valor da variável de ambiente "BASE_URL"
    except Exception as e:
        print(e)