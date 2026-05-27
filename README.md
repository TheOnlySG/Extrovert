# project updates

we have loaded our database url inside of app/core/config.py , using dotenv loader
os.load_env thingy

main connection of ORM is in folder
app/db/database.py


tables created :
users(id (PK) , username , base )


so  how does the flow work ? 
1. models imported
2. create_all() will get metadata
3. sqlalchemy writes queries
4. postgres creates table.



