
:: ---------------------------------------------------------------------
:: lynxi startup script.
:: ---------------------------------------------------------------------

:: develop
set LYNXI_ENABLE_TRACE=TRUE
set LYNXI_ENABLE_DEVELOP=TRUE
::
set LYNXI_PATH=e:\myworkspace\td\lynxi
set LYNXI_SCHEME_VAR=workspace\scheme\windows\default
set PYTHONPATH=\python\lynxi；
set LYNXI_BIN_PYTHON=%LYNXI_PATH%\bin\windows-python-2.7.13\bin\python
:: run bin
%LYNXI_BIN_PYTHON% %LYNXI_PATH%\%LYNXI_SCHEME_VAR%\lynxi\platform\script\setup.py