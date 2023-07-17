:: this script will run a python program ('main.py') using the local virtual 
:: environment (.env) on windows 10. note that the venv must be generated in 
:: the same folder as the python script. 

@echo off
call .env\Scripts\activate.bat
python main.py
call .env\Scripts\deactivate.bat