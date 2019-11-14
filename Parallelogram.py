def para(x, y=1, z=0):
    if type(x) != int:
        print("Not an int")
        return()
    while x > 0:
        for a in range(x):
            print(' ' * x + '*' * y + '*' * z)
            x -= 1
            y, z = y+1, z+1
    while y > 0:
        for a in range(y):
            print(' ' * x + '*' * y + '*' * z)
            x += 1
            y, z = y-1, z-1

para(5)