.PHONY: serve test

serve:
	python3 -m http.server 8000

test:
	python3 -m unittest discover -s tests -v
