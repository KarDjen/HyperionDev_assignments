# we provide the relevant string. Alternatively, we could ask user to prompt a sentence instead
user_input = 'LiTTle JoHn LoVEs NutElLa.'

# Program that reads a string and makes each lowercase an uppercase and vice-versa
result_after_conversion = ''
for char in user_input:
    if char == char.lower():
        char = char.upper()
        result_after_conversion += char
    else:
        char = char.lower()
        result_after_conversion += char
print(result_after_conversion)

# Program that converts alternate words in uppercase and the others in lowercase starting with lowercase (pairs)

# Method 1: without using "".join(string_list)
result_method1 = ''
i = 0
result1 = user_input.split(' ')
for i in range(0, len(result1)):
    if i % 2 == 0:
        word = result1[i].lower()
        result_method1 += word + ' '
    else:
        word = result1[i].upper()
        result_method1 += word + ' '
print(result_method1)

# Method 2: with using "".join(string_list)
list_strings = []
for i in range(0, len(result1)):
    if i % 2 == 0:
        word = result1[i].lower()
        list_strings.append(word)
    else:
        word = result1[i].upper()
        list_strings.append(word)

result_method2 = ' '.join(list_strings)
print(result_method2)

