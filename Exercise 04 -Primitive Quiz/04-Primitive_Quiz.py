quiz = {
    "France": "Paris", 
    "Norway": "Oslo",
    "Portugal": "Lisbon",
    "Italy": "Rome",
    "Netherlands": "Amsterdam",
    "Spain": "Madrid",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Germany": "Berlin",
    "Greece": "Athens"
}
#store a list of 10 countries and their capitals
for country, capital in quiz.items():
    answer = input(f"Define the capital of {country}? ").strip().lower()
    #makes user input ignore capitalisation
    if answer == capital.lower():
        print("You are Correct!")
    else:
        print(f"You are wrong! The correct answer is {capital}.")
    #if user is correct, print respective line
    #if user is incorrect, print a different respective line