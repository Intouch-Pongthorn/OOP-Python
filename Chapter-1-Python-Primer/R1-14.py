# Write a short Python function that takes a sequence of integer values and determines 
# if there is a distinct pair of numbers in the sequence whose product is odd.

def product_is_odd(lst):
    for i in lst:
        for j in lst:
            if i!= j and (i*j) & 1:  #i and j are not identical and their product is odd
                return True 
        return False
    
print(product_is_odd([2,3,4]))
print(product_is_odd([1,3,4]))
