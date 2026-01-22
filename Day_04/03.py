text = "Python is a very good langauage and anyone with python can excel python very easily"

words = text.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] =1

print(f"{frequency}")