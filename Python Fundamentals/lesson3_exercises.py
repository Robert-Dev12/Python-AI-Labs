
# ---------- Part A - Conditions ------------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

num = int(input("Input number: "))

if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
else:
    print("number is zero")



# ---------- Task 2 ------------------------------

age = int(input("What is your age: "))

if age >= 65:
    print("you have retired")
elif age >= 30 and age < 65:
    print("you hare an adult")
elif age >= 18 and age < 30:
    print("you are an young adult")
else:
    print("you are a child")



# ---------- Task 3 ------------------------------

username = input("username: ")

if username == "student":                     # checks username
    password = input("password: ")            
    if password == "1234":                    # checks password
        print("password correct")
    else:
        print("password false")
else:
    print("username false")




# ---------- Part B - Truthy, falsy, membership ---------------------------------------------------------------------------------

# ---------- Task 2 ------------------------------

language_list = ["Python", "Java", "C++", "C#", "Pascal", "Rust"]

language = input("Input langauge: ").capitalize()                   # capitalize converts the first char to upper case

if language in language_list:
    print("In the list")
else:
    print("Not in the list")



# ---------- Task 3 ------------------------------

users_blocked =["anders", "bob", "julia", "chris"]

user = input("Enter username: ")

if user in users_blocked:
    print("You are blocked!")
else:
    print("You may enter!")



# ---------- Task 4 ------------------------------

age = int(input("Your age: "))

if not age < 30 :
    print("you are an adult")
elif not age < 18:
    print("you are an young adult")
else:
    print("you are an child")




# ---------- Part C - For loops -------------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

names = ["Anders", "Julia", "Bob", "Charlie"]
i = 0

for name in names:
    i += 1
    print(f"{i}. Hey, {name}")



# ---------- Task 2 ------------------------------

for num in range(1,51):
    if num % 2 == 0:                    # checks even number
        print(num)



# ---------- Task 3 ------------------------------

numbers = [5, 10, 2, 24, 32, 8]
sum = 0

for num in numbers:
    sum += num                         

print(sum)



# ---------- Task 4 ------------------------------

numbers = [5, 10, 2, 24, 32, 8]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num= num

print(max_num)



# ---------- Task 5 ------------------------------

words = ["Python", "Java", "JavaScript", "Rust", "C++", "Pascal", "Perl", "Assembly"]
count = 0

for word in words:
    if len(word) > 5:                   # checks if the word has more than five chars
        count += 1

print(count)



# ---------- Task 7 ------------------------------

movie = {
    "name" : "The Green Mile",
    "genre" : "Drama",
    "year" : 1999
}

for key in movie:                           # gets the keys
    print(key)

for value in movie.values():                # gets the values
    print(value)

for key, value in movie.items():            # unpack key-value pair
    print(key, value)





# ---------- Part D - Range, enumerate, nested loops ----------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

for num in range(10, 0, -1):                # range from 10 to 1 (-1 gives reversed order)
    print(num)



# ---------- Task 2 ------------------------------

num = int(input("Input number: "))
multi = 0
for i in range(1, 11):
    multi = i * num
    print(f"{i} * {num} = {multi}")



# ---------- Task 3 ------------------------------

playlist = ["Billie Jean", "Smooth Criminal", "Beat it", "Bad", "Thriller"]

for i, song in enumerate(playlist, start=1):                 # enumerate givs both index and the value
    print(i, song)



# ---------- Task 4 ------------------------------

for x in range(1,4):
    for y in range(1, 5):
        print(x,y)




# ---------- Part E - While loops -----------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

count = 10

while count >= 0:
    print(count)
    count -= 1



# ---------- Task 2 ------------------------------

password = input("Password: ")

while password != "student":
    print("incorrect password, try again!")
    password = input("Password: ")

print("correct password")



# ---------- Task 3 ------------------------------

while True:
    menu_val = input("Menu:\n 1. Log in \n 2. Account\n 3. Settings \n 4. quit\n Select: ")
    if menu_val == "quit":
        print("You selected: ", menu_val)
        break
    else:
        print("You selected: ", menu_val)



# ---------- Task 4 ------------------------------

total = 0
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    total += num

print("total: ", total)



# ---------- Part F - Break and continue -----------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

for num in range(1, 101):
    if num % 7 == 0 and num % 9 == 0:
        print("number", 63, "is divisible with 7 and 9")
        break



# ---------- Task 2 ------------------------------

strings =["Python", "Java", "", "C++", "", "Rust"]

for string in strings:
    if not string:
        continue
    print(string)



# ---------- Task 3 ------------------------------

names =["Anders", "Julia", "Charlie", "Bob"]

for name in names:
    if name == "Bob":
        print(name, "found!")
    else:
        print(name, "not found")



# ---------- Task 4 ------------------------------

numbers = [10, -5, 20, -99, 150, 999]

for num in numbers:
    if num == 999:
        break
    elif num < 0:
        continue
    print(num)




# ---------- Part G - Console study tracker -------------------------------------------------------------------------------------

sessions = [
    {"subject": "Python", "minutes": 30},
    {"subject": "SQL", "minutes": 60},
    {"subject": "LLM", "minutes": 90},
    {"subject": "Science", "minutes": 45},
    {"subject": "Python", "minutes": 60},   
    {"subject": "LLM", "minutes": 30},
    {"subject": "SQL", "minutes": 45},
    {"subject": "English", "minutes": 60},
    {"subject": "Science", "minutes": 90},
    {"subject": "English", "minutes": 30},    
]    

total_min = 0

for session in sessions:
    total_min += session["minutes"]          # calculates total minutes

print("Total minutes: ", total_min)



# calculate total minutes per subject in dictionary
subject_min = {}
for session in sessions:
    subject = session["subject"]
    minutes = session["minutes"]

    # adds value of the key or 0 of no key is found
    subject_min[subject] = subject_min.get(subject, 0) + minutes 

print(subject_min) 


# Find longest study session
max_session = sessions[0]["minutes"]

for session in sessions:
    if session["minutes"] > max_session:
        max_session = session["minutes"]            

print(max_session)


# Menu
while True:
    menu_value = input("Menu, chose a number:\n 1. All sessions \n 2. Total time\n 3. Filter by subject \n 4. Quit\n Select: ")

    if menu_value == "1":
        for session in sessions:
             print(session)

    elif menu_value == "2":
         print("Total time: ", total_min)

    elif menu_value == "3":
        subject = input("Chose a subject: ")
        for session in sessions:
            if session["subject"] == subject:
                print(f"Subject: {session["subject"]}, minutes {session["minutes"]}")

    elif menu_value == "4":
        break

    print("\n")
