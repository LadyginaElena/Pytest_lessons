import pytest
import requests

base_url = 'https://jsonplaceholder.typicode.com/'
url = 'https://playground.learnqa.ru/api/'

HTTP_code = 200

def test_get_all_posts():
    response = requests.get(f'{base_url}posts')
    assert response.status_code == HTTP_code, 'Wrong status code'
    assert len(response.json()) == 100, 'actual length does not match to expected'

def test_get_post1():
    response = requests.get(f'{base_url}posts/1')
    response_data = response.json()
    assert response.status_code == HTTP_code, 'Wrong status code'
    expected_keys = ['userId', 'id', 'title', 'body']
    for key in response_data.keys():
        assert key in expected_keys, 'Wrong keys'

def test_post_in_posts():
    post_data = {
              'id': 101,
           'title': 'my title',
            'body': 'my body'
    }
    response = requests.post(f'{base_url}posts', data=post_data)
    assert response.status_code == 201, 'Wrong status code'
    response_data = response.json()
    expected_title = 'my title'
    assert response_data['title'] == expected_title, 'Wrong title'

def get_all_names():
    response = requests.get(f'{base_url}users/')
    response_data = response.json()
    name_list =[]
    for i, name in enumerate(response_data):
        name_list.append((i+1, response_data[i]['name']))
    return name_list