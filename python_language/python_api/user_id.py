import requests

def ask_user_id():

    api_url = "https://jsonplaceholder.typicode.com/todos/1"

    response = requests.get(api_url)

    if response.status_code == 200:

