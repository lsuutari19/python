import mysql.connector
from difflib import get_close_matches

def est_connection():
    connection = mysql.connector.connect(
        user = "ardit700_student",
        password = "ardit700_student",
        host = "108.167.140.122",
        database = "ardit700_pm1database"
)   
    return connection

def look_for_word(query, con):
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def translate(con):
    word = input("Please enter a word or enter Q to quit: ")
    while True:
        if word != "Q":
            query = "SELECT * FROM Dictionary WHERE Expression = '{}' ".format(word)
            results = look_for_word(query, con)
            temp = ""
            if results:
                for result in results:
                    temp += result[1] + "\n"
                print(temp)
                translate(con)
            else:
                query = "SELECT * FROM Dictionary"
                results = look_for_word(query, con)
                all_words = [item[0] for item in results]
                
                if len(get_close_matches(word, all_words, cutoff = 0.8)) > 0:
                    yesno = input("Did you mean {}. Enter Y/N: ".format(get_close_matches(word, all_words, cutoff = 0.8)[0]))
                    if yesno.lower() == "y":
                        suggestion = get_close_matches(word, all_words, cutoff = 0.8)[0]
                        query = "SELECT * FROM Dictionary WHERE Expression = '{}' ".format(suggestion)
                        results = look_for_word(query, con)
                        if results:
                            for result in results:
                                temp += result[1] + "\n"
                            print(temp)
                            translate(con)
                    else:
                        print("The word in question does not exist in the database. ")
                        translate(con)
                else:
                    print("Could not find {}. Please double check your word.".format(word))
                    translate(con)
                    
        break

        




con = est_connection()
print( translate(con) )

