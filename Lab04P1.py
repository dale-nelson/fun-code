def main():
  print("This program calculates the nth value of the Fibonacci sequence.")
  valid_check = isInputValid()
  pos_check = isPos(valid_check)
  print(fibonacci(pos_check))
  return

def fibonacci(i):
  if i <= 1:
    return i
  #If i > 1, return the following:
  return fibonacci(i - 1) + fibonacci(i - 2)

def userInput():
    try:
        return int(float(input()))
    except ValueError:
        print("Your input is not a number. Please try again.")

def isInputValid():
    ui = userInput()
    if not userInput():
        ui = userInput()
    return ui

def isPos(i):
    if i < 0:
        print("Negative numbers are invalid for the Fibonacci sequence. Please try again.")
        i = isInputValid()
    return i

main()