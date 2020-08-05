# coding:utf-8
import os
#
import sys
#
import shutil


# Method
def main(sourceFile, targetFile):
    if not sourceFile.lower() == targetFile.lower():
        directory = os.path.dirname(sourceFile)
        try:
            os.makedirs(directory)
        except:
            os.path.exists(directory)
        finally:
            shutil.copy2(sourceFile, targetFile)


# Run
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])