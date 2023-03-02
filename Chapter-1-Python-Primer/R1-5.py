# Give a single command that computes the sum from Exercise R-1.4,
# relying on Python’s comprehension syntax and the built-in sum function.

test_data= [1,2,3,4]
for data in test_data:
    print(sum([i**2 for i in range(1,data)]))