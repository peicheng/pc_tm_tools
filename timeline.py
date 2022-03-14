#!/usr/bin/env python3
print('Timeline\n====')
for h in range(10, 13):
    if h in [12]:
        print(f'{h}:00')
        print('--')
        continue
    print(f'{h}:00\n{h}:30')
print('--')
for h in range(14, 19):
    print(f'{h}:00\n{h}:30')
