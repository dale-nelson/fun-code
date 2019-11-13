def fibonacci(i):
  if i <= 1:
    return i
  #if fibonacci:
  return fibonacci(i - 1) + fibonacci(i - 2)

print(fibonacci(7))