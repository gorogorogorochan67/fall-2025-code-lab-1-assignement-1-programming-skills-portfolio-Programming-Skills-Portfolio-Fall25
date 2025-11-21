while True:  # Main program loop
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
#create a list of all the months and their days
    leapyear = input("Is it a leap year? (Y/N): ")
    if leapyear.lower() == 'y':
        months[2] = 29
        #if user says its a leap year, account for that and change the month appropriately
   
    while True:
        try:
            m_choice = int(input("Input a month (by number): "))
            break
        except ValueError:
            print("Oops! only answer by number, Try again!")

    if m_choice in months:
        print(f"{m_choice} has {months[m_choice]} days.")
    else:
        print("Uh Oh! that month doesnt exist!")
        continue  #restart loop

    tryagain = input("Would you like to try again? (y/n): ")
    if tryagain.lower() != 'y':
        print("Thank You!")
        break  #exit the main loop