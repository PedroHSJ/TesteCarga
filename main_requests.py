import requests

def requestJob(url: str, status_code_expected: int):
    try:
        print("Requesting...")
        print("URL: " + url)     
        response = requests.get(url)
        if(response.status_code == status_code_expected):
            print("Request OK")
        else:
            print("Request failed")
    except Exception as e:
        print(e)
        return False
        