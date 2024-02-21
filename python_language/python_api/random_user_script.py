#!/usr/bin/python3

import requests

def get_random_user_info():

    api_url = "https://randomuser.me/api/"

    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json()["results"][0]

        print("User Information:")
        print(f"Name: {user_data['name']['first']} {user_data['name']['last']}")
        print(f"Email: {user_data['email']}")
        print(f"Date of Birth: {user_data['dob']['date']}")

    else:
        print(f"Failed to fetch user information. Status Code: {response.status_code}")

if __name__ == "__main__":
    get_random_user_info()
