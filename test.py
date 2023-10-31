def i(ex):
    if ex == 0:
        return 1
    return ex * i(ex- 1)  #the aim of it find the factorial

print(i(4))