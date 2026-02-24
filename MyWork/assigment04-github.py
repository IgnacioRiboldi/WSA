
from github import Github
from config import config as cfg

# Configuration
REPO_NAME = "IgnacioRiboldi/WSA"
FILE_PATH = "MyWork/test.txt"
OLD_TEXT = "Andrew"
NEW_TEXT = "Ignacio"
COMMIT_MESSAGE = "Replace Andrew with Ignacio"

# Authenticate with GitHub
g = Github(cfg["token"])

# Get the repository
repo = g.get_repo(REPO_NAME)

# Get the file
file = repo.get_contents(FILE_PATH)
content = file.decoded_content.decode("utf-8")

# Replace text
updated_content = content.replace(OLD_TEXT, NEW_TEXT)

# Update the file in the repository
repo.update_file(
    path=FILE_PATH,
    message=COMMIT_MESSAGE,
    content=updated_content,
    sha=file.sha
)

print("File updated and pushed using GitHub API.")