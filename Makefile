setup:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip3 install -r requirements.txt; \

run:
	. venv/bin/activate; \
	python3 template.py; \

freeze:
	. venv/bin/activate; \
	pip3 install --upgrade Jinja2 PyYAML boto boto3 nested_dict nose psutil pynput pytest pytest-xdist python-dateutil requests simplejson six slacker black flake8 pylint; \
	pip3 freeze > requirements.txt; \

format:
	. venv/bin/activate; \
	black *.py tests/*.py; \

lint:
	. venv/bin/activate; \
	flake8 --ignore E501,W503 *.py tests/*.py; \
	pylint --disable=C,R *.py tests/*.py; \

check: format lint

test:
	. venv/bin/activate; \
	pytest -n auto -v; \

retest:
	. venv/bin/activate; \
	pytest -n auto -v --lf; \

.PHONY: check format freeze lint run setup test
