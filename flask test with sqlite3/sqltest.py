# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 02:19:03 2020

@author: dhk13
"""
import sqlite3

con = sqlite3.connect("./user.db")
#print(type(con))
#print(sqlite3.Connection)

cursor=con.cursor()

"""
primary key 설정이 안되어있음.
"""

def createTable(tablename, numofcol, collst, coltype):
    cmd=f'CREATE TABLE {tablename}('
    for idx in range(numofcol):
        cmd+=collst[idx]
        cmd+=(" "+coltype[idx]+", ")
    cmd=cmd[:-2]+")"
    print(cmd)
    cursor.execute(cmd)

def insertRow(tablename, numofcol, collst):
    cmd=f'INSERT INTO {tablename} VALUES( '
    for idx in range(numofcol):
        cmd+=('\''+collst[idx]+'\''+", ")
    cmd=cmd[:-2]+")"
    print(cmd)
    cursor.execute(cmd)

#def selectRow():
    #참고: cursor.fetchone() fetches single row result 
    #everytime it is executed. (like iterator)
    #.fetchall() fetches all the lst into list.

#def selectAll():


if __name__=="__main__":
    #createTable('user', 2, ['id', 'pw'], ['text', 'text'])
    insertRow('user', 2, ['dhk1349','123123'])
    con.commit()
    con.close()