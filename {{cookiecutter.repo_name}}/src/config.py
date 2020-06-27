"""
Top level config file for the project. Contains things like key project directories, data dtypes etc.

Author: {{cookiecutter.author_name}} 
Created: {% now 'utc', '%d/%m/%Y' %}
"""

from pathlib import Path

# Key project directories, avoids repetition in other files
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = PROJECT_ROOT / "Data" / "Raw"
PROCESSED_DATA = PROJECT_ROOT / "Data" / "Processed"
FINAL_DATA = PROJECT_ROOT / "Data" / "Final"
