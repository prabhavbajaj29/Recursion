def sum_of_digits(n):
    if n==0: #base case
        return 0
    remaining_part=n//10 #getting the remaining part of the number except the last digit
    last_digit=n%10 #getting the last digit

    
    return sum_of_digits(remaining_part)+last_digit #we trust our function

n=int(input())

print(sum_of_digits(n))


        