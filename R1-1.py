# Write a short Python function, is multiple(n, m),that takes two integer values and returns True 
#if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
###########################
#solution 
#if n is a multiple of m then m mod n = 0

def is_multiple(n,m):
    return n % m == 0

test_data =[(15,5),(25,5),(12,9)]
for i in test_data:
    print(is_multiple(i[0],i[1]))

