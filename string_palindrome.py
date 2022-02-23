#to check if the string is palindrome or not using recursion

def check_palindrome(string,start,end):
    if (start==end): #i.e the len(string)==1
        return True
    if (start>end): 
        return False
    if (string[start]!=string[end]): #for a palindrome first and last item should be same
        return False

    return check_palindrome(string,start+1,end-1) #we trust our function

string=input()

start=0
end=len(string)-1

if (check_palindrome(string,start,end)):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome") 

       