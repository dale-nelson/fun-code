def main():
    print("This program will calculate the nth value of the Fibonacci sequence.")
    userInput = validLoop()
    posCheck = isPos(userInput)
    print("The value of the fib sequence at position {0} is {1}".format(posCheck,fib(posCheck)))
    return

def fib(i):
    if i <= 1 or i is None:
        return i
    return fib(i - 1) + fib(i - 2)

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