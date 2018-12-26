#!/usr/bin/env python3.7

message = input("Please input your message : ")
count = input("Please input the count number: ")
if count:
    count = int(count)
else:
    count = 1
def loop_display(message,count):
    while count>0:
        print(message)
        count -= 1
loop_display(message,count)
     
