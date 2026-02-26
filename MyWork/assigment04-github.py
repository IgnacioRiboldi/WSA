from github import Github
from config import config as cfg

REPO_NAME = "IgnacioRiboldi/WSA"
FILE_PATH = "MyWork/test.txt"
OLD_TEXT = "Andrew"
NEW_TEXT = "Ignacio"
COMMIT_MESSAGE = "Replace Andrew with Ignacio"

g = Github(cfg["token"])
repo = g.get_repo(REPO_NAME)
print("Repo permissions:", repo.permissions)

file = repo.get_contents(FILE_PATH, ref=repo.default_branch)
content = file.decoded_content.decode("utf-8")

updated_content = content.replace(OLD_TEXT, NEW_TEXT)

repo.update_file(
    path=file.path,
    message=COMMIT_MESSAGE,
    content=updated_content,
    sha=file.sha,
    branch=repo.default_branch
)

print("File updated and pushed on GitHub.")