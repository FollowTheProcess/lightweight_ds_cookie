# Lightweight Data Science Project Template

This is a lighter weight version of the [cookiecutter-data-science template](https://github.com/drivendata/cookiecutter-data-science) I created mainly for personal use and convenience on DS projects. However, anyone is free to use this.

This version has been tested and MacOS and Linux but not Windows. The only thing that may not work is the makefile.

## Changes from the Original

* Simplified Makefile
* Changed Sphinx docs to [mkdocs](https://www.mkdocs.org) and [mkapi](https://github.com/daizutabi/mkapi/) plugin for simplicity and easier markdown support
* Removed tox.ini as the only thing in there in original was flake8 config
* Changed requirements.txt to environment.yml for conda support
* Added support for pre-commit hooks

## Instructions

First ensure cookiecutter is installed (or updated with -U)

``` shell
 pip install -U cookiecutter
 ```

 *Note: You will also need the [Anaconda Distribution](https://www.anaconda.com/products/individual) installed*

* Navigate to directory you want your project to be created in

``` shell
cd <your_absolute_path_to_where_you_put_python_projects>
```

* Use cookiecutter

``` shell
cookiecutter https://github.com/FollowTheProcess/lightweight_ds_cookie.git
```

You will then be asked a series of questions, following which cookiecutter will create

1) Your project directory structure using the name provided

2) A conda environment with python3, some dev requirements, pandas and numpy and the same name

<p><small> I have also included a top level environment.yml so you can replicate the exact environment this template was made in, incase anything doesn't work</small></p>
