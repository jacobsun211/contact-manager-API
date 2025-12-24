import mysql.connector

import uvicorn



class Contacts:
    @staticmethod
    def get_connection():
        conn = mysql.connector.connect(
            host="db",
            port=3306,
            user="user",
            password="7618",
            database="db",)
        cursor = conn.cursor()
        return conn, cursor
        

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
        conn, cursor = Contacts.get_connection()
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        cursor.close()
        conn.close()
        return contacts

    @staticmethod
    def create_contact(first_name, last_name, phone_number):
        conn, cursor = Contacts.get_connection()
        cursor.execute( 
            f"INSERT INTO contacts (first_name, last_name, phone_number) \
            VALUES ('{first_name}', '{last_name}', '{phone_number}')")
        conn.commit()
        new_id = Contacts.new_contact_id()
        return new_id
    

    def new_contact_id():
        conn, cursor = Contacts.get_connection()
        cursor.execute("SELECT MAX(id) FROM contacts;")
        new_contact_id = cursor.fetchone()
        cursor.close()
        conn.close()
        return new_contact_id
    
    @staticmethod
    def update_contact(id,new_first_name,new_last_name,new_number):  # need to change to get dict and not parameters, watch create_contact for refrence
        conn,cursor = Contacts.get_connection()
        cursor.execute(
            f"UPDATE contacts \
            SET first_name = '{new_first_name}', last_name = '{new_last_name}', phone_number = '{new_number}' \
            WHERE id = '{id}';")
        conn.commit()
        return cursor.rowcount > 0

    @staticmethod
    def delete_contact(id):
        conn,cursor = Contacts.get_connection()
        cursor.execute(
            f"DELETE FROM contacts \
            WHERE id = '{id}';")
        conn.commit()
        return cursor.rowcount > 0


# new = {"first_name":"ploni","last_name":"almoni","phone_number":"unknown2"}  
# a = Contacts.create_contact(new)
# print(a)
# Contacts.update_contact(1,'jake','sun','75678')
# Contacts.delete_contact(2)
# rows = Contacts.get_all_contacts()
# print(Contacts.sql_to_dict(rows))














# cursor.close()
# conn.close()