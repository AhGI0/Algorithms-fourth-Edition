def get_data(ex):
    num = ()
    word = ()
    for i in ex:
        num += (i[0],)
        if i[1] not in word:
            word += (i[1],)
    min_n = min(num)
    max_n = max(num)
    unique = len(word)
    return(min_n,max_n,unique)


print(get_data(((10,"Ahmed"),(100,"Nada"),(400,"Yosra"))))