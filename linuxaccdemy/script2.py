#!/usr/bin/env python3.7
user = {'admin':True,'active':True,'name':'Kevin'}
prifix = ""
if user['admin'] and user['active']:
    prifix += "ADMIN - (ACTIVE)"
elif user['admin']:
    prifix += "ADMIN"
elif user['active']:
    prifix = "ACTIVE-"
print(prifix+user['name'])

