print("welcome to le name generator where we generate v cheap gud names 4 u ok")
from random import choice
len = 10
name = 'r'
for i in range(len):
     name += choice ('abcdefghijklmnopqrstuvwxyz')+('esh')+choice ('12345678910111213')
print(name)
