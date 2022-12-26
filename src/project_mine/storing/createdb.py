import sqlite3

query = "CREATE TABLE PRODUCT \
        (ID INTEGER     PRIMARY KEY     AUTOINCREMENT, ) \
        NAME            CHAR(50)        NOT NULL, \
        CURRENCY        CHAR(20)        NOT NULL, \
        PRICE           REAL            NOT NULL) \
    "

def create_db(db_path: str) -> None:
    """create a sqlite db with a single table, called product 

    Args:
        db_path (str): database path
    """
    connection = sqlite3.connect(db_path)
    connection.execute(query)
    print("The connection with the db {db_path} has been established and table has been created")

if __name__ == "__main__":
    create_db("product.db")