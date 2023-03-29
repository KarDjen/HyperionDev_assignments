# program to validate that the user provides at least two names
while True:
    full_name = input("Please enter your full name: ")

    # condition 1: absence of input
    if len(full_name) == 0:
        print("You haven’t entered anything. Please enter your full name.")
        
    # condition 2: input is less than 4 (not enough characters)
    elif len(full_name) < 4:
        print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
        
    # condition 3: input is more than 25 (too many characters)
    elif len(full_name) > 25:
        print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
        
    # condition 4: check for first name and last name
    elif " " not in full_name:
        print("You have not entered a valid full name. Please make sure to include both your first and last name.")
        
    # greetings
    else:
        print("Thank you for entering your name.")
        break