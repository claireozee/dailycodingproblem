#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

'''Proposed solution: 
- loop through array from arr[0] to end (consider infinite size) - simple for loop and print
- write function which returns each element of the list to be used in product function
- write function for product of array elements
- use both functions - for array[i] newarray=product/i

#pseudo
define new function(arr)
    for x in arr:
        print(x) prints each array object individually. want to take each of these and multiply them (store each number as a variable maybe)

    product =  
    
'''


def array_input(arr):
    for x in arr:
        print(x)
        #return x
    

#def new_array():
    #array_input

#calling the function
print(array_input([2, 4, 11, 6]))



#problem faced - every element is printed on a separate line - need to multiply each one (by storing as a variable (?) but what happens to a very large array?)


#note needed to break array structure then reconstruct at the end