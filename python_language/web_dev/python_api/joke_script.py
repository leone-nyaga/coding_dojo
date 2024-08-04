#!/usr/bin/python3

import requests

def get_programming_joke():

    api_url = "https://v2.jokeapi.dev/joke/Programming"

    response = requests.get(api_url)

    if response.status_code == 200:
        
        joke_Data = response.json()

        if joke_Data["type" ] == "twopart":
            print("Programming Joke:")
            print(f"Setup: {joke_data['setup']}")
            print(f"Delivery: {joke_data['delivery']}")
        else:
            print("Programming Joke:")
            print(joke_Data['joke'])

    else:
        print(f"Failed to fetch programming joke. Status Code: {response.status_code}")

if __name__ == "__main__":
    get_programming_joke()
