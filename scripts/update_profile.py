import os
import requests

USERNAME = "hasanRAZU"
README = "README.md"

headers = {
    "Accept": "application/vnd.github+json"
}

url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"

repos = requests.get(url, headers=headers).json()

repos = [
    repo for repo in repos
    if repo["name"].lower() != USERNAME.lower()
    and not repo["fork"]
]

projects = "## 🚀 Projects\n\n"
projects += "<!-- PROJECTS:START -->\n\n"

for repo in repos:
    name = repo["name"]
    description = repo["description"] or "No description available."
    html_url = repo["html_url"]
    language = repo["language"] or "N/A"
    stars = repo["stargazers_count"]

    projects += f"""### [{name}]({html_url})

{description}

**Language:** {language} | **Stars:** ⭐ {stars}

"""

projects += "<!-- PROJECTS:END -->"

with open(README, "r", encoding="utf-8") as file:
    readme = file.read()

start = "<!-- PROJECTS:START -->"
end = "<!-- PROJECTS:END -->"

start_index = readme.index(start)
end_index = readme.index(end) + len(end)

new_readme = (
    readme[:start_index]
    + projects
    + readme[end_index:]
)

with open(README, "w", encoding="utf-8") as file:
    file.write(new_readme)

print("Projects updated successfully.")
