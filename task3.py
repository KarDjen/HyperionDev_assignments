# Time taken in minutes by the user to complete swim, cycle, and run events
print("Please enter the time (in minutes) for each event:")
swim_time = int(input("Swimming: "))
cycle_time = int(input("Cycling: "))
run_time = int(input("Running: "))

# Calculate the total time taken to complete the triathlon
total_time = swim_time + cycle_time + run_time

# Display the total time taken to complete the triathlon
print(f"Total time taken to complete the triathlon: {total_time} minutes")

# Display award for the user according to the time taken and criteria provided
if total_time <= 100:
    print ("Award received: Provincial Colours")
elif total_time <= 105:
    print("Award received: Provincial Half Colours")
elif total_time <= 110:
    print("Award received: Provincial Scroll")
else:
    print ("Award received: No award")