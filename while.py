# initialize variables
user_number = 0
total = 0
count = 0

while True:
    # keep asking the user to enter a number
    user_number = int(input('Enter a number: '))
    
    # stop requesting if input is -1 and exit the loop
    if user_number == -1:
        break

    total += user_number
    count += 1
    
 # once exited, calculate average   
average = total/count

print(average)