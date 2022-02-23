"""
1
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6 <for n=6>
"""
def pattern_print(n):
    if n==0: #base case
        return

    pattern_print(n-1) #we trust our function--> printing till (n-1)th row

    for i in range(1,n+1):
        print(i,end=" ") #to print the last row

    print()
n=int(input())
pattern_print(n)        
