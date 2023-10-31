def fact(Ex):
    if Ex == 0:
        return 1
    return Ex*(fact(Ex-1))


print(fact(4))  # 4*3*2*1