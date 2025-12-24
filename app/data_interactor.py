import mysql.connector




conn = mysql.connector.connect(
    host="localhost",   # change to "mysql" when im opening the api container 
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
    @staticmethod
    def sql_to_dict(rows):
        contacts_dict = []
        for contact in rows:
            row = {"id":contact[0],
             "first_name":contact[1],
             "last_name":contact[2],
             "phone_number":contact[3],
             }
            contacts_dict.append(row)
        return contacts_dict
    
    @staticmethod
    def get_all_contacts():
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        return contacts

    @staticmethod
    def create_contact(contact: dict):
        cursor.execute( 
            f"INSERT INTO contacts (first_name, last_name, phone_number) \
            VALUES ('{contact["first_name"]}', '{contact["last_name"]}', '{contact["phone_number"]}')")
        conn.commit()
        return cursor.rowcount > 0
    
    @staticmethod
    def update_contact(id,new_first_name,new_last_name,new_number):  # need to change to get dict and not parameters, watch create_contact for refrence
        cursor.execute(
            f"UPDATE contacts \
            SET first_name = '{new_first_name}', last_name = '{new_last_name}', phone_number = '{new_number}' \
            WHERE id = '{id}';")
        conn.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete_contact(id):
        cursor.execute(
            f"DELETE FROM contacts \
            WHERE id = '{id}';")
        conn.commit()
        return cursor.rowcount > 0


# new = {"first_name":"moshe","last_name":"cohen","phone_number":"628162"}  
# Contacts.create_contact(new)
# Contacts.update_contact(1,'jake','sun','75678')
# Contacts.delete_contact(2)
# rows = Contacts.get_all_contacts()
# print(Contacts.sql_to_dict(rows))














# cursor.close()
# conn.close()