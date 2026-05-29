'''
soo we want reusable functions for the password hashing now.
this will help keepingh auth centralized. reusable . and clean structure.

also why ddnt we direcly write this in the routes , well routes are preffered
to be thin. soo yeah
'''

from passlib.context import CryptContext #this object manages hashing algos
from datetime import datetime , timedelta , timezone
from jose import jwt , JWTError
from app.core.config import ALGORITHM , SECRET_KEY
from fastapi.exceptions import HTTPException


#object that will store context for our hash func
pwd_context = CryptContext(
    schemes=['bcrypt'], #so we gonna use bcrypt
    deprecated = "auto" # if sometime we migrate from paslib bcrypt hash to some other algo
)

#hash function for reusability
def hash_password(password : str):
    return pwd_context.hash(password)


#for signup and login , lets implement password verification
def verify_password(password : str , hashed_password : str):
    return pwd_context.verify(
        password, #this would be the password we will recieve from user
        hashed_password # this parameter uses the hashed thing to extract stored hash , rehashes and compares safely
    )
#basically , does this hash belong to this password.


#alr lets handle the jwt now !
def create_access_token(user_id , expires_in_minutes = 30):
    payload = {
        'sub'  : str(user_id),
        'exp' : datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)
    }  

    access_token = jwt.encode(
        payload,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )
    return access_token

#now that the jwt token is generated we need to verify it in cases where we need to return the user
#thus this function will handle decoding , from token -> userid with proper auth checking

def verify_access_token(token):
    
    try : 
        payload = jwt.decode(
            token=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        ) #this checks everything --> token expiration , token validation , correct/invalid , signature
        #if somthing mismatches , gives jwtError , so we handled it below
        
        user_id = payload.get('sub' , None)
        
        if user_id is None:
            raise HTTPException(
                status_code=401 ,
                detail='invalid token'
            )
        
        return int(user_id)
    except JWTError: #so basically , jwt.decode gives an error , if the token is invalid , or expired or anything , that is jwterror , and we handled it as a httpexception
        raise HTTPException(
            status_code=401 ,
            detail='invalid token'
        )
