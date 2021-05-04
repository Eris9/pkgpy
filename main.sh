rm -rf build && rm -rf dist
pip install build twine
python -m build
python3 -m twine upload --repository pypi dist/*