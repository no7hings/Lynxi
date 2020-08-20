#!/bin/sh
# ---------------------------------------------------------------------
# lynxi startup script.
# ---------------------------------------------------------------------

# develop
export LYNXI_ENABLE_TRACE=TRUE
export LYNXI_ENABLE_DEVELOP=TRUE
#
export LYNXI_PATH=/data/e/myworkspace/td/lynxi
export LYNXI_SCHEME_VAR=workspace/scheme/linux-x64/default
export PYTHONPATH=$LYNXI_PATH/script/python
export LYNXI_BIN_PYTHON=$LYNXI_PATH/bin/linux-x64-python-2.7.18/bin/python
$LYNXI_BIN_PYTHON $LYNXI_PATH/$LYNXI_SCHEME_VAR/lynxi/platform/script/setup.py