# TODO:
# 1) GET https://jsonplaceholder.typicode.com/comments with params: postId=1
# 2) Print the length of results and print first 2 items (pretty as JSON).

import requests
import json

def main():
    response = requests.get("https://jsonplaceholder.typicode.com/comments", params={"postId": 1})
    if response.status_code == 200:
        data = response.json()
        print("Number of comments:", len(data))
        print("First 2 comments:")
        for comment in data[:2]:
            print(json.dumps(comment, indent=4))
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    main()
