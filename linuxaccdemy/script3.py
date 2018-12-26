#!/usr/bin/env python3.7
users =  [
     {'admin':True,'active':True,'name':'Kevin'},
     {'admin':False,'active':True,'name':'James'},
     {'admin':True,'active':False,'name':'Kim'},
     {'admin':False,'active':False,'name':'Thomas'},
     {'admin':True,'active':False,'name':'Sam'},
]
linenum = 1
#user = {'admin':True,'active':True,'name':'Kevin'}
#prifix =f"{linenum}: "
for user in users:
    prifix =f"{linenum}: "
    if user['admin'] and user['active']:
        prifix += "ADMIN - (ACTIVE) "
    elif user['admin']:
        prifix += "ADMIN "
    elif user['active']:
        prifix += "ACTIVE - "
    print(prifix+user['name'])
    linenum +=1
