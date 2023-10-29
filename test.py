# let's play bisection algorithm again 

low = 0
epison = .01
cube = int(input("Enter a Number: "))
high =cube
guess = (low + high) / 2
num_guesses =0

# you can play any root [square root , cube root]
while abs((guess ** 2 - cube)) >= epison:
    if guess **2 < cube:
        low = guess
    else:
        high =guess
    guess =((low + high) / 2)
    num_guesses += 1

print(f'the cube root of {cube} is {guess}')
