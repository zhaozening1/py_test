import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='chat')



def selectUserByUP(uname, psd):
    try:
        temp = "select * from user where username='%s' and password='%s'" % (uname, psd)
        cursor = conn.cursor()
        cursor.execute(temp)
        result = cursor.fetchone()
        cursor.close()
        conn.commit()
    except:
        conn.close()
    return  result

def insertUser(uname, pwd):
    sql = "insert into user(username, password) values('%s', '%s')" % (uname, pwd)
    try:
        cursor = conn.cursor()
        effect_row = cursor.execute(sql)
        cursor.close()
        conn.commit()
        return 1
    except:
        conn.rollback()
        return 0


def updatePsw(uname, pwd):
    sql = "update user set password='%s' where username='%s' " % (pwd, uname)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return 1
    except:
        conn.rollback()
        return 0


def deleteUserByUsername(uname):
    sql = "delete from user where username = '%s'" % (uname)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return 1
    except:
        conn.rollback()
        return 0


