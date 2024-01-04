import requests_mock

#

# Дополнительные тесты для get_pull_requests.py

def test_get_pull_requests_invalid_state():
    with requests_mock.Mocker() as m:
        m.get("https://api.github.com/repos/boto/boto3/pulls?state=invalid&per_page=100", status_code=400)
        result = get_pull_requests("invalid")
        assert result == []


#



def test_get_pull_requests_api_failure():
    with requests_mock.Mocker() as m:
        m.get("https://api.github.com/repos/boto/boto3/pulls?state=closed&per_page=100", status_code=500)
        result = get_pull_requests("closed")
        assert result == []

def test_get_pull_requests_structure():
    mock_response = [
        {"title": "PR 1", "number": 1, "html_url": "https://github.com/boto/boto3/pull/1"},
        {"title": "PR 2", "number": 2, "html_url": "https://github.com/boto/boto3/pull/2"}
    ]

    with requests_mock.Mocker() as m:
        m.get("https://api.github.com/repos/boto/boto3/pulls?state=open&per_page=100", json=mock_response)
        result = get_pull_requests("open")

        assert all(isinstance(pr, dict) for pr in result)
        assert all("title" in pr and "num" in pr and "link" in pr for pr in result)
