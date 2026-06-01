1. come to the root folder which is 'repository name'
2. make sure you have python on pc [python --version]
3. creating a virtual environment for python [python -m venv venv]
4. activate the virtual environment  


5. NOTE - you need postgres installed locally inorder to run this on localhost .once installed , follow these steps
6. open postgres in new terminal [psql -U postgres]
7. create a database called 'socialmedia' [CREATE DATABASE socialmedia]
8. db setup done , back to python terminal


9. install requirements [pip install -r requirements.txt]
10. run the uvicorn server locally [uvicorn app.main:app --reload]
11. open port [localhost 8000 mostly]
12. open swagger [LOCALHOSTURLXYZ/docs]


