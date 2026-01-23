email = input("Enter your email address: ")

if (
    " " not in email
    and email.count("@") ==1
    and "." in email.split("@")[1]
):
    print(f"Valid {email}")
else:
    print(f"Invalid {email}")