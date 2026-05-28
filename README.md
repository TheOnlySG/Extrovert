this readme currently holds my journey for building a social media app. and i use it to maintain 
a track on my progress so you can totally ignore it for now ! :)


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


great now we have a dummy user storage model . wait , why did i call it dummy ? 
well we cant directly store passwords in database , right ? that will probably make
security vernareble if some of the data leaks , passwords are exposed.
solution - we use password hashing , and for that we use passlib[bycrypt]

let me break the wroking of it .
say our password is -- and our password hashed string is --
password123 => $2b$12$asdasdjasd...
and now we compare hashed strings. match ? return from server the required page !

bycrypt is a password hashing algorithm , not encription btw , both are different,

in bycryption , you cant reverse your password , means
once the password got hashed , you cant convert the hashing back to password.
example : 
password123 => $2b$12$asdasdjasd... , now this hashed thing cant be converted back to password

but , encryption is reversible.it is used for messeging , files etc.

also , deep down bycryption hashing is broken into fast hashing and slow hashing , 
fast hashing -> fast and quick hashed password. 
slow hashing -> slow but reliable and perfect hashed password.

hackers can try millions of password per sec to break a fast hashed password , but slow hashed cant be done

also , it uses salt , now wth is salt ? 
well if another user enters same password , then their hash wont be same.


alr enough explaination
so i have now updated the users.py from both db and api.routes . Thus , both validation model and
orm model are updated and yeah , "same synced" if we keep it simple.

NOW NOW NOW , earlier the postgres table stored password,  butnow , the table stores password_hash.
fair. but the table now alter exists and our sqlalchemy cant update an existing table. 
sooo here , a concept is introduced called migration , (well i pretty much understood the core
why, what , where for migration)
we would be using alembic for doing so btw. 
**BUT**
not now , for now i am simply dropping table from postgres manually.