# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#proposed solution: loop through list, compare two values in each iteration, stop when true, else print false

def sum_to_k(k, thislist):
    for x in thislist:
        for y in thislist:
            if x + y == k:
                return "True"
    return "False" #return for first for loop and not second
           
#call the function  
result = sum_to_k(10, [9, 1, 0, 10, 7, 30])
print(result)
    


#problems
#loop didn't stop when true - had to use two arguments and call function at the end, don't need to declare the variables at the start i.e. k = ... and thislist = ...

#only outputting false even when conditions are met - need to make sure x and y are distinct - because I put the 'else' in the if statement

#including else in the if statement and putting print instead of return caused it to loop through entire list and print result for each list value