import mysql.connector
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='prescott',
        password='embryriddle',
        database='graya17_db',
        unix_socket='/var/lib/mysql/mysql.sock'
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Teams")
    rows = cursor.fetchall()
    print('Total Rows:', cursor.rowcount)
    for row in rows:
        print("{} {} {}".format(row[0], row[1], row[2]))
except mysql.connector.Error as error:
    print(error)
finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()