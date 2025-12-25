# please read me! (.md)

## author:
Jacob shemesh\
325606481\
negev

copyright disclaimer: if you want to copy this code... be my guest, i dont know waht you found here tbh...




## what i maneged to do

i did Docker, sql database, api application
each one with his respective branch 

**-------- Docker branch --------**

2 working containers that can communicate with each other

**--------- sql branch --------**

init sql and data_intractor that has all the needed sql querys

**--------- api branch --------**

all endpoints work




## how to run the code ##

```bash
docker compose up --build 
```

then open: (optional)
http://localhost:8000/docs  



in postman:

url: (http://localhost:8000/contacts/)

**POST endpoint:**

write this format in body:
{\
    "first_name":"x",\
    "last_name": "y",\
     "phone_number":"010110101"\
}

returns:
  {\
     "message": "Contact created successfully",\
     "id": new_id\
        }

**PUT endpoint:**

you need to enter the id of the contact you want to change

example in postman:
                              ! the "1" is the id
http://localhost:8000/contacts1

and you need to enter the changes like that in body

{\
    "first_name":"jake",\
    "last_name": "sun",\
     "phone_number":"1050343"\
}


return: True of False

**DELETE endpoint:**

http://localhost:8000/contacts/?id=1 (the id of the contact you want to delete)

returns: True or False




