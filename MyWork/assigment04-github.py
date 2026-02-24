from github import Github, UnknownObjectException
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

try:
    # Try to get the file
    file = repo.get_contents(FILE_PATH, ref="main")
    content = file.decoded_content.decode("utf-8")
    updated_content = content.replace(OLD_TEXT, NEW_TEXT)

    # Update the file
    repo.update_file(
        path=FILE_PATH,
        message=COMMIT_MESSAGE,
        content=updated_content,
        sha=file.sha
    )
except UnknownObjectException:
    # File does not exist → create it
    updated_content = NEW_TEXT
    repo.create_file(
        path=FILE_PATH,
        message=COMMIT_MESSAGE,
        content=updated_content
    )

print("File updated and pushed on GitHub.")