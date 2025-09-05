# Python OOP and APIs Assignment

This repository contains a series of Python scripts designed as an assignment to practice **Object-Oriented Programming (OOP)** concepts and how to interact with **web APIs** using the `requests` library.

---

## 📂 Directory Structure

python-apis-oop-assignment/
├─ src/ # Contains all the assignment solution scripts
├─ tests/ # Contains optional smoke tests
├─ requirements.txt # Project dependencies
└─ README.md # Instructions and project overview

---

## ✅ Prerequisites
- Python **3.8** or newer  
- `pip` for package installation  

---

## ⚙️ Setup and Installation
Clone the repository (if applicable):

```bash
git clone <repository-url>
cd python-apis-oop-assignment
```

## How to Run the Scripts
```bash
All assignment scripts are located in the src/ directory and can be run directly from the root of the project folder.

The general command format is:

python src/<script_name>.py

Examples
To run the basic OOP script:

python src/q01_oop_book_basics.py

To run the requests GET example:

python src/q06_requests_get.py

To run the CLI HTTP client:
This script accepts command-line arguments.

```

# Example GET request
```bash
python src/q12_cli_http_client.py --method GET --url [https://jsonplaceholder.typicode.com/posts/1](https://jsonplaceholder.typicode.com/posts/1)

# Example POST request
python src/q12_cli_http_client.py --method POST --url [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts) --data '{"title": "foo", "body": "bar", "userId": 1}'
```

## Running Tests (Optional)
```bash
Simple smoke tests are provided to perform basic checks. You can run them with the following command:

python tests/smoke_tests.py

File Descriptions
Object-Oriented Programming (src/q01 to src/q05)
q01_oop_book_basics.py: Implements a basic Book class.

q02_oop_encapsulation.py: Demonstrates encapsulation with private attributes and getter/setter methods.

q03_oop_inheritance.py: Shows inheritance by creating specialized book classes.

q04_oop_polymorphism.py: Illustrates polymorphism through a common interface.

q05_oop_all_in_one.py: A comprehensive task combining all the above OOP principles.

APIs and requests Library (src/q06 to src/q12)
q06_requests_get.py: Performs a simple HTTP GET request.

q07_requests_get_params.py: Performs a GET request with URL parameters.

q08_requests_post.py: Performs an HTTP POST request with a data payload.

q09_requests_put_delete.py: Demonstrates HTTP PUT and DELETE requests.

q10_http_status_classifier.py: A function to classify HTTP status codes.

q11_fetch_with_status_handling.py: Fetches a URL and handles the response based on the status code.

q12_cli_http_client.py: A command-line tool for making basic HTTP requests.

```
