# pyutils
Python utility scripts

## Prerequisites
These scripts rely on the a few external libraries.

To install these with pip:

```bash
$ pip install --upgrade Jinja2 PyYAML psutil requests six
```

To format & lint these scripts:

```bash
PYTHONPATH=$HOME/github.com/google/yapf python $HOME/github.com/google/yapf/yapf FILE.py > FILE.py.yapf
diff FILE.py FILE.py.yapf

pylint FILE.py
```
