import mysql.connector

# function returning the cursor of the database
def define_database():
    db = mysql.connector.connect(
        host="FPeco35.mysql.pythonanywhere-services.com",
        user="FPeco35",
        passwd="mysqlDatabase",
        database="FPeco35$inputs"
    )
    return db

def insert_query(database, email, subj, content):
    cur = database.cursor()
    query = "INSERT INTO user_inputs (email, subj, messg) VALUES (%s, %s, %s);"
    cur.execute(query, (email, subj, content))
    database.commit()
    cur.close()
    database.close()
    