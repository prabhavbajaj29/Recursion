"""
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 <for n=6>
"""
def pattern_print(n):
    if n==0: #base case
        return
    
    for i in range(1,n+1):
        print(i,end=" ")
    print() #printing a new line
    pattern_print(n-1) #we trust our function

n=int(input())
pattern_print(n)
