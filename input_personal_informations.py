while True:
    try:
        nameinput = input("Enter your full name: ").title()
        if any(char.isdigit() for char in nameinput):
            raise ValueError("HOI BAT MAY NUMBER PANGALAN MO! ULET")
        print(f"Name: {nameinput}")
        break
    except ValueError as error:
        print (error)
while True:
    try:
        ageinput = int(input("Enter your age: "))
        print (f"Age: {ageinput}")
        break
    except ValueError:
        print ("gets kita, pero pwede bang gawin mong numbers yan")
addressinput = input("Enter your address: ").title()
print (f"Address: {addressinput}")