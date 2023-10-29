cube = 27
high = cube 
low = 0
guess =(high + low) / 2
num_guesses = 0
epsilon = .01

while abs((guess **3 - cube)) >= epsilon:
    if guess **3 <cube:
        low = guess
    else:
        high = guess
    guess =(low+ high) / 2
    num_guesses += 1


print(f'the cube root of {cube} is {guess}')