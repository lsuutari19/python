import json
import sys
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load( open( "data/data.json", "r" ) )

def main():

    word = input("Enter a word: ").lower()

    if word in data:
        return(data[word])

    elif word.title() in data:
        return(data[word.title()])
    
    elif word.upper() in data:
        return(data[word.upper()])

    elif get_close_matches(word, data.keys()):
        choice = input( "Did you mean {}? Enter Y/N: ".format( get_close_matches(word, data.keys())[0] ) )
        if choice.lower() == "y":
            return(data[get_close_matches(word, data.keys())[0]]) 
        elif choice.lower() == "n":
            return("{} was not found. Please try again.".format(word))
        else:
            return("I didnt understand what you meant.")

    else:
        return("{} was not found. Please try again.".format(word))

search = main()
if type(search) == list:
    for item in search:
        print(item)
else:
    print(search)

