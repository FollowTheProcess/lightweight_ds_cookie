#! /usr/bin/env bash

# If GitHub cli used to create remote repo
# This script will create the local & remote repos, link the two together, and make an initial commit

{% if cookiecutter.use_gh_cli_to_create_repo == 'y' -%}

# Already at the root of the generated project, no need to cd anywhere

git init
git add -A
git commit -m "Initial Commit (Automated at Project Creation)"

gh repo create {{cookiecutter.project_slug}} --confirm --description "{{cookiecutter.description}}"

{% endif %}
