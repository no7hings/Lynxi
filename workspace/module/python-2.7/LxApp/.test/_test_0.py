# coding:utf-8
if __name__ == '__main__':
    from LxApp import appObjects

    tk = appObjects.AppToolkit()

    for t in tk.tools():
        print t.icon
