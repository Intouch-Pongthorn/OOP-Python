# Write a short Python function, is even(k), that takes an integer value 
# and returns True if k is even, and False otherwise. 
# However, your function cannot use the multiplication, modulo, or division operators.
###########################
#solution 
#use  bitwise AND (&)
# 2 -> 010 (binary form) & 1 = 000 (0 even)
# 3-> 011 (binary form) & 1 = 001 (1 odd)

def even(k):
    if k & 1:
        return False
    return True

test_data = [1,2,3,4,6,1001,650,456,666]
for i in test_data :
    print(even(i))
