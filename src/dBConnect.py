from langchain_community.utilities import SQLDatabase

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)



try:
    init_database(user="thunderstorm",
                  password="admin",
                  host="localhost",
                  port="3306",
                  database="Chinook")
    print("Success")
except Exception as e:
    print(e)