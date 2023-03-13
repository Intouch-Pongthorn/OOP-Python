# Write a Python function that takes a sequence of numbers 
# and determines if all the numbers are different from each other (that is, they are distinct).

def is_distinct(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] == lst[j]:
                return False
    return True

test_data = [[1,2,3,4],[1,2,3,4,5,6,4,7,9]]
for data in test_data:
    print(is_distinct(data))
