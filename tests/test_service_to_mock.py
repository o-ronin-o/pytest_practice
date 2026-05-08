import pytest 
import src.service_to_mock as service 
import unittest.mock as mock 
import requests

@mock.patch("src.service_to_mock.get_user")
def test_get_user(mocked_get_user):
    mocked_get_user.return_value = "Mocked meow"
    user_name = service.get_user(2)
    assert user_name == "Mocked meow"

@mock.patch("requests.get")
def test_get_user_api(mocked_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200 
    mock_response.json.return_value = {"id": 1, "name": "memo"}
    mocked_get.return_value = mock_response
    data = service.get_user_api()
    assert data == {"id": 1, "name": "memo"}

@mock.patch("requests.get")

def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_user_api()



