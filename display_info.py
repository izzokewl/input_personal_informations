def search_user():
    print("hanapin ko yan wait....\n")

    try:
        with open("user_entries.txt", "r") as file:
            entries = file.read().strip().split("\n\n")

        if not entries:
            print("wala naman laman yung file lagay ka muna entries")
            return

        while True:
            try:
                search_name = input("Search full name: ").title()
                if any(char.isdigit() for char in search_name):
                    raise ValueError("HOI BAT MAY NUMBER PANGALAN MO! ULET")
                break
            except ValueError as error:
                print(error)

        print(f"\nkilangan mo ba si {search_name}")

        found = False
        for entry in entries:
            if search_name in entry:
                print("\nnahanap ko sha baks")
                print(entry)  
                found = True
                break

        if not found:
            print(f"\nwala naman dito baks")

    except FileNotFoundError:
        print("lagay ka muna entries baks, excited ka")

search_user()
