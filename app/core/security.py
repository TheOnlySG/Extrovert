'''
soo we want reusable functions for the password hashing now.
this will help keepingh auth centralized. reusable . and clean structure.

also why ddnt we direcly write this in the routes , well routes are preffered
to be thin. soo yeah
'''

from passlib.context import CryptContext #this object manages hashing algos

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
        password,
        hashed_password
    )
#basically , does this hash belong to this password.

