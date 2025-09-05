# TODO:
# Implement fetch_data(url: str) that:
# - GETs the URL
# - Prints "Success" if 200
# - Prints "Client Error" if 400–499
# - Prints "Server Error" if 500–599
# - Else prints "Unexpected status code: <code>"
# - Handles exceptions (ConnectionError, Timeout) and prints a message.
# Test with:
#  - https://jsonplaceholder.typicode.com/posts/1  (should be 200)
#  - https://jsonplaceholder.typicode.com/invalid  (404)
#  - an obviously wrong URL like http://does-not-exist.example (should except)

import requests

def fetch_data(url: str) -> None:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Success")
        elif 400 <= response.status_code < 500:
            print("Client Error")
        elif 500 <= response.status_code < 600:
            print("Server Error")
        else:
            print(f"Unexpected status code: {response.status_code}")
    except requests.ConnectionError:
        print("Connection Error occurred.")
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # tests
    fetch_data("https://jsonplaceholder.typicode.com/posts/1")
    fetch_data("https://jsonplaceholder.typicode.com/invalid")
    fetch_data("http://does-not-exist.example")
