def search_user():
    try:
        with open("user_entries.txt", "r") as file:
            entries = file.read().strip().split("\n\n")

        if not entries:
            print("wala naman laman yung file lagay ka muna entries")
            return

        while True:
            try:
                search_name = input("Enter your full name: ").title()
                if any(char.isdigit() for char in search_name):
                    raise ValueError("HOI BAT MAY NUMBER PANGALAN MO! ULET")
                break
            except ValueError as error:
                print(error)

        found = False
        for entry in entries:
            if f"Name: {search_name}" in entry:
                print("nahanap ko sha baks:")
                print(entry)  
                found = True
                break

        if not found:
            print(f"\nwala naman dito baks")

    except FileNotFoundError:
        print("lagay ka muna entries baks, excited ka")
