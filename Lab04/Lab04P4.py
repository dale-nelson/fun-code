def main():
    print("This program prints out a diamond of asterisks. You get to input how many rows it has until it reaches its middle point.")
    valVar = validLoop()
    posVar = isPos(valVar)
    top = topHalf(posVar)
    bottomHalf(top)
    return

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

def topHalf(n):
    count = 1
    while count <= n:
        print(' ' * (n - count), '*' * count + '*' * (count - 1))
        count += 1
    return count

def bottomHalf(n):
    count = n
    count -= 2
    while count >= 0:
        print(' ' * (n - count - 1), '*' * count + '*' * (count - 1))
        count -= 1

main()