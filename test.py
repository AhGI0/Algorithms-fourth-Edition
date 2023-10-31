def check(num):
    low =0
    high = num
    epsion =.01
    guess= (high + low) / 2.0
    num_guesses = 0
    while abs(guess **3 - num) >= epsion:
        if guess ** 3 < num:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2
        num_guesses += 1
    return f'the cube root of {num} is {guess}'
A= int(input("Enter a number: "))    
print(check(A))