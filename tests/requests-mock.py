import requests_mock

#

# Дополнительные тесты с использованием requests-mock

def test_get_pull_requests_empty_response():
    with requests_mock.Mocker() as m:
        m.get("https://api.github.com/repos/boto/boto3/pulls?state=open&per_page=100", json=[])
        result = get_pull_requests("open")
        assert result == []


#
def test_get_pull_requests_api_failure():
    with requests_mock.Mocker() as m:
        m.get("https://api.github.com/repos/boto/boto3/pulls", status_code=500)
        result = get_pull_requests("open")
        assert result == []
