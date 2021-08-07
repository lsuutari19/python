import json
import sys
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load( open( "data/data.json", "r" ) )

def find_meaning(word):
        return(" ".join( data[word] ) )


def main():
    user_input = input("Enter a word: ")
    
    while True:
        i = ""
        for i in data.keys():
            print(SequenceMatcher(None, user_input, i).ratio())

            if SequenceMatcher(None, user_input, i).ratio() > 0.9:
                print(find_meaning(i))
                main()

            elif SequenceMatcher(None, user_input, i).ratio() <= 0.9 and SequenceMatcher(None, user_input, i).ratio() >= 0.7:
                user_input2 = input("Did you mean {}? Y/N: ".format(i))
                if user_input2 == "Y".lower():
                    print(find_meaning(i))

                main()

        if user_input == "Q":
            sys.exit()

        else:
            print("{} not found in data.".format(user_input))
            user_input = ""
            main()

main()
