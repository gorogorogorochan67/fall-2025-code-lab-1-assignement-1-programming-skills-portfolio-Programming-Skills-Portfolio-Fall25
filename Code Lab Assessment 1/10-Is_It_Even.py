def function(number):
    number = number % 2

    if number == 0:
        return "\nIt is even."
    else:
        return "\nIt is odd."

def main():
    number = int(input("Enter number of choice: "))
    print(f"{function(number)}")
    repeat = input("\nWould you like to try again? (Y/N) ")
    if repeat == "y":
        main()       
    else:
        print("\nThank you for trying!")
        exit()

main()