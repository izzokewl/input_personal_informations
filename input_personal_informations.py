while True:
    try:
        nameinput = input("Enter your full name: ").title()
        if any(char.isdigit() for char in nameinput):
            raise ValueError("HOI BAT MAY NUMBER PANGALAN MO! ULET")
        print(f"Name: {nameinput}")
        break
    except ValueError as error:
        print (error)
