# sum of a squared and b squared
def sum_of_squares(a,b):
  return a**2 + b**2

# increments a
def increment(a):
  return a + 1

# increments a by n
def increment_by(a, n):
  return a + n

# calculates the factorial of n
def factorial(n):
  result = 1
  for num in range(2,n+1):
    result = result*num
  return result

# counts from one to ten by using a for loop
def one_to_ten_for():
  for num in range(1,11):
    print(num)

# counts from one to ten by using a while loop
def one_to_ten_while():
  num = 1
  while num < 11:
    print(num)
    num = increment(num)

# checks if a number is between 1 and 10
def between_one_and_ten(num):
  num in range(1,11)

# checks if a is bigger than b then
# checks if a is smaller than b then
# checks if a and b are equal
def number_relation(a,b):
  print(a>b)
  print(a<b)
  print(a==b)

# checks if the given number is a prime
def is_prime(num):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        return False
    else:
      return True
