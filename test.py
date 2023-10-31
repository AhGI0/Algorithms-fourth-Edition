def g(x):
    def h():
        x ="abc"  # it's conestant
        print(x) 
    x = x+ 1
    print(f'g:x = {x}')
    h()
    return x
x= 3
z= g(x)

