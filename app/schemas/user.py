from pydantic import BaseModel , EmailStr


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