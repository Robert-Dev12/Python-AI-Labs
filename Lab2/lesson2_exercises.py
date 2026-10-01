# ---------- Part A - Lists -----------------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

languages = ["Ada", "C", "C++", "C#", "Java", "Matlab", "Pascal", "Python"]

print(languages[0])
print(languages[-1])
print(languages[2])
print(languages[1:])



# ---------- Task 2 ------------------------------

languages = ["Ada", "C", "C++", "C#", "Java", "Matlab", "Pascal", "Python"]

print(languages[:4])
print(languages[3:6])
print(languages[2:-2])                    # -2 --> second index from the end
print(languages[::-1])                    # Reverse the list



# ---------- Task 3 ------------------------------

languages = ["Ada", "C", "C++", "C#", "Java", "Matlab", "Pascal", "Python"]

languages.append("Rust")                  # Adds 'Rust' at the end
print(languages)

languages.insert(5, "JavaScript")         # Inserts "JavaScript" at index 5
print(languages)

languages.remove("Java")                  # Removes "Java"
print(languages)

languages.pop(2)                          # Removes "C++" (index 2)
print(languages)



# ---------- Task 4 ------------------------------

numeric = [10, 5, 15, 2]

print("Length:", len(numeric))                    # lenght of the list
print("Min:", min(numeric))                       # min value in the list
print("Max:", max(numeric))                       # max value in the list
print("Sum:", sum(numeric))                       # sum the values in the list



# ---------- Task 5 ------------------------------

numeric = [10, 5, 15, 2]

numeric.sort()                            # Sorts in ascending order
print(numeric)

numeric.sort(reverse=True)                # Sorts in descending order
print(numeric)

new_numeric = sorted(numeric)             # sorted dont change original list, but sort do change the original list

print(numeric)
print(new_numeric)



# ---------- Task 6 ------------------------------

list_a = [1, 2, 3, 4]

list_b = list_a                           # list_b and list_a references to the same list object
list_b.append(5)                          # adds 5 to list_a and list_b

list_c = list_a.copy()                    # creates a new list object, list_c, with copy of list_a (lists refers to diffrent list object)
list_c.append(6)                          # Adds 6 only to the list_c

print(list_a)
print(list_b)               
print(list_c)




# ---------- Part B - Tuples and unpacking --------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

rgb = (132, 77, 212)

red, green, blue = rgb               # Unpacking RGB values

print("Red:", red)
print("Green:", green)
print("Blue", blue)



# ---------- Task 2 ------------------------------

person = ("Victor", 30, "London")

name, age, city = person                        # Unpacking person values

print(f"{name} is {age} years old and lives in {city}")



# ---------- Task 3 ------------------------------

# Tuples are immutble and are used when you need the values to be fixed and not changed, cant change the structure of a tuple



# ---------- Task 4 ------------------------------

Coord_list = [(10, 20), (30, 40), (50, 60), (70, 80)]

Coord1_x = Coord_list[0][0]           # accesses all values individual
Coord1_y = Coord_list[0][1]
Coord2_x = Coord_list[1][0]
Coord2_y = Coord_list[1][1]
Coord3_x = Coord_list[2][0]
Coord3_y = Coord_list[2][1]
Coord4_x = Coord_list[3][0]
Coord4_y = Coord_list[3][1]

print("Coord1 xy:", Coord1_x, Coord1_y)
print("Coord2 xy:", Coord2_x, Coord2_y)
print("Coord3 xy:", Coord3_x, Coord3_y)
print("Coord4 xy:", Coord4_x, Coord4_y)





# ---------- Part C - Sets ------------------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

names = ["Anders", "Julia", "Anders", "Christian", "Julia"]

unique_names = set(names)                               # Converts the list to a set

print("Length of list:", len(names))                    # Compare the lengths before and after                   
print("Length of set:", len(unique_names))



# ---------- Task 2 ------------------------------

Dev1_skill = {"Python", "C#", "Java"}
Dev2_skill = {"Python", "C++", "Pascal"}

print("Shared skills:", Dev1_skill & Dev2_skill)                                # skills they share (Intersection)
print("Skills only Dev1 has:", Dev1_skill - Dev2_skill)                         # skills that only the firts Dev has (Difference)
print("All skills for either person:", Dev1_skill | Dev2_skill )                # all skills that represented by either person (Union)



# ---------- Task 3 ------------------------------

languages = {"Python", "C#", "Java"}

languages.add("C++")                      # Add an element to the set
print(languages)                        

languages.remove("Java")                  # Remove an element to the set
print(languages)                        

print("Python" in languages)              # Checks if Python is a member of languages



# ---------- Task 4 ------------------------------

# A set contains unique values and it prevent to store dublicates values, 
# therfore set is a better choice than list when you need to store items that must be unique

# Real-world problem : A guest list --> Stores the names of people attending a party. Each person should only appear once.





# ---------- Part D - Dictionaries ----------------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

# Dictionaries --> Key-value pairs

laptop = {"brand": "HP",
          "model": "ZBook",
          "RAM":   32,
          "storage": 1000,
          "price": 10000
          }

print("Brand:", laptop["brand"])              # Gets values by key
print("Model:", laptop["model"])
print("RAM:", laptop["RAM"], "GB")
print("Storage:", laptop["storage"], "GB")
print("Price:", laptop["price"], "kr")



# ---------- Task 2 ------------------------------

laptop["price"] = 15000                 # Changes the price
laptop["OS"] = "Win11"                  # Adds a key-value pair
laptop.pop("model")                     # Removes a key

print(laptop)



