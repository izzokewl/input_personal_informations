while True:
    try:
        nameinput = input("Enter your full name: ").title()
        if any(char.isdigit() for char in nameinput):
            raise ValueError("HOI BAT MAY NUMBER PANGALAN MO! ULET")
        break
    except ValueError as error:
        print (error)

while True:
    try:
        ageinput = int(input("Enter your age: "))
        break
    except ValueError:
        print ("gets kita, pero pwede bang gawin mong numbers yan...")

addressinput = input("Enter your address: ").title()

emailinput = input("Enter your Email address: ")

feelingrn = input ("What are you feeling as of the moment? ")
print (f"ok gets kita sana malagpasan mo yan")
print("")

user_entry = (nameinput, ageinput, addressinput, emailinput, feelingrn)
print (f"SO ITO PERSONAL INFORMATIONS MO HAHAHAH LAGOT KA SAKIN: ")
print ("")
print (f"{user_entry[0]}")
print (f"{user_entry[1]}")
print (f"{user_entry[2]}")
print (f"{user_entry[3]}")
print (f"sabi niya {user_entry[4]}")
