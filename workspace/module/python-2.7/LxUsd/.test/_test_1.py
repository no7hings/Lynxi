# coding:utf-8
from __future__ import print_function
import sys
import pxr.Usdviewq as Usdviewq

if __name__ == '__main__':
    try:
        Usdviewq.Launcher().Run()
    except Usdviewq.InvalidUsdviewOption as e:
        print("ERROR: " + e.message, file=sys.stderr)
        sys.exit(1)
