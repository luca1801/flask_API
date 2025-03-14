# Instructions to create the code Environment

 # vscode config
 - config vscode to show files first over folder, go to settings.json and put on user profile: `"explorer.sortOrder": "filesFirst"`

 ## python, pipx, and poetry

- Add ***python***: install python
- Add ***pipx***( Install and Run Python Applications in Isolated Environments): `py -m install pipx`
> - This will ensure that the directory app is in you: `$PATH`: `pipx ensurepath `
>
> - Upgrade pipx: `py -m pip install --user --upgrade pipx`
>
> - See packages lists installed with pipx and what's available: `pipx list`
>
> - Documentação do ***pipx***: [https://pipx.pypa.io/stable/](https://pipx.pypa.io/stable/ 'Documentação')

- Add ***poetry*** : `pipx install poetry`
> - Create project with poetry: `poetry new poetry-demo`
>
> - The `pyproject.toml` file is what is the most important here. This will orchestrate your project and its dependencies
>
> - Poetry optional: put the environment virtual in your folder project:
>   - To see the config atual: `poetry config --list `
>
>   - Put virtualenvs.in-project true: `poetry config virtualenvs.in-project true`
>
> - Doc [https://python-poetry.org/](https://python-poetry.org/)

## GIT config

- First initiate the git of the project: `git init`
- add gh-cli to take github to the comand line:
> - Documentation download for windows  gh-cli [https://cli.github.com/](https://cli.github.com/) 
>
> - Run to authenticate with your Github account: `gh auth login` 
>
> - Create a new directory or push an existing local repository to github: `gh repo create`
- add library ignr.py for create automatically an ingnoring archive when push to github
> - documentation ignr.py [https://github.com/Antrikshy/ignr.py](https://github.com/Antrikshy/ignr.py)
>
> - install: `pipx install ignr`
>
> -  Create a ignr file: ignr -p python > .gitignore

# Change Branch of Commit

- To change the branch of a commit, you can use the following steps:
> - Checkout to the target branch: `git checkout target-branch`
> - Cherry-pick the commit: `git cherry-pick <commit-hash>`
> - Delete the commit from the original branch if necessary: `git checkout original-branch` and `git reset --hard HEAD~1`

# Clone Poetry Project from GitHub

- Clone the repository:
> - `git clone <repository-url>`
> - `cd <repository-name>`

- Install project dependencies:
> - Make sure you have Poetry installed: `pipx install poetry`
> - Install dependencies: `poetry install`
> - Activate virtual environment: `poetry shell`

## Pytest

- The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries. [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)
> - Install pytest but create e specfic group [DEV] in pyproject.toml: `poetry add --group dev pytest`
- add `pytest-cov`. This plugin produces coverage reports. 
> - install: `poetry add --group dev pytest-cov`
>
> - Doc: [https://pytest-cov.readthedocs.io/en/latest/readme.html](https://pytest-cov.readthedocs.io/en/latest/readme.html)

## Linter

- install `Blue` a code formatter to coding using PEP-08 guides.
> - install: `poetry add --group dev blue`
>
> Doc: [https://blue.readthedocs.io/en/latest/](https://blue.readthedocs.io/en/latest/)
- install `isort` for sort imports
> - install: `poetry add --group dev isort`
>
> - Doc: [https://pycqa.github.io/isort/](https://pycqa.github.io/isort/)

## Documentation

- `mkdocs` is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.
- We are using `mkdocs-material`, a powerful theme documentation framework on top of MkDocs
> - Install mkdocs-material but create e specfic group [DOC] in pyproject.toml: `poetry add --group doc mkdocs-material`
>
> - Doc: [https://squidfunk.github.io/mkdocs-material](https://squidfunk.github.io/mkdocs-material)
-  install `mkdocstrings` for Automatic documentation from sources using mkdocs
> - install: `poetry add --group doc mkdocstrings`
> - install version specific for python: `poetry add --group doc mkdocstrings-python`
>
> - Doc mkdocstrings: [https://mkdocstrings.github.io/](https://mkdocstrings.github.io/)
> - Doc mkdocstrings-python: [https://mkdocstrings.github.io/python/](https://mkdocstrings.github.io/python/)

# automate tasks

- `taskipy` define tasks in one file and run them with a simple command such as test, lint or publish.
> - install: `poetry add --group dev taskipy`
>
> - Doc: [https://github.com/taskipy/taskipy](https://github.com/taskipy/taskipy)

# Instructions to config the code environment

# Mkdocs
- Comands:
> * `mkdocs new [dir-name]` - Create a new project.
> * `mkdocs serve` - Start the live-reloading docs server.
> * `mkdocs build` - Build the documentation site.
> * `mkdocs -h` - Print help message and exit.
- edit mkdocs theme and put mkdocs-material
- adjust layout for the project

# pytest
- comand for see tasks: `task -l`
- add in `pyproject.toml` config for pytest and add doctest in parameters
> `[tool.pytest.ini_options]`\
  `pythonpath = "."`\
  `addopts = "--doctest-modules"`
- add taskpy comands for automate lint and mkdocs
- add comands for save file coverage html
- add comand for see coverage test
- final config
> `[tool.taskipy.tasks]`\
  `lint = "blue --check --diff . && isort --check -- diff ."`\
  `docs = "mkdocs serve"`\
  `pre_test = "task lint"`\
  `test = "pytest -s -x --cov=flask_api -vv"`\
  `post_test = "coverage html"`

# isort
- add in `pyproject.toml` config for isort
>`[tool.isort]`\
 `profile = "black"`\
 `line_length = 79`

 # Start Flask api

 ## install packages necessary
 - Flask: `poetry add flask`
 - Flask Restful: `poetry add flask-restful`
 - flask Migrate: `poetry add flask-migrate`
 - flask SQLAlchemy: `poetry add flask-sqlalchemy`
 - SQLAlchemy: `poetry add sqlalchemy`
 - sqlalchemy-utils: `poetry add sqlalchemy-utils`
 - client for comunicate with postgresql: `poetry add "psycopg[binary]"`
 - python-dotenv: `poetry add python-dotenv`
 - create a .flaskenv file and add comand for flask app execute: 
 `FLASK_APP=c:/Users/Lucas/Desktop/python/flask_API/src/run.py`

 ## flask migrate
 - Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. It allows you to manage database schema changes in a structured and version-controlled way.
 - In your Flask application, you need to initialize Flask-Migrate with your Flask app and SQLAlchemy database instance. Here’s an example of how to do this in your __init__.py file:
  > `from flask import Flask` \
    `from flask_sqlalchemy import SQLAlchemy`\
    `from flask_migrate import Migrate`\
    `from flask_restful import Api`\
    \
    `flask_api = Flask(__name__)`\
    `flask_api.config.from_object('config')  # Load configuration from config.py`\
    \
    `api = Api(flask_api)`\
    `db = SQLAlchemy(flask_api)`\
    `migrate = Migrate(flask_api, db)`\
    \
    `from .views import employers_views`\
    `from .models import employer_model`
- Create Migration Repository: `flask db init`
- This will create a migrations directory in your project.
- Generate an Initial Migration, To generate an initial migration script based on your current database schema, run: `flask db migrate -m "Initial migration"`
- This will create a new migration script in the versions directory.
- Apply the Migration, To apply the migration and update your database schema, run: `flask db upgrade`
- Making Changes to the Database Schema, Whenever you make changes to your SQLAlchemy models, you need to generate a new migration script and apply it.
> Summary of Commands
> - Initialize Migration Repository: `flask db init`
> - Generate Migration Script: `flask db migrate -m "Description"`
> - Apply Migration: `flask db upgrade`
> - Rollback Migration: `flask db downgrade`

## 8.3. Flask Marshmallow
- `Flask-Marshmallow` is an extension of Flask that integrates the Python Web Framework with the Marshmallow Objects serialization library.
> - Validates http request data
> - serialize application data to JSON
> - Makes data serialization more intuitive and easy to understand
> - Facilitates the creation of a complex database structure
- `Marshmallow` is a library for converting complex datatypes, such as objects, to and from native Python datatypes.
-`Flask-Marshmallow` it is a layer of integration between Flask and Marshmallow.

## 8.4. Schemas
- No Flask-Marshmallow, um "schema" é uma maneira de definir a estrutura de dados que você deseja serializar (converter de um objeto Python para um formato como JSON) ou desserializar (converter de um formato como JSON para um objeto Python). Schemas são usados para validar e transformar dados de entrada e saída.
- Conceitos Básicos de Schemas:
> 1. ***Serialização***: Converte objetos Python (como instâncias de modelos) em formatos como JSON para que possam ser enviados em respostas HTTP.
> 2. Desserialização: Converte dados de entrada (como JSON) em objetos Python, validando e transformando os dados conforme necessário.
> 3. Validação: verifica se os dados de entrada atendem a certos critérios antes de serem processados ou armazenados.
