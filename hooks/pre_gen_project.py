#!/usr/bin/env python3

# Python script to create the Github repo for this project using PyGithub

# Runs as a pre project generation hook in cookiecutter

import os

from dotenv import load_dotenv
from github import Github

# Load .env file to source API key & other info
dotenv_path = os.path.join(os.path.expanduser("~"), ".env")

# Source the .env file
load_dotenv(dotenv_path)

# Github API access token
token = os.getenv("TOKEN")

repo_name = "{{cookiecutter.repo_name}}"


def make_github_repo():
    """
    Uses the github API and PyGithub to automatically create a remote repo based on
    {{cookiecutter.repo_name}}.

    Requires a .env file in home directory containing the following:

    TOKEN="<your github api access token>"

    Also requires python-dotenv and PyGithub.
    """
    try:
        user = Github(login_or_token=token).get_user()
        user.create_repo(repo_name)

    except Exception as e:
        print(e)

    else:
        print(f"Successfully created Github repo: {repo_name}")


if __name__ == "__main__":
    make_github_repo()
