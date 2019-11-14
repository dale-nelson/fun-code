def main():
    print("This program computes the factorial of a value the user inputs.")
    vl = validLoop()
    posCheck = isPos(vl)
    print("The value of {0}! is {1}".format(posCheck,factorial(posCheck)))
    return

def factorial(i):
  if i <= 1:
    return i
  if factorial:
    return i * factorial(i - 1)

def userInput():
    try:
        return int(float(input()))
    except ValueError:
        print("That is not a number. Please try again.")

def validLoop():
    ui = userInput()
    while ui is None:
        ui = userInput()
    return ui

def isPos(i):
    while i < 0:
        print("Only positive numbers can be accepted. Please try again.")
        i = validLoop()
    return i

main()