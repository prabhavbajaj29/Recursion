#sum of numbers from 1 to n --> 1+2+3+4+5+6+.....+(n-1)+(n)

def sum_n(n):
    if n==1: #base case
        return 1
    else:
        return sum_n(n-1)+n #we trust that the function works fine till n-1 and then add n to it


n=int(input())

print(sum_n(n))