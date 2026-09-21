
# ---------- Part A - Python basics ----------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

# print("Robert")
# print("Python + AI")
# print("Diffrent datatypes")




# ---------- Task 2 ------------------------------

# name = "Anders"                                     # variable holds refrences to an object (datatype)
# age = 35
# height = 1.78
# curr_student = True

# print(name, type(name))
# print(age, type(age))
# print(height, type(height))
# print(curr_student, type(curr_student))



# ---------- Task 3 ------------------------------

# value = 2
# print(type(value))

# value = 2.5
# print(type(value))

# value = "two"
# print(type(value))                # variabel changes data type --> Python is dynamically typed.




# ---------- Task 4 ------------------------------

# numb1 = 5
# numb2 = 3

# print("5 + 3 = ", numb1 + numb2)                    
# print("5 - 3 = ", numb1 - numb2)                    
# print("5 * 3 = ", numb1 * numb2)                    
# print("5 / 3 = ", numb1 / numb2)                    
# print("5 ** 3 = ", numb1 ** numb2)                  # power of
# print("5 // 3 = ", numb1 // numb2)                  # floor division
# print("5 % 3 = ", numb1 % numb2)                    # modulo




# ---------- Task 5 ------------------------------

# val_str= "5"
# val = int(val_str)                                  # string to int
# print(val, type(val))

# val2 = 5
# val_float = float(val2)                             # int to float
# print(val_float, type(val_float))

# val_str = str(val2)                                 # int to string
# print(val_str, type(val_str))

# val_fstr = f"{val2}"                                # f-strings convertions
# print(val_fstr, type(val_fstr))






# ---------- Part B - User input and calculations -------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

# first_name = input("First name: ")                              # asks for first name
# year_birth = int(input("Your year of birth : "))                # year of birth

# year = 2026
# age = year - year_birth                                         # calculates the age

# print(f"{first_name} is {age} years old")




# ---------- Task 2 ------------------------------

# price_item = int(input("Price of an item : "))                  # asks for price of an item
# discount = int(input("Discount percentage : "))                 # asks for discount percentage

# disount_deci = discount/100                                     # converts to decimal

# final_price = price_item * (1 - disount_deci)                   # calculate final price

# print("Final price: ", final_price)




# ---------- Task 3 ------------------------------

# temp_C = int(input("Temperature in Celcius: "))                 # asks for temp in Celsius

# temp_F = temp_C * 9/5 + 32                                      # converts temp to Fahrenheit

# print("Temperature in Fahrenheit: ", temp_F)




# ---------- Task 4 ------------------------------

# room_length = int(input("Lenght of the room: "))                # asks for length of the room
# room_width = int(input("Width of the room: "))                  # asks for widh of the room

# room_area = room_length * room_width                            # calculates room area
# room_peri = 2*room_length + 2*room_width                        # calculates room perimeter


# print("Room area: ", room_area)
# print("Room perimeter: ", room_peri)




# ---------- Task 5 ------------------------------

# You get value error, program cant convert "hello" (string) to an integer






# ---------- Part C - Strings ---------------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

# sentence = "  I Love Python  "

# print(len(sentence))                                # lenght of sentence
# print(sentence.lower())                             # lowercase
# print(sentence.upper())                             # uppercase
# print(sentence.strip())                             # Romove leading and trailng whitespace
# print(sentence.split())                             # Splits the words




# ---------- Task 2 ------------------------------

# first_name = input("First name: ")                  # asks for first name
# last_name = input("Last name: ")                    # asks for last name

# print(f"Your first name is {first_name} and last name is {last_name}")              # prints using f-string




# ---------- Task 3 ------------------------------

# text = "python programming"

# print(text[0])                                      # first char
# print(text[-1])                                     # last char
# print(text[:6])                                     # first six chars
# print(text[-11:])                                   # last eleven chars
# print(text[::-1])                                   # entire string reversed




# ---------- Task 4 ------------------------------

# first_name = input("First name: ")                  # asks for first name
# last_name = input("Last name: ")                    # asks for last name

# first_name =first_name.strip()                      # remove spaces for first name
# first_name = first_name.lower()                     # covert to lowercase for first name

# last_name =last_name.strip()                        # remove spaces for last name
# last_name = last_name.lower()                       # covert to lowercase for last name

# user_name = first_name[:3] + last_name[:5]          # creates username: first 3 letters of the first name and first 5 letters of the last name

