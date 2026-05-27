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



i also added get_db to database.py , explained the purpose of it there.

alr so fornow we are done with a model , but we need to validate it . what does that mean ? 
well lets break it down.
what did we create now , the model ? its user right ? something like class ...(Base): , its a
sqlalchemy inherited class right ? this would be the database representation , or in simple words
the table.
before inserting values , dont we need to validate it ? same datatype , same format and stuff ? 
this is where pydantic comes in , inbuilt in fastapi btw.
soo it has its own Base thingy , which can be inherited the same way as we did for our orm model.

what exactly will it do. it will define 
1. What api Expects 
2. Validation rules
3. response shaper.

    BASICALLY API LAYER



soo lets simply give a 1 worder for it:

pydantic will validate the input , is it correct ? does it fit our orm model ? if yes
then we push it over to our database from sqlalchemy model . simple.
check schemas folder for **validation** model

sqlalchemy -> database structure
pydantic -> api input output structure