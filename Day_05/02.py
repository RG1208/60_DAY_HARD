password = input("Enter a password: ")

chars= list(password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_special = any(char in "@/" for char in password)
has_int = any(char.isdigit() for char in password)


if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_special
    and has_int
):
    print(f"Valid Password")
else:
    print(f"Invalid Password")