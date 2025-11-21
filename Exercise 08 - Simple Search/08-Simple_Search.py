names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
ques_1 = input("Would you like to see a list of people? (Y/N) ")

if ques_1.lower() == "y":
    print(names)
    search = input("Choose your Character! ").lower().title()
else:
    print("\nThank you for trying!")
    exit()


if search in names:
    print(f"{search} is found")
else:
    print("Name not found.")