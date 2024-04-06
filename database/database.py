import psycopg2
from psycopg2.extras import RealDictCursor
import database.constants as c

class PostgreSQL:

    def __init__(self): 
        try:
            self.conn = psycopg2.connect(
                host=c.hostname,
                dbname=c.database,
                user=c.username,
                password=c.pwd,
                port=c.port_id
            )
            self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        except Exception as error: 
            print(error)
    
    def retrieve_data(self):
        # Retrieve data from the table
        self.cur.execute('SELECT * FROM public."WhitelistWebsite"')
        return self.cur.fetchall()
    
    def close_connection(self):
        if self.cur is not None: 
            self.cur.close()
        if self.conn is not None: 
            self.conn.close()
