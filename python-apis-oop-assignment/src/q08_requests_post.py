# TODO:
# 1) POST https://jsonplaceholder.typicode.com/posts
#    body: {"title": "OOPs Assignment", "body": "Learning Python requests", "userId": 101}
# 2) Print status_code and response JSON (expect an "id" returned by the fake API).

import requests
import json

def main():
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json={
        "title": "OOPs Assignment",
        "body": "Learning Python requests",
        "userId": 101
    })
    print("Status Code:", response.status_code)
    if response.status_code == 201:
        print("Response JSON:", response.json())
    else:
        print("Failed to create post")

if __name__ == "__main__":
    main()
