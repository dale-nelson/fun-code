def main():
    print("This program will calculate the addition of natural numbers in sequence.")
    userInput = validLoop()
    posCheck = isPos(userInput)
    print("The sum of all the natural numbers less than {0} is {1}".format(posCheck,naturalNumAdd(posCheck)))
    return

def naturalNumAdd(i):
  if i <= 1:
    return i
  if naturalNumAdd:
    return i + naturalNumAdd(i - 1)

def validCheck():
    try:
        return int(float(input()))
    except ValueError:
        print("That value is not a number. Please try again.")

def validLoop():
    inp = validCheck()
    while inp is None:
        inp = validCheck()
    else:
        return inp

def isPos(i):
    while i < 0:
        print("Negative numbers cannot be accepted. Please try again.")
        i = validLoop()
    else:
        return i

main()