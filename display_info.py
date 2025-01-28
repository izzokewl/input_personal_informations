while True:
       try:
             search_name = input("Enter your full name: ").title()
             if any(char.isdigit() for char in search_name):
                   raise ValueError("HOI BAT MAY NUMBER PANGALAN MO! ULET")
             break
       except ValueError as error:
            print (error)