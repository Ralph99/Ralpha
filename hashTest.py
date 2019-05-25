__author__ = 'Sage'
__version__ = '0.01'
'''This script uses md5 encryption algorithm to do its work'''
#first we import hashlib, which is the integral library for this script
import hashlib
import datetime
from datetime import date
s = date.today()
#then we import md5 which is the encription algorithm used
from hashlib import md5
#we first initialize the contents oof the hashing algorithm in preparation for future events
m = hashlib.md5()
#this asks for the thing we wanna hash
message = raw_input('what would you like to hash? ')
#we then update the input of the algorithm with the contents of message
m.update(message)
g = m.hexdigest()
print g
#now we save the generated hash into a .txt file named hasher
sage = open('hasher.txt', 'a')
sage.write('\n' +str(s)+ '\t' + g)