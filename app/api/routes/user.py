from fastapi import APIRouter , Depends
from app.db.database import  get_db
from app.db.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
'''
whats this api router btw ? this is something that allows fastapi to modernize the backend structure.
traditionally we stuff all routes in main.py or app.py right ? the apirouter allows you to spread your routes
in different folders which will keep code clean and modern

how do we use it ? like we doo app = FastAPI() , or app = Flask(__name__) ,
inside the folder we anna place route , or the file
we simply do

router = apirouter() thingy

'''


router = APIRouter()

@router.post('/signup')
def user_sign_up(
    person : UserCreate, #putting pydantic schema into person so we validate before the value is even passed to api
    db : Session = Depends(get_db) # basically fastapi is creating a sessionlocal while the function starts , and would probably close the session after the function ends or returns value
    ):
    # now we already have a validated user (person , which is a pydantic class object btw) and a database session (created from get_db())
    # the Depends() thing fetches and creates the db local session

    new_user = User(
        username = person.username,
        email = person.email,
        password = person.password
    ) # now this is an object of our orm , means this has database like structure

    # now we have a user , and we can push it straight to database , and how we do that ? with orm !

    db.add(new_user) 
    '''
    well this already knows which table we wanna put this value in
    as above we created orm object with User , and it already has table name inside . so yeah

    also , now we havent yet pushed this to table , we just prepared , something like
    "prepare changes" , now we need to use Data Transaction Language , thus make transactions
    means commit ! , meaning finalize changes
    '''

    db.commit() #transaction idea is simple , either all changes happen , or non happen , its never
    #the half way,


    return 'sample layout'