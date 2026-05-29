from pydantic import BaseModel , EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str


'''
we are not putting id , and created_at in here
as we dod for user.py . why ? 
as they wont be entered by user , id is auto
increment and datetime is auto set current utc time


username , email , password are the fields
which the user will enter while registering 
and are important for his profile
'''


#class for response
class UserResponse(BaseModel):

    model_config = {
        'from_attributes' : True
    } #well pydantic needs permission to read orm , so this thing handles it

    '''
    so basically we would be returning the orm object (new_user) from the api right ? 
    but we need to take permission of orm from that . as orm (sqlalchemy) wont direclty
    allow returning a model obejct . soo this statement handles that.
    '''


    #these are the things which would be returned throught the api

    id  : int
    username : str
    email : str
    created_at : datetime

    '''
    we will probably add the response model in route.post('/signup' , *HERE*) as an argument so
    api knows what object we returning and molds accordingly
    '''


#lets handle userlogin now

class UserLogin(BaseModel):
    email : EmailStr
    password : str


#jwt token object

class Token(BaseModel):
    access_token : str
    token_type : str
