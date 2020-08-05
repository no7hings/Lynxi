# coding:utf-8
import ctypes

HWND = ctypes.c_void_p

if ctypes.sizeof(ctypes.c_long) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulong
    LPARAM = ctypes.c_long
elif ctypes.sizeof(ctypes.c_longlong) == ctypes.sizeof(ctypes.c_void_p):
    WPARAM = ctypes.c_ulonglong
    LPARAM = ctypes.c_longlong

DWORD = ctypes.c_ulong


class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_long),
        ("y", ctypes.c_long)
    ]


class MSG(ctypes.Structure):
    _fields_ = [
        ("hWnd", HWND),
        ("message", ctypes.c_uint),
        ("wParam", WPARAM),
        ("lParam", LPARAM),
        ("time", DWORD),
        ("pt", POINT)
    ]

