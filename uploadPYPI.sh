echo "Uninstall old rasterMiner version"
pip uninstall -y rasterMiner

echo "Running setup"
python3 setup.py sdist bdist_wheel

echo "Uploading to test repository"
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

echo "Wait for 5 minute to update the repository"
sleep 300

echo "installing PAMI from the testPYPI"
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps rasterMiner

echo "Uploading PAMI to main PYPI repository"
python3 -m twine upload dist/*

echo "Deleting unnecessary files"
rm -rf dist/ rasterMiner.egg-info/ build/

pip3 show rasterMiner

echo "Completed."