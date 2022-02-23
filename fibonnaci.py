"""
Fibonnaci sequence(finding the nth fibonnaci)
0,1,1,2,3,5,8,13,21,34,55,89
"""
def fibonnaci(n):

    if n==1: #base case
        return 0
    if n==2: #base case
        return 1    
    
    return fibonnaci(n-1)+fibonnaci(n-2) #we trust our function

n=int(input())
print(fibonnaci(n))

