# coding=utf-8
import sqlite3


def connectDb(dbDirectory):
    connect = sqlite3.connect(dbDirectory)
    return connect


#
def saveDb(connect):
    return connect.commit()


#
def closeDb(connect):
    return connect.close()


#
def runDbCommand(connect, command, data=None):
    cur = connect.cursor()
    if data:
        cur.execute(command, data)
    else:
        cur.execute(command)
    return cur


#
def runDbCommands(connect, command, data=None):
    cur = connect.cursor()
    if data:
        cur.executemany(command, data)
    else:
        cur.executemany(command)
    return cur


#
def addDbTable(connect, tableName, tableValue):
    command = '''CREATE TABLE {0}{1}'''.format(tableName, tableValue)
    runDbCommand(connect, command)


#
def getDbTables(connect):
    lis = []
    command = "SELECT name FROM sqlite_master WHERE type='table'"
    data = runDbCommand(connect, command)
    if data:
        [lis.append(i[0]) for i in data]
    return lis


#
def getDbDatas():
    pass
