def check(str):
    if str == "Nada":
        return("it's okay")
    else:
        the_diff =str[0]
        return(f'the word will be N{str[1::]} the wrong letter is {the_diff}')
print(check("Hada"))