Contributing to Matrix
======================

## Python3.7 or higer

Matrix dependes on Python3.7 or higher

Install python3.7:

- use [pyenv](https://github.com/pyenv/pyenv)
- in ubuntu, see [wiki](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/)

## Create virtualenv by `poetry`

Install `poetry`

```shell
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

Use python3.7 virtualenv

```shell
poetry env use python3.7
poetry install
poetry shell
```

## Pre-commit, include lint and unit test

Install hooks

```shell
$ pre-commit install && pre-commit install-hooks
```

## Merge requests are always welcome

First, make sure you have latest code (in `dev` branch usually)

```shell
$ git fetch origin
```

Second, ceate a feature branch

```shell
$ git checkout -b feature-xxx
```

Then, add your feature code and commit, this step will run lint and pytest auto

```shell
$ git add -A && git commit -m 'message'
```

Submit your feature branch

```shell
$ git push -u origin feature-xxx
```

At last, create a [merge reuqest](https://code.infervision.com/backend/matrix/merge_requests/new) in GitLab UI, please write how down the key steps of how this feature is implemented, and post some screenshots of the operation

