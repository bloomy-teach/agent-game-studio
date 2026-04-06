@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip, setuptools, and wheel
python -m pip install --upgrade pip setuptools wheel

REM Clear pip cache
pip cache purge

REM Install numpy with precompiled binaries
pip install numpy --only-binary=:all:

REM Install required packages
pip install --use-deprecated=legacy-resolver -r "%~dp0requirements.txt"

REM Run the main.py script
python "%~dp0main.py"