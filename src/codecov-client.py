from collections import defaultdict
import json
import requests

CODECOV_ENDPOINT = "https://codecov.io/api/v2/github/codecov/{}"
TOKEN_NAME = "{{ ACCESS TOKEN }}"
CODECOV_HEADERS = {
    'Authorization': 'bearer {}'.format(TOKEN_NAME)
}

def _get_all_repos():
    print('Retrieving all repos...', end=" ")
    endpoint = CODECOV_ENDPOINT.format('repos?page_size=500')
    response = requests.get(
        endpoint,
        headers=CODECOV_HEADERS,
    )
    repos = json.loads(response.content)['results']
    print("Found {} repositories".format(len(repos)))
    return sorted(repo['name'] for repo in repos, key=str.casefold)
