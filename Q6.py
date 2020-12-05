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
    print('\x1b[1;36m' + '_' *125 + '\x1b[0m')
    print('')
    print('')
    print('\x1b[3;31m' + '     Hello!' + '\x1b[0m')
    print('')
    print('\x1b[3;31m' + '     This application is for players within the Fall 2019 Soccer Tournament.' + '\x1b[0m')
    print('')
    print('\x1b[3;31m' + '     You can find out your schedule for this tournament along with information such as' + '\x1b[0m')
    print('\x1b[3;31m' + '     who is coaching your team for the game, what team you are playing against, and if it' + '\x1b[0m')
    print('\x1b[3;31m' + '     is your responsibility to bring snacks for the game or not.' + '\x1b[0m')
    print('')
    print('\x1b[3;31m' + '     To search the database please enter your full name, you being a player in the tournament, ' + '\x1b[0m')
    print('\x1b[3;31m' + "     and press the ENTER key." + '\x1b[0m');
    print('\x1b[3;31m' + '     Once you press the ENTER key you will be shown a list of your schedule for the tournament' + '\x1b[0m')
    print('\x1b[3;31m' + '     and also be able to choose what information you would like to view.' + '\x1b[0m')
    print('')
    print('\x1b[3;35m' + '     Good luck and ' + '\x1b[0m' + '\x1b[4;35m' + 'have fun!' + '\x1b[0m')
    print('')
    print('\x1b[1;36m' + '_' *125 + '\x1b[0m')
    print('')
    print('')
    
    name = raw_input('   Please type your first and last name here: ');
    args = [name]
    print('')
    print('')
    print('\x1b[1;36m' + '_' *125 + '\x1b[0m')
    print('')
    print('')
    print('     Hi, ' + name + ', here is your schedule for the Fall 2019 Soccer Tournament: ')
    print('')
    
    cursor.callproc('playerSchedule', args)
    counter = 1
    for result_cursor in cursor.stored_results():
      for row in result_cursor:
        print('\x1b[4;31m' + 'Game #' + str(counter) + '\x1b[0m' + ': You are playing against ' + str(row[1]) + '.')
        print('         Your game is scheduled for:  ' + str(row[2]) + '.')
        print('')
        print('         Would you like to view more information about this game?')
        print('')
        info = raw_input("   Type 'yes' or 'no' : ")
        print('')
        while info == 'yes':
          print('')
          more = raw_input("   Type 'coach' to see who is coaching your game, 'snack' to see if you are bringing snacks, or 'nevermind' : ")
          if more == 'coach':
            print('')
            print('    ' + str(row[4]) + ' is coaching your game against ' + str(row[1]) + '.')
            print('')
            print('')
            print('   Would you like to view more information about this game?')
            print('')
            info = raw_input("    Type 'yes' or 'no' : ")
          elif more == 'snack':
            if row[3] == 1:
              print('')
              print('    You ' + '\x1b[4;31m' + 'are' + '\x1b[0m' + ' scheduled to bring snacks to the game against ' + str(row[1]) + '.')
              print('')
              print('')
              print('   Would you like to view more information about this game?')
              print('')
              info = raw_input("    Type 'yes' or 'no' : ")
            else:
              print('')
              print('    You are ' + '\x1b[4;31m' + 'not' + '\x1b[0m' + ' scheduled to bring snacks to the game against ' + str(row[1]) + '.')
              print('')
              print('')
              print('   Would you like to view more information about this game?')
              print('')
              info = raw_input("    Type 'yes' or 'no' : ")
          else:
            info = 'no'
        counter = counter + 1
        print('')
    print('\x1b[3;35m' + '          Thank you and good luck in all your games!' + '\x1b[0m')
    print('')
    print('')

except mysql.connector.Error as error:
    print(error)

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()