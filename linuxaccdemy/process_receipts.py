#!/usr/bin/env python3.7

import os
import glob
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

#get a list of receipts
receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

print(receipts)

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    destination = f"./processed/{name}"
    shutil.move(path,destination)
    print(f"Moved '{path}' to '{destination}'")
print(f"Receipts total: $%.2f" % subtotal)
