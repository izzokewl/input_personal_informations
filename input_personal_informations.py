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
        print ("\ngets kita, pero pwede bang gawin mong numbers yan...\n")

 addressinput = input("Enter your address: ").title()

 while True:
  emailinput = input("Enter your Email address: ").lower()
  if "@" in emailinput and "." in emailinput:
     break
  else:
     print("\nbaks parang mali yan nilagay mu\n")


 feelingrn = input ("What are you feeling as of the moment? ").lower()
 print ("\nok gets kita sana malagpasan mo yan\n")
 
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
    file.write("\n")

 print (f"SO ITO PERSONAL INFORMATIONS MO HAHAHAH LAGOT KA SAKIN: ")
 print ("")
 print (f"{user_entry[0]}")
 print (f"{user_entry[1]}")
 print (f"{user_entry[2]}")
 print (f"{user_entry[3]}")
 print (f"sabi niya {user_entry[4]} daw\n")

 while True:
  new_entry = input("Do you still want to add a new entry? (YES/NO): ").upper()
  if new_entry == "YES" or new_entry == "NO":
    break
  else:
    print("baks omayus ka\n")
    print("")
 
 if new_entry != "YES":
    print("\ngeh baks salamat lista q yan")
    break

