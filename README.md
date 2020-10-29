# Lightweight Data Science Project Template

This is a lighter weight version of the [cookiecutter-data-science template](https://github.com/drivendata/cookiecutter-data-science) I created mainly for personal use and convenience on DS projects. However, anyone is free to use this.

This version has been tested and MacOS and Linux but not Windows. It should work though, the only thing that may not are some of the invoke terminal commands.

## Changes from the Original

* Changed makefile to [Invoke][Invoke]
* Removed Docs, most individual level data projects don't require Docs. Focus here is on results based markdown reports and Notebooks
* Removed tox.ini, functionality moved to invoke tasks
* Changed requirements.txt to environment.yml for conda support, more appropriate to data science

## Instructions

First ensure cookiecutter is installed:

In a conda env:

``` shell
conda install -c conda-forge cookiecutter
 ```

Using pip:

``` shell
pip install cookiecutter
```

Homebrew:

``` shell
brew install cookiecutter
```

 *Note: You will also need the [Anaconda Distribution][anaconda] or [Miniconda][miniconda] installed*

* Navigate to directory you want your project to be created in

``` shell
cd <your_absolute_path_to_where_you_put_python_projects>
```

* Use cookiecutter

``` shell
cookiecutter https://github.com/FollowTheProcess/lightweight_ds_cookie.git
```

You will then be asked a series of questions, following which cookiecutter will create your project directory structure.

### Environment Creation

In the project root there is an environment.yml file with some initial common dependencies included for you. The name of the environment will be filled out for you by cookiecutter with the name of your project.

Add any packages you think you may need under the 'dependencies' section of the environment.yml file like so...

``` yaml
name: <your_project_name>
channels:
 - defaults
 - conda-forge
dependencies:
 - python>=3.7
 - black
 - flake8
 - <your_dependency_1>
 - <your_dependency_2>
 - etc.
```

After adding the dependencies, run the following command in the terminal (ensure you have cd'd to the project root)

``` shell
conda env create --file environment.yml
```

This will create the environment you specified.

You can of course add to the environment using the typical

``` shell
conda install <package>
```

But I recommend adding it to the environment.yml afterwards. This way, the environment can be generated cross-platform if required.

<p><small> I have also included a top level environment.yml so you can replicate the exact environment this template was made in, incase anything doesn't work</small></p>

[Invoke]: https://www.pyinvoke.org
[Anaconda]: https://www.anaconda.com/products/individual
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
