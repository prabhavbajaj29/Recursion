def factorial(n):

    if n==0 or n==1: #base case
        return 1
    else:
        return factorial(n-1)*n #we trust our function

n=int(input())

print(factorial(n))