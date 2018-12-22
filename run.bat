@echo off

rem "Try Python in venv if it exists"
set cmd=".\venv\Scripts\python.exe"
if exist %cmd% goto venv

rem Try to use Python 3.7 installed
rem in the root of the harddrive
set cmd="\Python37\python.exe"
if exist %cmd% goto exe

rem fallback to running python.
set cmd="python"
goto exe


:venv
call .\venv\Scripts\activate.bat
:exe
pushd %~dp0
%cmd% manage.py migrate
%cmd% manage.py runserver %*
popd
