# coding:utf-8
import sys
from ctypes import *
Xlib = CDLL("libX11.so.6")
display = Xlib.XOpenDisplay(None)
if display == 0: sys.exit(2)
w = Xlib.XRootWindow(display, c_int(0))
(root_id, child_id) = (c_uint32(), c_uint32())
(root_x, root_y, win_x, win_y) = (c_int(), c_int(), c_int(), c_int())
mask = c_uint()
ret = Xlib.XQueryPointer(display, c_uint32(w), byref(root_id), byref(child_id), byref(root_x), byref(root_y), byref(win_x), byref(win_y), byref(mask))
if ret == 0:
    sys.exit(1)
print child_id.value
print root_x, root_y
print root_x.value
