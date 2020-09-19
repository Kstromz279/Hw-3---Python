# Author: Khalil Stroman kzs5955@psu.edu
def digit_sum(n):
  if n > 0:
    return n%10 + int(digit_sum(n//10))
  else: 
    return 0

def run():
  digits = input("Enter an int: ")
  digits = int(digits)
  print(f"sum of digits of {digits} is {digit_sum(digits)}.")

if __name__ == "__main__":
  run()