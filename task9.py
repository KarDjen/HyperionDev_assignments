# Display the options that the user can select
print("""Please select one option below:
            -- Enter '1': provide two numbers and an operator to find the result.
            -- Enter '2': read all of the equation(s) from a txt file and print out all equation(s) with the result(s).
        """)

while True:
    try:
        # Prompt user to make a choice between 1 and 2
        Option = input('Your choice: ')
        if Option not in ['1', '2']:
            raise ValueError("Invalid option. Please enter 1 or 2.")
        break

        # Raise exception if value entered is not valid
    except ValueError as err:
        print(err)
        continue

# Option 1: user enter 2 numbers and an operator
if Option == '1':
    # Initialize a list that will store result(s)
    results = []
    while True:
        while True:
            try:
                # Prompt user to enter two numbers
                number_one = int(input('Enter a number: '))
                number_two = int(input('Enter another number: '))
                break

            # Raise exception if value entered is not valid
            except ValueError:
                print('Invalid input. Please try again.')
                continue

        while True:
            try:
                # Prompt user to enter the operation
                operation = input('Enter the operation (+, -, *, /, %, **, or //): ')
                if operation not in ['+', '-', '*', '/', '%', '**', '//']:
                    raise ValueError("Invalid operation. Please enter one of the following: +, -, *, /, %, **, or //.")
                break

            # Raise exception if value entered is not valid
            except ValueError as err:
                print(err)
                continue

        # Perform the relevant operations with error handling (if any)
        # CORRECTED: We remove break statement so that we don't exit the loop
        if operation == '+':
            result = number_one + number_two
        elif operation == '-':
            result = number_one - number_two
        elif operation == '*':
            result = number_one * number_two
        elif operation == '/':
            try:
                result = number_one / number_two
            except ZeroDivisionError:
                print("Division by zero is not possible. Please try again.")
                continue
        elif operation == '%':
            try:
                result = number_one % number_two
            except ZeroDivisionError:
                print("Modulo not available with 0. Please try again.")
                continue
        elif operation == '**':
            result = number_one ** number_two
        else:
            result = number_one // number_two

        # CORRECTED: Display the result using f-string
        print(f"{number_one} {operation} {number_two} = {result}")
        # CORRECTED: Append the result to our list
        results.append(f"{number_one} {operation} {number_two} = {result}")

        # CORRECTED: Ask user if they want to solve another equation
        while True:
            user_input = input("Do you want to solve another equation? (y/n): ")
            if user_input.lower() in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if user_input.lower() == 'n':
            break

    # Prompt user for the filename to store the results
    filename = input('Enter filename to store results: ')

    try:
        # Write the results to the file
        with open(filename, 'w') as file:
            file.write('\n'.join(results))
        print(f"Your result(s) has/have been saved to {filename}.")

    except Exception as err:
        # Catch any errors that occur when opening or writing to the file
        print(f"Error: {err}")

# Option 2: equation(s) is/are imported from file
else:
    while True:
        try:
            # Prompt user for the name of the file
            filename = input('Please enter the name of your file: ')

            # open and read all content
            with open(filename, 'r') as file:
                equations = file.readlines()

            # for each equation, eval and perform the equation
            for equation in equations:
                result = eval(equation.strip())

                # Print the equation and its result to the terminal
                print(f"{equation.strip()} = {result}")
            break

        except FileNotFoundError:
            # Catch any errors that occur when opening or reading from the file
            print("File not existing")
            continue