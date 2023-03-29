""" 
I am not using Windows. Please let me know any alternative instructions.

Note: I have not addessed the last blank space between "dog" and the final point.
It seems to be removed in the PDF file DS T02 at page 11.
"""

# Save the sentence as a string.
string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Ouput the sentence by replacing every "!" with a blank space.
string_replace = string.replace("!", " ")
print(string_replace)

# Output the sentence previously used in uppercases.
string_uppercase = string_replace.upper()
print(string_uppercase)

# Output the sentence in reverse.
string_reverse = string_replace[44::-1]
print(string_reverse)