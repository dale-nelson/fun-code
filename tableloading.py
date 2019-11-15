#This project will explore loading a table with rows and columns.
#An idea I have had is to take a bunch of words of equal length and 
#put them into a table letter by letter.

dozenLetterWords = ["embezzlement","jeopardizing","journalizing","quixotically","maximization","extravaganza",
"objectifying","unpublicized","exemplifying","immobilizing","subjectivity","sympathizing","cursed"]
print(len(dozenLetterWords))
print(len(dozenLetterWords[12]))

splitTest = dozenLetterWords[1]

splitList = []

for char in splitTest:
    print(char)
    splitList.append(char)

print(splitList)

for i in splitList:
    print(i)