while True:
    try:
        nameinput = input("Enter your full name: ").title()
        if any(char.isdigit() for char in nameinput):
            raise ValueError("HOI BAT MAY NUMBER PANGALAN MO! ULET")
        print(f"Ikaw si {nameinput}")
        break
    except ValueError as error:
        print (error)

while True:
    try:
        ageinput = int(input("Enter your age: "))
        print (f"Ang edad mo ay {ageinput}")
        break
    except ValueError:
        print ("gets kita, pero pwede bang gawin mong numbers yan...")

addressinput = input("Enter your address: ").title()
print (f"Jan ka pala nakatira haha, sa {addressinput}")

emailinput = input("Enter your Email address: ")
print (f"Hack ka sakin dejk ang email mo ay {emailinput}")

feelingrn = input ("What are you feeling as of the moment?")
print (f"ok gets kita sana malagpasan mo yan")
