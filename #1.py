# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Can you do this in one pass?

#solution: loop through list, compare two values in each iteration, stop if true else print false

def sum_to_k():
    k = int(input())
    thislist = [8, 2, 15, 6, 21, 3, 4, 90, 1000000, 0, 71]

    for x in thislist:
        for y in thislist:
            if x + y == k:
                output = "True"
            else:
                output = "False" #putting print here will loop through entire list and print result for each list value
            return output
#print(output)
sum_to_k()
    


