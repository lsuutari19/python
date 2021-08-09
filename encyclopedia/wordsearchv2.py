import json
import sys
from difflib import SequenceMatcher
from difflib import get_close_matches
import pandas


data = json.load( open( "data/data.json", "r" ) )


def main():

    while True:
        word = input("Enter a word: ").lower()
        
        if word in data:
            print("\n".join(data[word]))

        elif word.title() in data:
            print("\n".join(data[word.title()]))
        
        elif word.upper() in data:
            print("\n".join(data[word.upper()]))

        elif get_close_matches(word, data.keys()):
            choice = input( "Did you mean {}? Enter Y/N: ".format( get_close_matches(word, data.keys())[0] ) )
            if choice.lower() == "y":
                print("\n".join((data[get_close_matches(word, data.keys())[0]])))
            elif choice.lower() == "n":
                print("{} was not found. Please try again.".format(word))
            else:
                print("I didnt understand what you meant.")

        else:
            print("{} was not found. Please try again.".format(word))
        
        while True:
            decision = input("Would you like to search for another word? Y/N: ")

            if decision == "Y":
                break
            elif decision == "N":
                sys.exit()
            else:
                print("Im sorry that isn't a choice.")
                continue

search = main()
