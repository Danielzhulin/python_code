#!/usr/bin/env python3.7

import random
import os
import json

count = int(os.getenv("FILE_COUNT") or 5)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for indentifier in range(count):
    amount = random.uniform(1.0,1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./new/receipt-{indentifier}.json','w') as f:
        json.dump(content,f)
