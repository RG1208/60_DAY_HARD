def outer():
    print("This is Outer")

    def inner():
        print("This is Inner")
    return inner()

outer()