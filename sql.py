import mysql.connector
from mysql.connector import errorcode
import kairo
import datetime

dir = './templates/files'

#queries
add_stud = ("INSERT INTO stud "
            "(first_name, last_name, address, city, state, phone) "
            "VALUES (%s, %s, %s, %s, %s, %s)")

mark_atten = ("INSERT INTO atten "
            "(id, date) "
            "VALUES (%s, %s)")

summ = ("SELECT a.id, CONCAT(s.first_name,' ', s.last_name), a.date FROM atten AS a INNER JOIN stud AS s ON a.id=s.id ")

def regist(formd,img):        #form data in dictionary form and image

    try:
        cnx = mysql.connector.connect(user='dat', password='Qwerty,12',
                                    host='127.0.0.1',
                                    database='employees')

        data = (formd['first_name'], formd['last_name'], formd['address'], formd['city'], formd['state'], formd['phone'])

        cursor = cnx.cursor()
        cursor.execute(add_stud, data)
        id=str(cursor.lastrowid)
        print("-----------------------",img)
        fil=str(dir)+"/"+str(img)
        print("-----------------------",fil)
        gal='student'
        print("-------",id,"--------")
        kairo.enroll(fil,id,gname = 'test')
        cnx.commit()
        cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


    return

def atten(im):                 #getting image and marking attendance
    try:
        cnx = mysql.connector.connect(user='dat', password='Qwerty,12',
                                    host='127.0.0.1',
                                    database='employees')
        print("-----------------------",im)
        fil=str(dir)+"/"+str(im)
        print("-----------------------",fil)
        result = kairo.recog(fil)
        if (str(result['images'][0]['transaction']['status']) == 'failure'):
            print(result)
            return 0
        else:
            a = str(result['images'][0]['candidates'][0]['subject_id'])
            date = str(datetime.datetime.now())
            data = (a, date)
            cursor = cnx.cursor()

            cursor.execute(mark_atten, data)
            cnx.commit()
            cursor.close()
            cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return 0
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return 0
        else:
            print(err)
            return 0

    return 1


def summary():
    try:
        cnx = mysql.connector.connect(user='dat', password='Qwerty,12',
                                    host='127.0.0.1',
                                    database='employees')

        cursor = cnx.cursor()
        cursor.execute(summ)
        result = list(cursor)

        print('####',result)
        cursor.close()
        cnx.close()
        return result

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return 0
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return 0
        else:
            print(err)
            return 0
    return

# cnx = mysql.connector.connect(user='dat', password='Qwerty,12',
#                               host='127.0.0.1',
#                               database='employees')

try:
    cnx = mysql.connector.connect(user='dat', password='Qwerty,12',
                                host='127.0.0.1',
                                database='employees')


    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
