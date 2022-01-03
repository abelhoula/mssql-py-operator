.PHONY: default

default: build

shell:
	poetry shell	
install:
	poetry install

build:
	poetry build
test:
	pytest