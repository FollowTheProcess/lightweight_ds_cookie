#!/bin/bash

# Shell script to handle the creation of a local git repo
# and it's connection to the remote Github repo handled by pre_gen_project.py

# Runs as a post project generation hook in cookiecutter

# Requires .env file in home dir containing GHUB=<your_github_url/>
# Note the slash at the end, important

# Source the same .env file as pre_gen_project.py
source ~/.env

# Navigate to python projects directory
cd $FILEPATH

# Navigate to the directory created by cookiecutter
cd "{{cookiecutter.repo_name}}"

# Create a conda env and install basic requirements
# Because this is a data science cookiecutter, we can install common packages
yes | conda create --name "{{cookiecutter.repo_name}}" python=3 black flake8 pytest numpy pandas

# Export an environment.yml
conda env export --name "{{cookiecutter.repo_name}}" > environment.yml

# Do git stuff
git init
git remote add origin "{{cookiecutter.repo_url}}".git
git add -A
git commit -m "Initial Commit (Automated)"
git push -u origin master

# Open vscode in the project root
code .
