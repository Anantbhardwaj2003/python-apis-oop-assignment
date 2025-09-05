# TODO:
# Implement classify_status(code: int) -> str
# Returns: "Success" (2xx), "Created" (201 only), "Client Error" (4xx), "Server Error" (5xx), else "Other"
# Print classification for: 200, 201, 400, 401, 403, 404, 500, 502, 503

def classify_status(code: int) -> str:
    if 200 <= code < 300:
        return "Success"
    elif code == 201:
        return "Created"
    elif 400 <= code < 500:
        return "Client Error"
    elif 500 <= code < 600:
        return "Server Error"
    else:
        return "Other"

if __name__ == "__main__":
    codes = [200, 201, 400, 401, 403, 404, 500, 502, 503]
    for c in codes:
        print(c, "->", classify_status(c))
