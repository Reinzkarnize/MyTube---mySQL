import mysql.connector

conn = mysql.connector.connect(host='localhost', password='a4867787', user='root', database="mytube")

if conn.is_connected():
    cursor = conn.cursor()
    print('Connection established')

    try:
        cursor.execute("INSERT INTO users(username, hash) VALUES('a', "
                       "'pbkdf2:sha256:600000$D3m1BZPNi1CL3oxn$6f41ade5cef6256de81ee15b5181a46003e8b5c5f85f81517553ea969684f21b')")
        conn.commit()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print(rows)
        # for row in rows:
        #     print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()


