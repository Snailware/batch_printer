:: this script will create a python virtual environment and install the required
:: packages into it from a requirements.txt file. 

@echo off
echo creating virtual environment.
python -m venv .env
echo activating virtual environment.
call .env\Scripts\activate.bat
echo installing packages.
pip install -r requirements.txt
call .env\Scripts\deactivate.bat
echo setup complete.
pause