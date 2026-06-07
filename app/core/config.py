from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ENVIRONMENT = os.getenv('ENVIRONMENT' , 'development')

# print(DATABASE_URL)

# print(SECRET_KEY)
