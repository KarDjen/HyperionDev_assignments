import math

# user choice of calculator between 'investment' or 'bond'
user_choice = input(("""
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: """))

# convert to lowercase in all cases
user_calculator = user_choice.lower()

while True:
    # Error handling if not 'bond' or 'investment'
    if user_calculator in ['bond', 'investment']:

        # Investment calculator
        if user_calculator == 'investment':

            # Error handling if values entered are not of correct type
            while True:
                try:
                    amount_money_depositing = int(input('Please enter the amount of money you are depositing: ')) # 'P'
                    interest_rate = float(input('Please enter the interest rate as a percentage (numbers only): ')) # to be divided by 100 to find 'r'
                    years_of_investment = int(input('Please enter the number of years you are planning on investing: ')) # 't'
                    break
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue

            while True:
                interest = input("Do you want 'simple' or 'compound' interest? ").lower()
                if interest == 'simple' or interest == 'compound':
                    break
                else:
                    print("Invalid input. Please choose 'simple' or 'compound'.")

            # return on investment if 'simple' interest is selected
            if interest.lower() == 'simple':

                # interest on investment with simple interest = P*(1 + r*t)
                result = round(amount_money_depositing * (1 + (interest_rate / 100) * years_of_investment))
                print(f'The amount of interest you will earn on your investment is {result}.')
                break

            # return on investment if 'compound' interest is selected
            elif interest.lower() == 'compound':

                # interest on investment with compound interest = P * math.pow((1 + r), t)
                result = round(amount_money_depositing * math.pow((1 + (interest_rate / 100)), years_of_investment))
                print(f'The amount of interest you will earn on your investment is {result}.')
                break

        # Bond repayment calculator
        else:

            # Error handling if values entered are not of correct type
            while True:
                try:
                    present_value_house = int(input("Please enter the value of the house: ")) # 'P'
                    annual_interest_rate = float(input('Please enter the interest rate as a percentage (numbers only): '))
                    number_of_months = int(input('Please enter the number of months you expect to take to repay: ')) # 'n'
                    break
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue

            monthly_interest_rate = (annual_interest_rate/100)/12 # 'i'

            # repayment = (i * P)/(1 - (1 + i)**(-n))
            repayment = round((monthly_interest_rate * present_value_house)/(1-(1 + monthly_interest_rate)**(-number_of_months)))

            print(f'The amount you will have to repay each month is {repayment}.')
            break
    else:
        user_choice = input("This is not a valid entry. Please enter either 'investment' or 'bond': ")
        user_calculator = user_choice.lower()