def naturalNumberAddition(i):
  if i <= 1:
    return i
  if naturalNumberAddition:
    return i+naturalNumberAddition(i-1)

print(naturalNumberAddition(5))