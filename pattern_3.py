"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 <for n=5>
"""
def pattern_print(n):
    if n==1: #base case
        print(1)
        return #otherwise maximum recursion depth would be reached
    
    for i in range(1,n+1):
        print(i,end=" ")
    print()
    pattern_print(n-1) #we trust our function
    for i in range(1,n+1):
        print(i,end=" ")
    print()    
n=int(input())
pattern_print(n)        

    

