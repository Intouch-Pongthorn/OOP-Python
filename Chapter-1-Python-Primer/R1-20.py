
# Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. 
# The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). 
# Using only the randint function, implement your own version of the shuffle function.
import random

def shuffle(seq:list[any])-> None:
    print('orinal sequence: '+ str(seq))
    
    for current_position in range(0,len(seq)-1):
        random_position = random.randint(0,len(seq)-1)
        seq[current_position],seq[random_position] = seq[random_position],seq[current_position]
    print('shuffled sequence: '+ str(seq))

shuffle([1,2,3,4])