# coding:utf-8
import os
#
import sys


# Method
def main(file):
    if os.path.isfile(file):
        os.remove(file)


# Run
if __name__ == '__main__':
    main(sys.argv[1])