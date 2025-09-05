# TODO:
# Build a tiny CLI:
# Usage:
#   python q12_cli_http_client.py GET https://jsonplaceholder.typicode.com/posts/1
#   python q12_cli_http_client.py POST https://jsonplaceholder.typicode.com/posts '{"title":"x","body":"y","userId":1}'
# Requirements:
# - Accept method in {GET, POST, PUT, DELETE}
# - Optional JSON body for POST/PUT (as a raw JSON string argument)
# - Print status code and JSON (if any) or text.
# - Handle invalid method and JSON errors gracefully.

import sys
import json
import requests

def main(argv):
    if len(argv) < 2:
        print("Usage: python q12_cli_http_client.py <METHOD> <URL> [JSON_BODY]")
        return

    method = argv[0].upper()
    url = argv[1]
    json_body = None
    if len(argv) == 3:
        try:
            json_body = json.loads(argv[2])
        except json.JSONDecodeError:
            print("Invalid JSON body.")
            return

    if method == "GET":
        response = requests.get(url)
    elif method == "POST":
        response = requests.post(url, json=json_body)
    elif method == "PUT":
        response = requests.put(url, json=json_body)
    elif method == "DELETE":
        response = requests.delete(url)
    else:
        print("Invalid HTTP method.")
        return

    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except json.JSONDecodeError:
        print("Response Text:", response.text)

if __name__ == "__main__":
    main(sys.argv[1:])