password = "12345"
attempts = 5
#set password and attempts
while attempts > 0:
    enter = input("Insert Password: ")
    if enter == password:
        print("Access has been granted!")
        break
    #breaks the code if password is correct
    attempts -= 1
    print(f"Access Denied! you have {attempts} attempts left.")
    #failing the password will display how many attempts you have left

if attempts == 0:
    print("You have failed 5 times, The Authorities have been called.")
    #failing all attempts will break the code too