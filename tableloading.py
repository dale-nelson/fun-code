#This project will explore loading a table with rows and columns.
#An idea I have had is to take a bunch of words of equal length and 
#put them into a table letter by letter.

dLW = ["embezzlement","jeopardizing","journalizing","quixotically","maximization","extravaganza",
"objectifying","unpublicized","exemplifying","immobilizing","subjectivity","sympathizing"]
print(len(dLW))
print(len(dLW[6]))

splitTest = dLW[1]

splitList = []

for char in splitTest:
    print(char)
    splitList.append(char)

print(splitList)

for i in splitList:
    print(i, end=" ")

print('\n')

for i in dLW:
    print(i, end=" ")

for i in dLW:
    print(i)

for i in dLW:
    for char in i:
        print(char, end=" ")

row = []
column = []

#Ok, so I relized what I did here was I had already split up all the words into characters
for i in dLW:
    for char in i:
        column.append(i)
    row.append(column)

print(len(column))
print(column)
#print(len(row))
#print(row)