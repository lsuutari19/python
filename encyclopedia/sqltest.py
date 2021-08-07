import mysql.connector


connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

user_input = input("Search for a name: ")
cursor = connection.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}' ".format(user_input))
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])

else:
    print("Could not find {} in the database.".format(user_input))

