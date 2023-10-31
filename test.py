# how to make a specifications in loops 

def copy(one,two):
    A= one[:]
    for i in A:
        if i in two:
            one.remove(i)
    return one
print(copy([1,2,3,4,5],[4,5]))