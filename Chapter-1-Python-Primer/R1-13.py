# Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before, 
# and compare this method to an equivalent Python function for doing the same thing.

def reverse_lst(lst):
    start = 0
    end = len(lst) -1
    while start < end:
        lst[start],lst[end] = lst[end],lst[start]
        start += 1
        end -= 1
    return lst

print(reverse_lst([1,2,3,4]))
test_lst = [1,2,3,4]
test_lst.reverse()
print(test_lst)
