# Write a short Python function that takes a positive integer n 
# and returns the sum of the squares of all the positive integers smaller than n.
def sum(number):
    sum = 0
    for i in range(1,number):
        sum += i**2
    return sum

test_data = [1,2,3,4]
for integer in test_data:
    print(sum(integer))