a = [1,2,3,4,5,1,2,3,4,5]

new_list=[]
for num in a:
    # print(num)
    if num not in new_list:
        new_list.append(num)

print(new_list)