# print(user_name)                   




# ---------- Task 5 ------------------------------

# email = "robert@gmail.com"

# print(email.split("@"))                             # splits email at '@'




# ---------- Task 6 ------------------------------

# text1 = "I Love Java"

# text2 = text1.replace("Java", "Python")             # Replaces 'Java' with 'Python'

# print(text1)
# print(text2)






# ---------- Part D - String investigation --------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

# text = "Pythonic"

# expression to predict:
# text[2]       --> 't'
# text[-5:-2]   --> 'hon'
# text[:3]      --> 'Pyt'
# text[-3:]     --> 'nic'
# text[2:6]     --> 'thon'
# text[2:-4]    --> 'th'
# text[:7:2]    --> 'Ptoi'
# text[1:-2:3]  --> 'yo'

# print(text[2])
# print(text[-5:-2])
# print(text[:3])
# print(text[-3:])
# print(text[2:6])
# print(text[2:-4])
# print(text[:7:2])
# print(text[1:-2:3])





# ---------- Task 2 ------------------------------

# text = "Artifical Intelligence"

# print(text[4:15])                                   # --> 'fical Intel'
# print(text[10:])                                    # --> 'Intelligence'
# print(text[:-13])                                   # --> 'Artifical'
# print(text[::3])                                    # --> 'Aic tlee'
# print(text[2:-2:4])                                 # --> 'tcIle'
# print(text[::-3])                                   # --> 'eelt ciA'





# ---------- Task 3 ------------------------------

# text = "  Artifical_Intelligence  "

# text = text.strip()                                 # Romove leading and trailng whitespace
# text = text.split("_")                              # splits the word at '_'

# print(text)

# text = text.replace("Artifical", "Human")           # Replaces 'Artifical' with 'Human'

# print(text)
# print("Human" in text)                              # Checks if 'Human' is in text




# ---------- Task 4 ------------------------------

# text = "Python"

# text[3] = "-"                           

# print(text)                                         # TypeError: 'str' object does not support item assignment
#                                                     # once a string object is created in memory, its value cannot be changed or modified

# text = text[:3] + "-" + text[4:]                    # first modified way
# text2 = text.replace("h", "-")                      # second modified way

# print(text)
# print(text2)






# ---------- Part E - Registration summary --------------------------------------------------------------------------------------

# first_name  = input("First name: ")                             # asks for first name
# last_name   = input("Last name: ")                              # asks for last name
# city        = input("Your city: ")                              # asks for city
# year_birth  = input("Your year of birth: ")                     # asks for year of birth and converts to an int
# language    = input("Your favourit language: ")                 # asks for programing language

# removing surrounding spaces
# first_name = first_name.strip()
# last_name = last_name.strip()
# city = city.strip()
# year_birth = year_birth.strip()
# language = language.strip()

# print(f"ID: First name: {first_name.upper()}, Last name: {last_name.upper()}, Year of birth: {year_birth}")


# print("Initials: ", first_name[0] + last_name[0])                         # prits the initials
# print("Full name length: ", len(first_name + last_name))                  # prits the length of the full name
# print("Reversed language: ", language[::-1])                              # prits reversed programming language

# age = 2026 - int(year_birth)                                              # calculates the age

# print(f"{first_name.capitalize()} is {age} years old and lives in {city}, his favourite programming language is {language}!")






# ---------- Part F - Stretch challenges ----------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

# total_seconds  = int(input("Input total seconds: "))            # asks for total seconds

# hours = total_seconds // 3600                                   # calculate hours
# minutes = (total_seconds % 3600) // 60                          # calculate minutes
# seconds = total_seconds % 60                                    # calculate remaining seconds

# print(f"Output: {hours}h {minutes}m {seconds}s")                # prints total seconds to hours, minutes and remaining seconds




# ---------- Task 2 ------------------------------

# num = 1234

# num1 = num // 1000                                  # first digit
# num2 = (num // 100) % 10                            # second digit
# num3 = (num // 10) % 10                             # third digit
# num4 = num % 10                                     # fourth digit

# print(num1)
# print(num2)
# print(num3)
# print(num4)




# ---------- Task 3 ------------------------------

# text = input("Input word: ")                                    # asks for first name

# nr_middle_chars = len(text) - 4                                      # number of middle chars

# text = text[:2] + "*" * nr_middle_chars + text[-2:]                  # gets first two chars, last two chars and in the middle is '*'

# print(text)
