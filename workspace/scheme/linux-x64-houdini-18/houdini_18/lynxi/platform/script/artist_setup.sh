# coding:utf-8
#!/bin/sh
# ---------------------------------------------------------------------
# lynxi startup script.
# ---------------------------------------------------------------------

# develop
export LYNXI_ENABLE_TRACE=TRUE
export LYNXI_ENABLE_DEVELOP=FALSE
#
export LYNXI_PATH="/l/packages/pg/prod/lynxitool/0.0.3/lynxitool"
export LYNXI_SCHEME_VAR="resource/scheme/linux-x64-houdini-18-houdini_18/0.0.0/source/houdini_18"

export PYTHONPATH="$LYNXI_PATH/python/lynxi"

export LYNXI_PATH_HOUDINI="/opt/hfs18.0.460/"
export LYNXI_BIN_HOUDINI="$LYNXI_PATH_HOUDINI/bin/houdinifx"
export LYNXI_BIN_PYTHON="$LYNXI_PATH_HOUDINI/python/bin/python2.7"
# arnold
export solidangle_LICENSE="5053@192.168.16.240"
export HOUDINI_PATH="$LYNXI_PATH/resource/plug/linux-houdini-18-htoa/5.3.0/source:&"
# lynxi
export HOUDINI_PATH="$HOUDINI_PATH:$LYNXI_PATH/$LYNXI_SCHEME_VAR/lynxi/houdini:&"
$LYNXI_BIN_HOUDINI