# ---------- Task 3 ------------------------------

print(laptop.get("brand"))                              # for existing key
print(laptop["brand"])                                  # direct indexing


print(laptop.get("processor"))                          # for missing key, default value is 'None'
print(laptop.get("processor", "Unknown"))               # default value is changed to 'Unknown'

# print(laptop["processor"])                              # direct indexing --> KeyError, Key is missing



# ---------- Task 4 ------------------------------

print(laptop.keys())                        # prints keys
print(laptop.values())                      # prints values
print(laptop.items())                       # prints items



# ---------- Task 5 ------------------------------

courses = {"Python": 160,
         "SQL": 80,
         "ML": 40,
         "LLM": 60,
         "C#": 30
         }

# calculating the total study hours
total_hours = courses["Python"] + courses["SQL"] + courses["ML"] + courses["LLM"] + courses["C#"]

print("Total hours:", total_hours)





# ---------- Part E - Nested collections ----------------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

books = [
    {
     "title" : "The Alchemist",
     "auther":  "Paulo Coelho",
     "pages" :  177,
     "available": True,  
    },
    {
     "title" : "The Hobbit",
     "auther":  "J.R.R Tolkien",
     "pages" :  400,
     "available": True,  
    },
    {
     "title" : "The Hunger Games",
     "auther":  "Suzanne Collins",
     "pages" :  464,
     "available": False,  
    },
    {
     "title" : "Harry Potter and the Sorcerer's Stone",
     "auther":  "J.K Rowling",
     "pages" :  336,
     "available": True,  
    },
    {
     "title" : "The Power of Now",
     "auther":  "Eckhart Tolle",
     "pages" :  191,
     "available": False,  
    }
]



# ---------- Task 2 ------------------------------

print(books[2]["title"])                    # gets the title for the third book
print(books[4]["available"])                # gets the availability för the last book



# ---------- Task 3 ------------------------------

books[3]["pages"] = 350                     # changes the pages for the fourth book
books[1]["year"]  = 2006                    # adds publication year to the second book

print(books[3]["pages"])
print(books[1]["year"])



# ---------- Task 4 ------------------------------

company = {"sales": ["Charlie", "Anna", "Sven"],
           "IT": ["Christian", "Bob"], 
           "developers": ["Anders", "Fabian", "Gloria","Julia"]
           } 

print(company)



# ---------- Task 5 ------------------------------

courses = [
    { "course" : "Python & AI",
      "teacher" : "Aladdin",
      "topics" : ["Python", "SQL", "LLM", "AI agents"]
      },
    { "course" : "Algebra",
      "teacher" : "Katarina",
      "topics" : ["Vector space", "Matrix", "Diagonalization"]
      },
    { "course" : "Electronics",
      "teacher" : "Peter",
      "topics" : ["Analog", "Digital", "Circuits", "Power"]
      }
]

print(courses[1]["topics"][1])                      # prints 'Matrix'





# ---------- Part F - Personal media catalogue -----------------------------------------------------------------------------------

# ---------- Task 1 ------------------------------

# catalogue contains video games
games = [{          
              "title" : "Minecraft",
              "developer" : "Microsoft",
              "genre" : "Survival",
              "year" : 2011
            },
            {
              "title" : "GTA 5",
              "developer" : "Rockstar Games",
              "genre" : "Action-Adventure",
              "year" : 2013
            },
            {
              "title" : "FIFA 23",
              "developer" : "Electronic Arts",
              "genre" : "Sports",
              "year" : 2022
            },
            {
              "title" : "Fortnite",
              "developer" : "Epic Games",
              "genre" : "Battle Royale",
              "year" : 2017
            },
            {
              "title" : "Apex Legends",
              "developer" : "Respawn Entertainment",
              "genre" : "Battle Royale",
              "year" : 2019
            },
            {
              "title" : "NBA 2K26",
              "developer" : "Visual Concepts",
              "genre" : "Sports",
              "year" : 2025
            },
            {
              "title" : "Civilization VII",
              "developer" : "Firaxis Games",
              "genre" : "Turn-Based Strategy",
              "year" : 2025
            },
            {
              "title" : "The Sims 4",
              "developer" : "Maxis",
              "genre" : "Life Simulation",
              "year" : 2014
            }
]



# ---------- Task 2 ------------------------------

games_list = list(games)

print(games_list)



# ---------- Task 3 ------------------------------

unique_genres = {item["genre"] for item in games}                   # gets unique genres

print(unique_genres)



# ---------- Task 4 ------------------------------

num= 0

for game in games:
    num +=1 
    id_nr = 'VG0' + str(num)                                # ID number
    game["identifier"] = (id_nr, game["year"])              # identifier and realese year for each video game

print(games[1]["identifier"])                   # --> 'VG02', 2023



# ---------- Task 5 ------------------------------

# Uppdate operations
games[4]["developer"] = "AI Dev"            # key "developer" -value chenges to 'AI Dev' in game 5
games[1]["engine"]  = "RAGE"                # adds new key-value pair, to game 2

print(games[4]["developer"])
print(games[1]["engine"])

# Nested indexing
print(games[1]["title"])            # --> 'GTA 5'
print(games[5]["genre"])            # --> 'Sports'
print(games[-1]["developer"])       # --> 'Maxis'

# Membership
print('FIFA 23' in games[2]["title"])               # True
print('Microsoft' not in games[0]["developer"])     # False

# Collections methods
print(games[3].keys())                # keys for game 4
print(games[3].values())              # values for game 4
print(games[3].get("title"))          # gets title for game 4
