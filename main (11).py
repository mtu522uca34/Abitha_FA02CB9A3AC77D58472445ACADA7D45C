#1.1 Implement a recursive function to calculate the factorial of a given number
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n-1)

#driver code
num = 5;
print("factorial of", num, "is",
factorial (num))

#this code is contributed by smitha Dinesh semwal