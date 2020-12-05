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
    print('')
    print('')
    print('\x1b[5;31m' + '     Hello!' + '\x1b[0m')
    print('')
    print('\x1b[3;31m' + '     Here you can find out what team you are on this soccer season!' + '\x1b[0m')
    print('')
    print('\x1b[3;31m' + '     To search the database of all the soccer teams this season, ' + '\x1b[0m')
    print('\x1b[3;31m' + "     please enter the player's full name below. (Format: [First Last])" + '\x1b[0m');
    print('')
    print('')
    
    print('Type below and press ENTER: ')
    print('')
    name = raw_input();
    args = [name]
    print('')
    print('\x1b[5;31m' + '     Congratulations!!!' + '\x1b[0m')
    print('')
    print('\x1b[3;31m' + ' Your team is:' + '\x1b[0m')
    print('')
    cursor.callproc('teamPlayer', args)
    for result_cursor in cursor.stored_results():
      for row in result_cursor:
        print('\x1b[1;36m' + '*' *26 + '\x1b[0m')
        print('\x1b[1;36m' + '*' + ' ' *24 + '*' + '\x1b[0m')
        print('\x1b[1;36m' + '*' + ' ' * 10 + '\x1b[5;36m' + str(row[0]) + '\x1b[0m' + '\x1b[1;36m' + ' ' *10 + '*' + '\x1b[0m')
        print('\x1b[1;36m' + '*' + ' ' *24 + '*' + '\x1b[0m') 
        print('\x1b[1;36m' + '*' *26 + '\x1b[0m')
        print('')

except mysql.connector.Error as error:
    print(error)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()