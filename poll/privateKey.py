# A script to generate unique random private key
#!/usr/bin/env python

import random
from models import key

#Alphabet list
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
		 'n','o','p','q','r','s','t','u','v','w','x','y','z']

key = []


privateKey = ''
for i in range(10):
	no = str(random.randint(1,1000))
	txt = alpha[random.randint(1,24)]
	key.append(no + txt)
	
print(key)

#combining the key into one string
	

for item in key:
	privateKey = privateKey+item


#saving to db
a = key(username = 'Sam', privateKey = privateKey)
a.save()

print(privateKey)

#user_key = key.object.all()
#User_key = user_key[0].privatekey