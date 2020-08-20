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
set LYNXI_SCHEME_VAR=workspace\scheme\windows-maya\maya_default
:: python
set PYTHONPATH=%LYNXI_PATH%\script\python
set PYTHONPATH=%PYTHONPATH%;%LYNXI_PATH%\%LYNXI_SCHEME_VAR%\lynxi\maya\scripts
:: bin
set LYNXI_PATH_MAYA=E:\app\windows-x64-maya-2019\source
set LYNXI_BIN_MAYA=%LYNXI_PATH_MAYA%\bin\maya.exe"
:: run bin
%LYNXI_BIN_MAYA%
popd
echo. & pause