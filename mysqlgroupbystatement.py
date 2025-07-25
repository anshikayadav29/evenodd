import pymysql as mq

try:
    conn = mq.connect(host="localhost", user="root", password="1234", database="school")
    mycursor = conn.cursor()

    print("{:<15}".format("Department"))

    sql = "SELECT dpoint FROM emp GROUP BY dpoint"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    for s in sdata:
        print("{:<15}".format(s[0]))

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
