# A simple reverse cypher program
message = input("what would you like to reverse?")
translated = ''
# len is used to signify length
i = len(message) - 1
while i >= 0:
	translated = translated + message[i]
	i = i - 1

print (translated)
print ('what else would you like to do??')