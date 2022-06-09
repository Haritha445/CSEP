def recursive_factorial(n):
    if n==1 or n==0:
        return 1
    else:
       return n*recursive_factorial(n-1)
number = int(input("enter the input:"))
if number < 0:
   print("factorial does not exist for negative numbers")
else:
   print("the factorial of",number, "is", recursive_factorial(number))
