# def shelf(one,two):
#     if two ==0:
#         return 0 
#     else:
#         return one +shelf(one ,two-1)
# print(shelf(10,5))

# # --- 


def shelf(one,two):
    result =0 
    while two > 0:
        result += one
        two -= 1
    return result


print(shelf(10,3))   #expected to be 300