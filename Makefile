install:
	pip install --upgrade pip &&\
	pip install --prefer-binary -r requirements.txt

test:
	python -m pytest --nbval-lax *.ipynb
	python -m pytest -vv --cov=main -rw test_*.py

format:
	black *.py

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.py

run:
	python lib.py	
	python main.py

all: install lint format test
