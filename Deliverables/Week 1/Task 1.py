# print('Program to check if input number is a prime number')
num = int(input('enter a number greater than 1: '))
for i in range(2,num):
    if num % i == 0:
        print(str(num),'is not a prime number.')
        break
else:
    print(str(num),'is a prime number')


# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# def func1(*args):
#   print(*args)

# func1(1, 2, 3, "Hello", "World!")

# def sum_(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_(n-1)
    
# print(sum_(15))


import pandas as pd
