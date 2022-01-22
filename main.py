# IMPORTS
import random
import time
##############################################
# CUSTOMIZATION
## Words correspond to added words.
## Prompts are prompts that CANNOT appear.
## These tables only correlate to their specific languages.

EN_WORDS = []
EN_PROMPTS = []

FR_WORDS = []
FR_PROMPTS = []

BANNED_PROMPTS = []
ADDED_WORDS = []
## BANNED_PROMPTS and ADDED_WORDS are for ALL languages.

LETTERS_FOR_LIFE_OPT = True
LETTERS_FOR_LIFE = "abcdefghijlmnopqrstuv"
## LETTERS_FOR_LIFE_OPT is an option for whether you should gain lives for using all the letters listed in LETTERS_FOR_LIFE.

STARTING_LIVES = 3
MAX_LIVES = 5

##############################################
# MISC

heart = "♡ "

clear = "\n" * 100
small_clear = "\n" * 1

lives = STARTING_LIVES

run = True

accented_letters = [
  "é",
  "à",
  "è",
  "ù",
  "â", 
  "ê", 
  "î", 
  "ô", 
  "û",
  "ç",
  "ë", 
  "ï", 
  "ü"
]

letters_remaining = []
##############################################
# PICK LANGUAGE

language = None

while language == None:
  print(clear)
  lang = input("""
Welcome, what language would you like to play in?
Available Options:
EN
FR\n\n""")

  if lang.upper() == "EN":
    language = "EN"
    for x in EN_WORDS:
      ADDED_WORDS.append(x)
    for x in EN_PROMPTS:
      BANNED_PROMPTS.append(x)
  elif lang.upper() == "FR":
    language = "FR"
    for x in FR_WORDS:
      ADDED_WORDS.append(x)
    for x in FR_PROMPTS:
      BANNED_PROMPTS.append(x)



# GET WORDS

AVAILABLE_WORDS = []
words = open('dict_' + language + '.txt','r')
for each in words:
  AVAILABLE_WORDS.append(each[0:-1])

# FUNCTIONALITY
def refillLetters():
  for x in LETTERS_FOR_LIFE:
      letters_remaining.append(x.lower())

def generatePrompt():

  if random.randint(0,1) == 0:
    x = 2
  else:
    x = 3
  
  success = None

  while success != True:
    success = True
    random_word = random.randint(0,len(AVAILABLE_WORDS))
    chosen_word = AVAILABLE_WORDS[random_word]

    for letter in accented_letters:
      if letter in chosen_word:
        success = False
      
  random_letter = random.randint(0,len(chosen_word)-x)
  letters = chosen_word[random_letter:random_letter+x]

  prompt = letters
  return prompt, chosen_word

print(clear)
turn = 0
refillLetters()

while run == True:

  if lives <= 0:
    pause = input("You lose! Press any key to start over.")
    lives = STARTING_LIVES
    letters_remaining = []
    refillLetters()

  print(clear)
  for character in letters_remaining:
    print(character)
  print(small_clear)
  prompt, word = generatePrompt()
  print(lives * heart)
  print(prompt.upper())
  response = str(input())

  in_words = False
  in_prompt = False
  success = " also"

  if response == "stop":
    run = False

  if (response.lower() in ADDED_WORDS):
    in_words = True
  elif (response.lower() in AVAILABLE_WORDS):
    in_words = True

  if (prompt.lower() in response.lower()):
    in_prompt = True

  if (in_words == False or in_prompt == False):
    lives -= 1
    success = ""
  else:
    for x in letters_remaining:
      if x in response.lower():
        n = letters_remaining.index(x)
        letters_remaining.pop(n)

    
  print("You" + success + " could have used:\n"+word)

  if len(letters_remaining) == 0:
    if LETTERS_FOR_LIFE_OPT and lives != MAX_LIVES:
      lives += 1
      refillLetters()

print(clear)
print("ratio + you fell off")
