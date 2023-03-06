# Write a short Python function that takes a positive integer n 
# and returns the sum of the squares of all the odd positive integers smaller than n.

def sum(number):
    sum_of_squared_odd = 0
    for i in range(1,number):
        if i & 1: # AND bitwise operator checking the parity
            sum_of_squared_odd += i**2
    return sum_of_squared_odd

test_data = [1,2,3,4]
for integer in test_data:
    print(sum(integer))