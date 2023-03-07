# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, 
# and expression s[k] is used for in- dex −n ≤ k < 0, 
# what is the equivalent index j ≥ 0 such that s[j] references the same element?

###########################
#solution 
# relation between j and k -> s[j] = n + s[k] where n is the length of a sequence

def test_equivalent(seq,negative_index):
    positive_index = len(seq) + negative_index
    print(f' the negative indes and positive index are {negative_index} and {positive_index} respectively')
    print(f'the value of seq[{negative_index}] is {seq[negative_index]}')
    print(f'the val of seq[{positive_index}] is {seq[positive_index]}')
    print('_______________________________________________________________________________________________________')

test_data = [1,2,3]

for i in range(-1,-abs(len(test_data)+1),-1): #loop negatively  from -1 to the last one 
    test_equivalent(test_data,i)


