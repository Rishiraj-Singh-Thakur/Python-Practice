while True:
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))

        print(a+b)

    except ValueError:
        print("Enter valid number")