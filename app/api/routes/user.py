from fastapi import APIRouter , Depends
from app.db.database import  get_db
from app.db.models.user import User
from app.schemas.user import UserCreate , UserResponse , UserLogin , Token , UserUpdate , UserProfile
from sqlalchemy.orm import Session

from fastapi.exceptions import HTTPException
from app.core.security import create_access_token

from app.api.dependencies.auth import get_current_user

from app.core.security import verify_password
from app.core.security import hash_password

from app.api.dependencies.user import get_user_by_id

# from app.core.security import verify_access_token
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

@router.post('/signup' ,response_model=UserResponse)  #notice we added response model as userresponse here
def user_sign_up(
    person : UserCreate, #putting pydantic schema into person so we validate before the value is even passed to api
    db : Session = Depends(get_db) # basically fastapi is creating a sessionlocal while the function starts , and would probably close the session after the function ends or returns value
    ):
    # now we already have a validated user (person , which is a pydantic class object btw) and a database session (created from get_db())
    # the Depends() thing fetches and creates the db local session

    email_exists = db.query(User).filter(
        User.email == person.email
    ).first()
    user_exists = db.query(User).filter(
        User.username == person.username
    ).first()

    if email_exists:
        raise HTTPException(
            status_code=400,
            detail='You already have an account with this email. please login'
        )
    if user_exists:
        raise HTTPException(
            status_code=400,
            detail='Username already taken'
        )



    new_user = User(
        username = person.username,
        email = person.email,
        password_hash = hash_password(person.password)
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


    #we gotto return the user right , so the object may not contain it as it is passed to orm model
    #thus we gotto refresh the db
    db.refresh(new_user)


    return new_user  #now to return this , fastapi will convert orm to json and send the new_user data


#lets handle login now , as signup is done.
@router.post('/login' , response_model=Token)
def user_login(person : UserLogin , db :Session = Depends(get_db)):
    login_user = db.query(User).filter( #passed the orm model User btw from db/user.py , smth like select * from user
        User.email == person.email #smth like select * from users where email = person.email
    ).first()
    '''
    we could have left the query here , but that will return an empty thing like [] if user dsnt exist
    . if we use .first() it will return email if it exists , and None if it dsnt
    '''
    if login_user and verify_password(person.password , login_user.password_hash):
        access_token = create_access_token(login_user.id) #now we got the token !
        
        token = {
            'access_token' : access_token,
            'token_type' : 'bearer'
        }

        return token
    else:
        raise HTTPException(status_code=401 , detail='invalid credentials')
        


@router.get('/me' , response_model=UserResponse)
def me(
    current_user : User = Depends(get_current_user)
):
    return current_user

@router.get('/users/{user_id}' , response_model=UserProfile)
def profile(
    user_id : int,
    db : Session = Depends(get_db)
):
    received_user = get_user_by_id(user_id , db)
    return received_user


@router.patch('/me' , response_model=UserProfile)
def update_user(
    update_data : UserUpdate,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):

    if update_data.bio is not None:
        current_user.bio = update_data.bio

    if update_data.profile_picture_url is not None:
        current_user.profile_picture_url = update_data.profile_picture_url

    if update_data.github_url is not None:
        current_user.github_url = update_data.github_url

    if update_data.linkedin_url is not None:
        current_user.linkedin_url = update_data.linkedin_url


    db.commit()
    db.refresh(current_user)

    return current_user


@router.get('/users', response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(User).all()


@router.get('/users/me/followers', response_model=list[UserResponse])
def get_my_followers(
    current_user: User = Depends(get_current_user)
):
    return [follow.follower for follow in current_user.followers]

    
