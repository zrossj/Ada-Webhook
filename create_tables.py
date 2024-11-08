from sqlalchemy import create_engine, text


# read the credentials to acess the data base
with open ('postgre_aut.txt', 'r') as f:
    file_content = f.read()[:-1]


uri = file_content # uri holds the connection string for the database.
engine = create_engine(uri)


# queries to create the tables - drop table in use at the beggining; 

## creating a table to store subscribers email addresses 

with engine.connect() as conn:
    
    try: 
        conn.execute(
            text(
                """drop table if exists customer_mail; 
                create table 
            customer_mail  (
            name varchar(64), 
            mail_address varchar(64)
            );"""
            )
        )
    
    except Exception as e:
        print(f"error: {str(e)}")

    conn.commit()




## creating table to store fx collected data;
with engine.connect() as conn:


    try:
        conn.execute(
            text(
                """drop table if exists fx_price_collected;
                create table fx_price_collected (
            coin char(6),
            date timestamp,
            code char(3),
            codein char(3),
            name varchar(64),
            high decimal,
            low decimal,
            "varBid" decimal,
            "pctChange" decimal,
            bid decimal, 
            ask decimal);""")
        )


    except Exception as e:
        print(f"error: {str(e)}")

    conn.commit()


print('create tables finish')

