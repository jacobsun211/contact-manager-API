from fastapi import FastAPI
import uvicorn
from data_interactor import Contacts

app = FastAPI()



@app.get("/")
def get_contacts():
    contacts = Contacts.get_all_contacts()
    contacts = Contacts.sql_to_dict(contacts)
    return contacts

# @app.post("create/")
# def post_contact():



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
