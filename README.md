This is a task for global alania interview  
Env is specially opened here)  
  
To deploy the project you need run next commands  
  
(Optional) create a venv  

```python -m venv venv```

To open venv enter the command in the terminal  

```source venv/Scripts/Activate```

Once you have entered the venv you need to install all the dependencies

```pip install -r requirements.txt```

After that, configure the connection to your database in the database.py and alembic.ini files  

To start migrations you need to run the commands:  

- ```alembic revision --autogenerate -m "initial"```
- ```alembic upgrade head```

To start the app run command

```uvicorn main:app --reload```

That's all