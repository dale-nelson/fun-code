def fibonacci(i):
  if i <= 1:
    return i
  #if fibonacci:
  return fibonacci(i - 1) + fibonacci(i - 2)

print(fibonacci(7))

def factorial(i):
  if i <= 1:
    return i
  if factorial:
    return i*factorial(i-1)

print(factorial(4))

def naturalNumberAddition(i):
  if i <= 1:
    return i
  if naturalNumberAddition:
    return i+naturalNumberAddition(i-1)

print(naturalNumberAddition(5))