n = int(input("Enter a number: "))
list=[]
def even(n):
    for i in range(1,n+1):
        if i%2==0:
            list.append(i)
        else:
            continue
    return list

print(even(n))