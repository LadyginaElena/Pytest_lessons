import pytest
import requests
import time

base_url = 'https://jsonplaceholder.typicode.com/'
url = 'https://playground.learnqa.ru/api/'

HTTP_code = 200


@pytest.mark.skip
def test_get_all_posts():
    response = requests.get(f'{base_url}posts')
    assert response.status_code == HTTP_code, 'Wrong status code'
    assert len(response.json()) == 100, 'actual length does not match to expected'


@pytest.mark.skip
def test_get_post1():
    response = requests.get(f'{base_url}posts/1')
    response_data = response.json()
    assert response.status_code == HTTP_code, 'Wrong status code'
    expected_keys = ['userId', 'id', 'title', 'body']
    for key in response_data.keys():
        assert key in expected_keys, 'Wrong keys'


@pytest.mark.skip
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


@pytest.mark.skip
def get_all_names():
    response = requests.get(f'{base_url}users/')
    response_data = response.json()
    name_list = []
    for i, name in enumerate(response_data):
        name_list.append((i + 1, response_data[i]['name']))
    return name_list


@pytest.mark.skip
@pytest.mark.parametrize('userid, expected_name', get_all_names())
def test_get_all_users_name(userid, expected_name):
    response = requests.get(f'{base_url}users/{userid}')
    response_data = response.json()
    assert response_data['name'] == expected_name, 'Wrong user name'


@pytest.mark.skip
def test_end_to_end():
    new_user = {
        'username': 'my user',
        'firstName': 'MyFirstname',
        'lastName': 'MyLastname',
        'email': str(time.time()) + '@example.com',
        'password': '12345'
    }
    response = requests.post(f'{url}user', data=new_user)
    assert response.status_code == HTTP_code, 'Wrong status code'
    response_data = response.json()
    assert 'id' in response_data.keys()
    user_id = response_data['id']

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == HTTP_code, 'Wrong status code'

    auth_data = {
        'email': new_user['email'],
        'password': '12345'
    }
    response = requests.post(f'{url}user/login', data=auth_data)
    assert response.status_code == HTTP_code, 'Wrong status code'
    token = response.headers['x-csrf-token']
    auth_sid = response.cookies['auth_sid']
    print(token, auth_sid)

    new_user_update = {
        'username': 'my_user_updated'
    }
    response = requests.put(f'{url}user/{user_id}',
                            data=new_user_update,
                            headers={'x-csrf-token': token},
                            cookies={'auth_sid': auth_sid})
    assert response.status_code == HTTP_code, 'Wrong status code'

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == HTTP_code, 'Wrong status code'
    response_data = response.json()
    assert 'my_user_updated' in response_data.values()

    response = requests.delete(f'{url}user/{user_id}',
                               headers={'x-csrf-token': token},
                               cookies={'auth_sid': auth_sid})

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == 404, 'Wrong status code'


@pytest.mark.skip
def test_get_all_albums():
    response = requests.get(f'{base_url}albums')
    assert response.status_code == HTTP_code, 'Wrong status code'
    assert len(response.json()) == 100, 'actual length does not match to expected'
    response_data = response.json()
    print(response_data)


@pytest.mark.skip
def test_album_in_albums():
    album_data = {
        'userId':'101',
        'id': '101',
        'title': 'my title'
    }
    response = requests.post(f'{base_url}albums', data=album_data)
    assert response.status_code == 201, 'Wrong status code'
    response_data = response.json()
    expected_title = 'my title'
    assert response_data['title'] == expected_title, 'Wrong title'


@pytest.mark.skip
def test_post_update_delete():
    post88_update = {
        'title': '88my title',
        'body': '88my body'
    }
    response = requests.put(f'{base_url}posts/88', data=post88_update)
    assert response.status_code == 200, 'Wrong status code'

    response = requests.delete(f'{base_url}posts/88')

    response = requests.get(f'{base_url}posts/88')
    print(response.json())


# simple methods
@pytest.mark.skip
def test_method_any():
    response = requests.get(f'{url}check_type')
    assert response.status_code == HTTP_code, 'Wrong status code'
    print(response.text)


@pytest.mark.skip
def test_return_status_code_500():
    response = requests.get(f'{url}get_500')
    assert response.status_code == 500, 'Wrong status code'


@pytest.mark.skip
@pytest.mark.xfail
def test_return_status_code_303():
    response = requests.get(f'{url}get_303')
    assert response.status_code == 303, 'Wrong status code'


@pytest.mark.skip
def test_return_text():
    response = requests.get(f'{url}get_text')
    assert response.status_code == HTTP_code, 'Wrong status code'
    response_data = response.text
    print(response_data)


@pytest.mark.skip
@pytest.mark.xfail
def test_return_200_for_post():
    response = requests.get(f'{url}method_post_only')
    assert response.status_code == 404, 'Wrong status code'
    response = requests.post(f'{url}method_post_only')
    assert response.status_code == 200, 'Wrong status code'


@pytest.mark.skip
def test_get_auth_cookie():
    auth_cookie = {'login': 'secret_login', 'password':'secret_pass'}
    response = requests.get(f'{url}get_auth_cookie', params=auth_cookie)
    assert response.status_code == HTTP_code, 'Wrong status code'
    response_data = response.text
    print(response_data)


@pytest.mark.skip
def test_return_map_api():
    response = requests.get(f'{url}map')
    assert response.status_code == HTTP_code, 'Wrong status code'
    response_data = response.text
    print(response_data)

