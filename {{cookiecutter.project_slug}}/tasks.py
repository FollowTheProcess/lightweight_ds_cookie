"""
Invoke tasks for easy project automation.
"""

from pathlib import Path

from invoke import task

PROJECT_ROOT = Path(__file__).parent.resolve()


@task
def clean(c):
    """
    Recursively removes cache files and other clutter from the project.
    """
    c.run('find . -name "__pycache__" -exec rm -rf {} +')
    c.run('find . -name ".pytest_cache" -exec rm -rf {} +')
    c.run('find . -name ".mypy_cache" -exec rm -rf {} +')
    c.run('find . -name ".ipynb_checkpoints" -exec rm -rf {} +')


@task
def style(c):
    """
    Runs style checking and linting tools on the project.
    """
    c.run("isort .")
    c.run("flake8")
    c.run("black .")
    c.run("mypy .")


@task
def test(c):
    """
    Runs the test suite.
    """
    c.run("pytest")
