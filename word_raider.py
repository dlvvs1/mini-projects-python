# WORD RAIDER
# A word guessing game where players try to guess a hidden word by suggesting letters. the words are tollywood movies.
# there are three levels of difficulty: EASY, MEDIUM, and HIGH. Each level has a different set of words to guess from.

import random

def get_random_word(word_list):
    word = (random.choice(word_list)).lower()
    display = "_ " * len(word)
    chances = 6
    return word, display, chances

dic = {1: "EASY", 2: "MEDIUM", 3: "HIGH"}
print("WELCOME TO TOLLYWOOD WORD RAIDER!")
print("Select a difficulty level: \n1. EASY - MOVIES FROM 2015-2025\n2. MEDIUM - EASY-MOVIES FROM 2000-2014\n3. HIGH - MOVIES BEFORE 2000")

try:
     level = int(input("Enter your choice (1, 2, or 3): "))
except ValueError:
     print("Invalid input. Please enter a number (1, 2, or 3).")
     exit()

if level not in dic:
    print("Invalid choice. Please select a valid difficulty level.")
    exit()

if (level == 1):
     list_easy = ["bahubali" , "druva" , "liger" , "katamarayudu" , "sarrainodu" ,"temper"]
     word, display, chances = get_random_word(list_easy)
elif(level == 2):
     list_medium = ["billa" , "chirutha" , "gamyam" , "happy" , "kushi" ,"okkadu"]
     word, display, chances = get_random_word(list_medium)
else:
     list_high = ["garanamogudu" , "pathalabhairavi" , "geethanjali" , "KshanaKshanam"]
     word, display, chances = get_random_word(list_high)
     
guessed = []

while chances > 0:
     print(f"guess the movie from level {level}: {display}")
     guess = input("Enter a letter: ").lower()

     if guess in guessed:
          print("You already guessed that letter!")
          continue
     guessed.append(guess)

     if guess not in word:
          chances -= 1
          print(f"Wrong guess! You have {chances} chances left.")

     display = ""
     for letter in word:
          if letter in guessed:
                    display += letter + " "
          else:
               display += "_ "
     
     if "_" not in display:
          print(f"Congratulations! You guessed the movie: {word}")
          break

if chances == 0:
     print("your chance are over! try again next time. ")