import requests
import os
import logging

# Настройка базового логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'token {TOKEN}'}

def filter_pull_requests_by_title(pull_requests, title_keyword):
    """
    Фильтрует список pull request'ов по ключевому слову в заголовке.
    """
    logger.info(f"Filtering {len(pull_requests)} pull requests by title keyword '{title_keyword}'")
    filtered = [pr for pr in pull_requests if title_keyword.lower() in pr["title"].lower()]
    logger.debug(f"Found {len(filtered)} pull requests after filtering")
    return filtered

def get_pull_requests(state):
    """
    Получает список pull request'ов из репозитория boto/boto3 на GitHub.
    """
    url = f"https://api.github.com/repos/boto/boto3/pulls?state={state}&per_page=100"
    logger.info(f"Fetching pull requests from GitHub with state '{state}'")
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        pull_requests = [{
            "title": pr["title"],
            "num": pr["number"],
            "link": pr["html_url"]
        } for pr in response.json()]
        logger.info(f"Retrieved {len(pull_requests)} pull requests")
        return pull_requests
    else:
        logger.error(f"Failed to fetch data from GitHub API: Status {response.status_code}")
        return []
