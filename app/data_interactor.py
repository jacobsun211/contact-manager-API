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
    
    def get_all_contacts():
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        return contacts

    def create_contact(contact: dict):
        sql = f"INSERT INTO contacts (first_name, last_name, phone_number) \
                VALUES ('{contact["first_name"]}', '{contact["first_name"]}', '{contact["phone_number"]}')"
        cursor.execute(sql)

        conn.commit()
        print("created")
        return "success"
    

# new = {"first_name":"moshe","last_name":"cohen","phone_number":"628162"}  
# Contacts.create_contact(new)
rows = Contacts.get_all_contacts()
print(Contacts.sql_to_dict(rows))






















cursor.close()
conn.close()