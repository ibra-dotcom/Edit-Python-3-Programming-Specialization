#Factorial of a number using recursion:def factorial(n):
#simple function  
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Example usage:
num = 8
print("Factorial of", num, "is", factorial(num))