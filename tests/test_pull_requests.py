
import pytest
from handlers.pull_requests import get_pull_requests

from handlers.pull_requests import filter_pull_requests_by_title
#



# Дополнительные тесты в test_pull_requests.py

def test_filter_pull_requests_case_insensitive():
    mock_pull_requests = [
        {"title": "Add new feature", "num": 1, "link": "https://..."},
        {"title": "add new feature", "num": 2, "link": "https://..."}
    ]
    filtered_prs = filter_pull_requests_by_title(mock_pull_requests, "ADD")
    assert len(filtered_prs) == 2


#
def test_filter_pull_requests_by_title():
    mock_pull_requests = [
        {"title": "Add new feature", "num": 1, "link": "https://..."},
        {"title": "Fix bug", "num": 2, "link": "https://..."},
        {"title": "Update documentation", "num": 3, "link": "https://..."}
    ]

    # Фильтрация по ключевому слову "Add"
    filtered_prs = filter_pull_requests_by_title(mock_pull_requests, "Add")
    assert len(filtered_prs) == 1
    assert filtered_prs[0]["num"] == 1

    # Фильтрация по ключевому слову "documentation"
    filtered_prs = filter_pull_requests_by_title(mock_pull_requests, "documentation")
    assert len(filtered_prs) == 1
    assert filtered_prs[0]["num"] == 3

    # Фильтрация с ключевым словом, которого нет в заголовках
    filtered_prs = filter_pull_requests_by_title(mock_pull_requests, "Refactor")
    assert len(filtered_prs) == 0


def test_get_pull_requests():
    # Проверка на возвращаемый тип данных
    assert isinstance(get_pull_requests("open"), list)

    # Проверка на корректность структуры данных
    # (можно добавить больше детальных проверок, если необходимо)
    for pr in get_pull_requests("open"):
        assert "title" in pr
        assert "num" in pr
        assert "link" in pr

