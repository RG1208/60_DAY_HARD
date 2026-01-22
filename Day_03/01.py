a = [1,2,3,4,5,6,7,8,9,10]

max=a[0]
min=a[0]

for num in a:
    if num>max:
        max=num
    if num<min:
        min=num

print(f"Max = {max}")
print(f"Min = {min}")