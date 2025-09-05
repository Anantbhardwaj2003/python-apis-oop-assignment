# TODO:
# 1) GET https://jsonplaceholder.typicode.com/posts/1
# 2) Print the response JSON and specifically print the "title" field.

import requests

def main():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        data = response.json()
        print("Response JSON:", data)
        print("Title:", data.get("title", "No Title Found"))
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    main()
