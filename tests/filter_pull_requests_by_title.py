#

# Дополнительные тесты для filter_pull_requests_by_title.py

def test_filter_pull_requests_no_match():
    mock_pull_requests = [
        {"title": "Add new feature", "num": 1, "link": "https://..."},
        {"title": "Fix bug", "num": 2, "link": "https://..."}
    ]
    filtered_prs = filter_pull_requests_by_title(mock_pull_requests, "Non-existent")
    assert len(filtered_prs) == 0


#


def test_filter_pull_requests_by_empty_title():
    mock_pull_requests = [
        {"title": "Add new feature", "num": 1, "link": "https://..."},
        {"title": "", "num": 2, "link": "https://..."}
    ]
    filtered_prs = filter_pull_requests_by_title(mock_pull_requests, "")
    assert len(filtered_prs) == 1
    assert filtered_prs[0]["num"] == 2

def test_filter_pull_requests_by_title_case_insensitive():
    mock_pull_requests = [
        {"title": "Add new feature", "num": 1, "link": "https://..."},
        {"title": "fix bug", "num": 2, "link": "https://..."}
    ]
    filtered_prs = filter_pull_requests_by_title(mock_pull_requests, "FIX")
    assert len(filtered_prs) == 1
    assert filtered_prs[0]["num"] == 2
