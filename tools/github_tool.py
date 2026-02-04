import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def search_repositories(query="python", limit=3):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    repos = response.json()["items"][:limit]

    return [
        {
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "url": repo["html_url"],
            "description": repo["description"]
        }
        for repo in repos
    ]
