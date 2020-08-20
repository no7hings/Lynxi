#!/bin/sh
# ---------------------------------------------------------------------
# lynxi startup script.
# ---------------------------------------------------------------------

# develop
export LYNXI_ENABLE_TRACE=TRUE
export LYNXI_ENABLE_DEVELOP=TRUE
#
export LYNXI_PATH="/data/e/myworkspace/td/lynxi"
export LYNXI_SCHEME_VAR="workspace/scheme/linux-x64-houdini-18/houdini_18"

export PYTHONPATH="$LYNXI_PATH/script/python"

export LYNXI_PATH_HOUDINI="/opt/hfs18.0.460/"
export LYNXI_BIN_HOUDINI="$LYNXI_PATH_HOUDINI/bin/houdinifx"
export LYNXI_BIN_PYTHON="$LYNXI_PATH_HOUDINI/python/bin/python2.7"
# arnold
export solidangle_LICENSE="5053@192.168.16.240"
export HOUDINI_PATH="$LYNXI_PATH/resource/plug/linux-houdini-18-htoa/5.3.0/source:&"
# lynxi
export HOUDINI_PATH="$HOUDINI_PATH:$LYNXI_PATH/$LYNXI_SCHEME_VAR/lynxi/houdini:&"
$LYNXI_BIN_HOUDINI

