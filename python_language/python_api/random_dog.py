#!/usr/bin/python3

import requests

def get_random_dog_image():

    url_api = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url_api)

    if response.status_code == 200:
        dog_data = response.json()

        print("Random Dog Image:")
        print(dog_data['message'])

    else:
        print(f"Failed to fetch a random dog image. Status Code: {response.status_code}")

if __name__ == "__main__":
    get_random_dog_image()
