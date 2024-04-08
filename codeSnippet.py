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

#Note on recursion: 

#We define factorial(n) to calculate the factorial of n.
#If n is 0, the factorial is 1 (base case).
#Otherwise, we return n times factorial(n-1), which is a smaller version of the same problem.
#This process continues until n reaches 0, and then it starts combining the results to calculate the factorial.
