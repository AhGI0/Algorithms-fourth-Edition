# how to find the cube root


low= 0
cube = 18 
high = cube
value = (high + low) / 2
epsion = .01
num_guesses = 0

while abs(value ** 2 - cube) >= epsion:
    if value **2 < cube:
        low = value
    else:
        high = value
    value =(high +low)/2
    num_guesses += 1


print((value))  #
