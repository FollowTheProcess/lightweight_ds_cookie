# Lightweight Data Science Project Template

This is a lighter weight version of the [cookiecutter-data-science template](https://github.com/drivendata/cookiecutter-data-science) I created mainly for personal use and convenience on DS projects. However, anyone is free to use this.

This version will run pre and post generation scripts in python and bash, it should work by default on MacOS if you follow the instructions. Windows most likely won't like it!

## Changes from the Original

* Simplified Makefile
* Changed Sphinx docs to [mkdocs](https://www.mkdocs.org) and [mkapi](https://github.com/daizutabi/mkapi/) plugin for simplicity and easier markdown support
* Removed tox.ini as the only thing in there in original was flake8 config
* Changed requirements.txt to environment.yaml for conda support
* Added pre and post generation hooks that handle the creation and syncing of a git/github repo as well as the creation of a conda environment
* Added support for pre-commit hooks

## Instructions

First ensure cookiecutter is installed (or updated with -U) and install other dependencies

``` shell
 pip install -U cookiecutter python-dotenv PyGithub
 ```

 *Note: You will also need the [Anaconda Distribution](https://www.anaconda.com/products/individual) installed*

In order for the pre and post generation hook scripts to work correctly, ensure you do following:

* Create a .env file in your home directory

``` shell
# cd to your home directory
cd

# Create a .env file
touch .env
```

* Open the .env file in a text editor and add the following information:

``` shell
# Note the slash at the end of FILEPATH, thats there on purpose!

FILEPATH="<your_absolute_path_to_where_you_put_python_projects>/"
TOKEN="<your_github_api_access_token>"
```

You can find out how to get a Github API access token [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

* Navigate to directory you want your project to be created in

``` shell
cd <your_absolute_path_to_where_you_put_python_projects>
```

* Use cookiecutter

``` shell
cookiecutter https://github.com/FollowTheProcess/lightweight_ds_cookie.git
```

You will then be asked a series of questions, following which your project will be created, a remote github repo will be created with the same name, and a local git repo will be initialised and linked up the github repo.
