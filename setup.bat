
@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install required packages
pip install -r requirements.txt
REM Run the main.py script
python main.py
