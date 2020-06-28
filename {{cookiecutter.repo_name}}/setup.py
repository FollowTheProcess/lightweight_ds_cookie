from os import path

from setuptools import find_packages, setup

# Define project root folder for later refs
ROOT = path.abspath(path.dirname(__file__))

# Read in the README.md to form the long description
with open(path.join(ROOT, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    packages=find_packages(),
    version="0.1.0",
    description="{{cookiecutter.description}}",
    author="{{cookiecutter.author_name}}",
    license="{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
