# https://reqres.in/

import requests
from reqres.request import *


def test_list_users():
    r = requests.get('https://reqres.in/api/users?page=2')
    with open("response_body.txt", "w") as file:
        file.write("test_list_users response\n")
        file.write(r.text)
    assert r.status_code == 200


def test_single_user():
    r = requests.get('https://reqres.in/api/users/2')
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_single_users response:\n")
        file.write(r.text)
    assert r.status_code == 200


def test_single_user_not_found():
    r = requests.get('https://reqres.in/api/users/23')
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_single_user_not_found response:\n")
        file.write(r.text)
    assert r.status_code == 404


def test_list_resource():
    r = requests.get('https://reqres.in/api/unknown')
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_list_resource response:\n")
        file.write(r.text)
    assert r.status_code == 200


def test_single_resource():
    r = requests.get('https://reqres.in/api/unknown/2')
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_single_resource response:\n")
        file.write(r.text)
    assert r.status_code == 200


def test_single_resource_not_found():
    r = requests.get('https://reqres.in/api/unknown/23')
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_single_resource_not_found response:\n")
        file.write(r.text)
    assert r.status_code == 404


def test_create():
    r = requests.post('https://reqres.in/api/users', data=user)
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_post response:\n")
        file.write(r.text)
    assert r.status_code == 200 or 201


def test_update():
    r = requests.put('https://reqres.in/api/users/2', data=user_update)
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_update response:\n")
        file.write(r.text)
    assert r.status_code == 200


def test_delete():
    r = requests.delete('https://reqres.in/api/users/2')
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_delete response:\n")
        file.write(r.text)
    assert r.status_code == 204


def test_register():
    r = requests.post('https://reqres.in/api/register', data=register)
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_register response:\n")
        file.write(r.text)
    assert r.status_code == 200


def test_register_unsuccessful():
    r = requests.post('https://reqres.in/api/register', data=register_unsuccessful)
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_register_unsuccessful response:\n")
        file.write(r.text)
    assert r.status_code == 400


def test_login():
    r = requests.post('https://reqres.in/api/login', data=login)
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_login response:\n")
        file.write(r.text)
    assert r.status_code == 200


def test_login_unsuccessful():
    r = requests.post('https://reqres.in/api/login', data=login_unsuccessful)
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_login_unsuccessful response:\n")
        file.write(r.text)
    assert r.status_code == 400


def test_login_unsuccessful():
    r = requests.post('https://reqres.in/api/login', data=login_unsuccessful)
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_login_unsuccessful response:\n")
        file.write(r.text)
    assert r.status_code == 400


def test_delayed():
    r = requests.get('https://reqres.in/api/users?delay=3')
    with open("response_body.txt", "a") as file:
        file.write("\n\ntest_delayed response:\n")
        file.write(r.text)
    assert r.status_code == 200















