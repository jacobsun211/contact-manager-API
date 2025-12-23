import os
import mysql.connector



conn = mysql.connector.connect(
    host="localhost",   # change to "mysql" when im opening the api con 
    port=3008,
    user="user",
    password="7618",
    database="db",
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()

for row in rows:
    print(row)


class Contacts:
    def sql_to_dict(rows):
        contacts_dict = {}
        for i,contact in enumerate(rows):
            row = {"id":contact[0],
             "first_name":contact[1],
             "last_name":contact[2],
             "phone_number":contact[3],
             }
            contacts_dict[i + 1] = row
        return contacts_dict


print(Contacts.sql_to_dict(rows))






















cursor.close()
conn.close()