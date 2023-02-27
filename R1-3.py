# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, 
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.
###########################
#solution 
#use  for loop
def minmax(data):
    min,max = data[0],data[0]
    #find min and max
    for i in data:
        if i < min:
            min = i
        if i > max:
            max = i
    return((min,max))

test_data = [[1,2,3,4],[6,2,9,18],[1]]
for k in test_data:
    print(minmax(k))
