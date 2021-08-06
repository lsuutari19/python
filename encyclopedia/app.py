import json
import sys
from difflib import SequenceMatcher

path = "thesaurus/data/data.json"
data = json.load( open( path, "r" ) )

def find_meaning(word):
        return(" ".join( data[word] ) )


def main():
    user_input = input("Enter a word: ")
    while True:
        if user_input in data:
            print(find_meaning(user_input.lower()))
            main()
        elif user_input == "Q":
            sys.exit()
        else:
            print("{} not found in data.".format(user_input))
            user_input = ""
            main()

main()