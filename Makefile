all: convert_readme build_package clean

convert_readme:
	@echo "Converting README.org to README.md..."
	pandoc -s README.org -o README.md

build_package: convert_readme
	@echo "Building the package..."
	trash dist
	. ./env/bin/activate && python3 -m build

clean:
	@echo "Cleaning build artifacts..."
	rm -f README.md

deploy_test:
	@echo "Deploy..."
	. ./env/bin/activate && python3 -m twine upload --repository testpypi dist/*

deploy:
	@echo "Deploy..."
	. ./env/bin/activate && python3 -m twine upload dist/*
