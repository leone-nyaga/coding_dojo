#!/usr/bin/python3

import requests

def get_user_info(user_id):

    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = requests.get(api_url)

    if response.status_code == 200:

        user_data = response.json()

        print(f"User Information for User ID {user_id}:")
        print(f"Name: {user_data['name']}")
        print(f"Username: {user_data['username']}")
        print(f"Email: {user_data['email']}")
        print(f"Address: {user_data['address']['city']}, {user_data['address']['street']}")
        print(f"Phone: {user_data['phone']}")

    else:
        print(f"Failed to fetch user information for User ID {user_id}. Status Code: {response.status_code}")

if __name__ == "__main__":

    user_id = input("Enter a User ID: ")
    get_user_info(user_id)
