import psycopg2
from config import config

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        drop table if exists DHT22_Temperature_Data
        """,
        """ create table DHT22_Temperature_Data (
              id serial primary key,
              SensorID text,
              Date_n_Time text,
              Temperature text
            )
        """,
        """
       drop table if exists DHT22_Humidity_Data 
        """,
        """
        create table DHT22_Humidity_Data (
              id serial primary key,
              SensorID text,
              Date_n_Time text,
              Humidity text
            )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
