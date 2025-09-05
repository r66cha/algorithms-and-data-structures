freeze:
	uv pip freeze > requirements.txt

install:
	uv pip install -r requirements.txt

run:
	uv run main.py


test:
	pytest -vv

test-sll:
	pytest -v tests/linked_lists/test_single_list.py::${name}

