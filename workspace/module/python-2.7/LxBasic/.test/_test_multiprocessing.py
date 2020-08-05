# coding:utf-8
from multiprocessing import Process
import time
import os


def task(name):
    print('{} 开始运行'.format(name))
    print('子进程id:{},父进程id:{}'.format(os.getpid(),os.getppid()))
    time.sleep(2)
    print('{} 运行结束'.format(name))


if __name__ == '__main__':
    print('主进程id:',os.getpid())
    p = Process(target=task, args=('进程1',))
    p.start()
    print('---主进程运行结束---')