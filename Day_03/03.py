a = [1,2,3,4,5,6,7,8,9,10]
new_list=[]

for num in a:
    if num%2==0:
        new_list.append(num)
    else:
        continue
print(f"{new_list}")
