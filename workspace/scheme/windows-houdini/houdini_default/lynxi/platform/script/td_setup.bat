:: ---------------------------------------------------------------------
:: lynxi startup script.
:: ---------------------------------------------------------------------
:: develop
set LYNXI_ENABLE_TRACE=TRUE
set LYNXI_ENABLE_DEVELOP=TRUE
::
set LYNXI_PATH=e:\myworkspace\td\lynxi
set LYNXI_SCHEME_VAR=workspace\scheme\windows-houdini\houdini_default

set PYTHONPATH=%LYNXI_PATH%\script\python

set LYNXI_PATH_HOUDINI=e:\app\windows-x64-houdini-18\source
:: lynxi
set HOUDINI_PATH=%LYNXI_PATH_HOUDINI%\houdini;^&;%LYNXI_PATH%\%LYNXI_SCHEME_VAR%\lynxi\houdini;^&


set LYNXI_BIN_HOUDINI=%LYNXI_PATH_HOUDINI%\bin\houdinifx.exe
%LYNXI_BIN_HOUDINI%

