# TODO:
# 1) PUT https://jsonplaceholder.typicode.com/posts/1 with some updated JSON payload.
# 2) DELETE https://jsonplaceholder.typicode.com/posts/1
# 3) Print both status codes. Print JSON for PUT response.

import requests
import json

def do_put():
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json={
        "title": "Updated Title",
        "body": "Updated body content",
        "userId": 101
    })
    if response.status_code == 200:
        print("PUT Response JSON:", response.json())
    return response.status_code

def do_delete():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    return response.status_code

if __name__ == "__main__":
    print("PUT status:", do_put())
    print("DELETE status:", do_delete())
