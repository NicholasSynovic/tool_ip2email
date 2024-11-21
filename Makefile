build:
	poetry build
	pip install dist/*.tar.gz
	pyinstaller --clean --onefile --workpath ./pyinstaller -n ip2email ip2email/main.py

create-dev:
	pre-commit install
	rm -rf env
	python3.10 -m venv env
	( \
		. env/bin/activate; \
		pip install -r requirements.txt; \
		poetry install; \
		deactivate; \
	)
