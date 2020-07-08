# pyutils

Python utility scripts

[![CircleCI](https://circleci.com/gh/mikemadden42/pyutils.svg?style=svg)](https://circleci.com/gh/mikemadden42/pyutils)

## Prerequisites

These scripts rely on the a few external libraries.

Install these with pip:

```bash
pip install --upgrade Jinja2 PyYAML boto boto3 nested_dict nose psutil pynput pytest python-dateutil requests simplejson six slacker
```

## Linters

Format & lint these scripts:

```bash
pip install --upgrade black flake8 pylint
```

```bash
flake8 FILE.py
pylint FILE.py
black FILE.py
```

Install all the needed libraries and tools:

```bash
pip install -r requirements.txt
```

