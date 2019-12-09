# coding:utf-8
# coding:utf-8
import os
#
import sys


# Method
def main(sourceFile, targetFile):
    if not sourceFile.lower() == targetFile.lower():
        os.rename(sourceFile, targetFile)


# Run
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])