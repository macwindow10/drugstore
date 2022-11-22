import sqlite3


def create_db():
    con = sqlite3.connect(database=r'drugstore.db')
    # To write any querries, we need to establish a cursor
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text, name text, email text, gender text, contact text, address text)")
    # cur.execute("INSERT INTO employee VALUES(1, 'William Admin', 'william@gmail.com', 'Male', '0300434678576', '12/12/1991', '01/01/2010', '1111', 'ADMIN', 'NY', 10000)")
    # cur.execute("INSERT INTO employee VALUES(2, 'David Manager', 'david@gmail.com', 'Male', '03003454355', '12/12/1985', '01/01/2012', '1111', 'MANAGER', 'CA', 8000)")
    # cur.execute("INSERT INTO employee VALUES(3, 'John Guard', 'john@gmail.com', 'Male', '03009887343', '12/12/1990', '01/01/2013', '1111', 'GUARD', 'DC', 7000)")
    print('users')
    con.commit()

    # we need to run it only once to create the table and then we close it.
    print('completed')


create_db()
