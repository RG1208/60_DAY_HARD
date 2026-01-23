Text = input("Enter a Text: ")

s = ""

for char in Text:
    if char not in "@/":
        s = s+ char
    else:
        continue
print(s)