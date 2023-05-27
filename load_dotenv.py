import os
from dotenv import load_dotenv


def get_dotenv(env_path=None):
    try:
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Agora você pode usar as variáveis de ambiente como desejar
        return os.getenv(env_path)  # Obtém o valor da variável de ambiente "BASE_URL"
    except Exception as e:
        print(e)