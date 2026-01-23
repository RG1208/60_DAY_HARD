try:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    def add(a,b):
        return a+b

except Exception as e:
    print(f"An error occurred: {e}")

result = add(a,b)
print(f"The sum of {a} and {b} is {result}")
