#From my UVU Python class, I want to try to generate a random wordsearch
#Couple ideas:
# 1. Provide a list of words to put into the table
# 2. Have the user enter words (<= 10) or until the user escapes (0 means quit)
# 3. Get a list of words from a file and have them read into the program

import random
import string

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

i = 0

randList = []

while i < 12:
    randList.append(random.choice(chars))
    i += 1

testPrint = ''
print(testPrint.join(randList))

#If I put the var as a space, it will print a space in between each random char
testPrint2 = ' '
print(testPrint2.join(randList))