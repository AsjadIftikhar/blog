@echo off
pip install virtualenv
virtualenv env
CALL env\Scripts\activate.bat
pip install -r requirements.txt
CALL env\Scripts\deactivate.bat
pause