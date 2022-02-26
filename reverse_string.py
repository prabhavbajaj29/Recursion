def reverse_string(string):

    if (len(string)==0): #base case
        return


    temp=string[0] #first character of the string
    reverse_string(string[1:]) #we trust our function

    print(temp,end="")

string=input()
reverse_string(string)   
