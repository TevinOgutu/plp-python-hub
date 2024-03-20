import json
from difflib import get_close_matches

# Load JSON data into a dictionary
with open('data.json') as f:
    data = json.load(f)

# Function to get the definition of a word
def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:  # If user enters a capitalized word
        return data[word.title()]
    elif word.upper() in data:  # If user enters an uppercase word
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        closest_match = get_close_matches(word, data.keys())[0]
        user_choice = input(f"Did you mean '{closest_match}'? (y/n) ").lower()
        if user_choice == 'y':
            return data[closest_match]
        else:
            return "Sorry, the word is not in the dictionary."
    else:
        return "Sorry, the word is not in the dictionary."

# Get word from user
word = input("Enter a word: ")

# Get the definition
definition = get_definition(word)
print(definition)
