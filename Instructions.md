 # Instructions to create the code Environment

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
-
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