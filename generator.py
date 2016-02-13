import random
len = 10
name = 'r'
for i in range(len):
     name += random.choice ('abcdefghijklmnopqrstuvwxyz')+('esh')+random.choice ('12345678910111213')
print(name)
