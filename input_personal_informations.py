entries =[]

def user_inputs():
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

 emailinput = input("Enter your Email address: ").lower()

 feelingrn = input ("What are you feeling as of the moment? ")
 print (f"ok gets kita sana malagpasan mo yan")
 print("")
 
 return (nameinput, ageinput, addressinput, emailinput, feelingrn)

while True:
 user_entry = user_inputs()
 entries.append(user_entry)

 with open("user_entries.txt", "a") as file:
    file.write(f"{user_entry[0]}")
    file.write(f"{user_entry[1]}")
    file.write(f"{user_entry[2]}")
    file.write(f"{user_entry[3]}")
    file.write(f"sabi niya {user_entry[4]} daw")

 print (f"SO ITO PERSONAL INFORMATIONS MO HAHAHAH LAGOT KA SAKIN: ")
 print ("")
 print (f"{user_entry[0]}")
 print (f"{user_entry[1]}")
 print (f"{user_entry[2]}")
 print (f"{user_entry[3]}")
 print (f"sabi niya {user_entry[4]} daw")
 print ("")

 while True:
  new_entry = input("Do you still want to add a new entry? (YES/NO): ").upper()
  if new_entry == "YES" or new_entry == "NO":
    break
  else:
    print("baks omayus ka")
    print("")
 
 if new_entry != "YES":
    break

