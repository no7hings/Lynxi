:: ---------------------------------------------------------------------
:: lynxi startup script.
:: ---------------------------------------------------------------------
@echo off
pushd %~d0
:: develop
set LYNXI_ENABLE_TRACE=TRUE
set LYNXI_ENABLE_DEVELOP=TRUE
::
set LYNXI_PATH=e:\myworkspace\td\lynxi
set LYNXI_SCHEME_VAR=workspace\scheme\windows\default
:: python
set PYTHONPATH=%LYNXI_PATH%\script\python
:: bin
set LYNXI_BIN_PYTHON=%LYNXI_PATH%\bin\windows-x64-python-2.7.13\source\python.exe
:: run bin
%LYNXI_BIN_PYTHON% %LYNXI_PATH%\%LYNXI_SCHEME_VAR%\lynxi\platform\script\setup.py
popd
echo. & pause