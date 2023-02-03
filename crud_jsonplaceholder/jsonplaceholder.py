import requests
import pytest


base_url = 'https://jsonplaceholder.typicode.com/posts'


@pytest.fixture(autouse=True, scope="module")
def change_data():  # функция, которая возвращает словарь dict
    return {}


def test_get_posts() -> object:
    r = requests.get(base_url)
    data = r.text
    with open("json-result.json", "w+") as f:
        f.write(f'test_get_posts response: \n{data}')


def test_post_post():
    user_data = {
        "userID": 11,
        "title": "2023 Post",
        "body": "Something interesting about 2023 year"
    }

    r = requests.post(base_url, user_data)
    data = r.text
    with open("json-result.json", "a") as f:
        f.write(f'\n\ntest_post_post response: \n{data}')


def test_put_post():
    new_url = f'{base_url}/2'
    new_data = {
        "title": "OneTwo"
    }
    r = requests.put(new_url, new_data)
    data = r.text
    with open("json-result.json", "a") as f:
        f.write(f'\n\ntest_put_post response: \n{data}')


def test_delete_post():
    delete_url = f'{base_url}/10'
    r = requests.delete(delete_url)
    data = r.text
    with open("json-result.json", "a") as f:
        f.write(f'\n\ntest_delete_post response: \n{data}')


def test_get_post():
    view_url = f'{base_url}/55'
    r = requests.get(view_url)
    data = r.text
    with open("json-result.json", "a") as f:
        f.write(f'\n\ntest_get_post 55 response: \n{data}')

