import requests
from HW4.request_body import *


def test_get():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    with open("response_body.txt", "w") as file:
        file.write("'test_get' response body:\n\n")
        file.write(r.text)
    assert r.status_code == 200


def test_post():
    r = requests.post('https://jsonplaceholder.typicode.com/posts', data=user)
    with open("response_body.txt", "a") as file:
        file.write("\n\n'test_post' response body:\n\n")
        file.write(r.text)
    assert r.status_code == 201


def test_patch():
    r = requests.patch('https://jsonplaceholder.typicode.com/posts/2', data=user_edit)
    with open("response_body.txt", "a") as file:
        file.write("\n\n'test_patch' response body:\n\n")
        file.write(r.text)
    assert r.status_code == 200


def test_delete():
    r = requests.delete('https://jsonplaceholder.typicode.com/posts/10')
    with open("response_body.txt", "a") as file:
        file.write("\n\n'test_delete' response body:\n\n")
        file.write(r.text)
    assert r.status_code == 200
