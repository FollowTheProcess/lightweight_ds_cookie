# {{cookiecutter.project_name}}

{{cookiecutter.description}}

{{cookiecutter.author_name}}, {% now 'utc', '%b %Y' %}

## Project Organisation

------------

    ├── LICENSE
    ├── README.md          <- Top level README (this document).
    ├── Docs               <- Project documentation, if required (mkdocs by default)
    ├── Data
    │   ├── Final          <- The final data sets for modelling.
    │   ├── Processed      <- Intermediate data that has been transformed or otherwise processed.
    │   └── Raw            <- The original, immutable data dump.
    │
    ├── Models             <- Trained and serialised models, model predictions, model summaries or mlflow data.
    │
    ├── Notebooks          <- Jupyter notebooks. Typically containing EDA or other exploratory content.
    │
    ├── Reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── Figures        <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yaml    <- The requirements file for reproducing the analysis environment,
    │                         generated with `conda env export > environment.yml
    │ 
    ├── makefile           <- Project level makefile. Run `make help` to see available commands
    │
    ├── setup.py           <- makes project pip installable `pip install -e .` so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── config.py      <- Top level project config file.
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                     predictions
    │   │
    │   └── visualisation  <- Scripts to create exploratory and results oriented visualizations
    │
    └── tests              <- Unit tests for src

<p><small>Project structure adapted from the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## High Level Summary

*A brief summary of the findings of the project and some of the key takeaways, some clear and concise figures to demonstrate any points you make*
