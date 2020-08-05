# coding:utf-8
#!/bin/sh
# ---------------------------------------------------------------------
# lynxi startup script.
# ---------------------------------------------------------------------

# develop config
export LYNXI_ENABLE_TRACE=TRUE
export LYNXI_ENABLE_DEVELOP=TRUE

export LYNXI_PATH="/data/e/myworkspace/td/lynxi"
export LYNXI_SCHEME_VAR="workspace/scheme/linux-x64-maya/maya_default"

export PYTHONPATH="$LYNXI_PATH/python/lynxi"
export PYTHONPATH="$PYTHONPATH:$LYNXI_PATH/$LYNXI_SCHEME_VAR/lynxi/maya/scripts"

export LYNXI_PATH_MAYA="/usr/autodesk/maya2019"
export LYNXI_BIN_MAYA="$LYNXI_PATH_MAYA/bin/maya2019"
export LYNXI_BIN_PYTHON="$LYNXI_PATH_MAYA/python/bin/python2.7"

$LYNXI_BIN_MAYA

