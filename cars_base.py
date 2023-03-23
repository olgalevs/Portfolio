#Create DataBase&Tables
import mysql.connector
from mysql.connector import Error
import pandas as pd

#Connecting to MySQL Server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection
    
#Creating a New Database

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

#Connecting to the Database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#Creating a Query Execution Function
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

#Creating Tables
create_car_table = """
CREATE TABLE IF NOT EXISTS car (
  `type_id` INT PRIMARY KEY,
  `type_name` VARCHAR(40) NOT NULL
  );
"""

create_country_table = """
CREATE TABLE IF NOT EXISTS country (
  `country_id` INT PRIMARY KEY,
  `country_name` VARCHAR(40) NOT NULL
  );
 """

#Connecting to MySQL Server and creating new DB "cars"

pw='###########'
db='cars'

server_connection = create_server_connection("###########", "###########", pw)
connection = create_db_connection("###########", "###########", pw, db)
create_database_query="CREATE DATABASE IF NOT EXISTS cars"
create_database(server_connection,create_database_query)

df_country = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=7)
df_bev = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=0)

year_string=''
for i in range(1,len(df_bev.columns)):
        year_string=f"{year_string}`{df_bev.columns[i]}` INT NOT NULL,"

create_bev_table =f"CREATE TABLE IF NOT EXISTS bev (`type_id` INT NOT NULL,`country_id` INT NOT NULL,{year_string} PRIMARY KEY (type_id,country_id));" 
create_pheb_table =f"CREATE TABLE IF NOT EXISTS pheb (`type_id` INT NOT NULL,`country_id` INT NOT NULL,{year_string} PRIMARY KEY (type_id,country_id));" 
create_hev_table =f"CREATE TABLE IF NOT EXISTS hev (`type_id` INT NOT NULL,`country_id` INT NOT NULL,{year_string} PRIMARY KEY (type_id,country_id));" 
create_ngv_table =f"CREATE TABLE IF NOT EXISTS ngv (`type_id` INT NOT NULL,`country_id` INT NOT NULL,{year_string} PRIMARY KEY (type_id,country_id));" 
create_lpg_table =f"CREATE TABLE IF NOT EXISTS lpg (`type_id` INT NOT NULL,`country_id` INT NOT NULL,{year_string} PRIMARY KEY (type_id,country_id));" 
create_petrol_table =f"CREATE TABLE IF NOT EXISTS petrol (`type_id` INT NOT NULL,`country_id` INT NOT NULL,{year_string} PRIMARY KEY (type_id,country_id));" 
create_diesel_table =f"CREATE TABLE IF NOT EXISTS diesel (`type_id` INT NOT NULL,`country_id` INT NOT NULL,{year_string} PRIMARY KEY (type_id,country_id));" 

# Connect to the Database and create table
execute_query(connection, create_car_table) 
execute_query(connection, create_country_table) 
execute_query(connection, create_bev_table) 
execute_query(connection, create_pheb_table) 
execute_query(connection, create_hev_table) 
execute_query(connection, create_ngv_table) 
execute_query(connection, create_lpg_table) 
execute_query(connection, create_petrol_table) 
execute_query(connection, create_diesel_table)

#Connection between tables
alter_bev = """
ALTER TABLE bev
ADD FOREIGN KEY(country_id)
REFERENCES country(country_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_bev2 = """
ALTER TABLE bev
ADD FOREIGN KEY(type_id)
REFERENCES car(type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_pheb = """
ALTER TABLE pheb
ADD FOREIGN KEY(country_id)
REFERENCES country(country_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_pheb2 = """
ALTER TABLE pheb
ADD FOREIGN KEY(type_id)
REFERENCES car(type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_hev = """
ALTER TABLE hev
ADD FOREIGN KEY(country_id)
REFERENCES country(country_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_hev2 = """
ALTER TABLE hev
ADD FOREIGN KEY(type_id)
REFERENCES car(type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_ngv = """
ALTER TABLE ngv
ADD FOREIGN KEY(country_id)
REFERENCES country(country_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_ngv2 = """
ALTER TABLE ngv
ADD FOREIGN KEY(type_id)
REFERENCES car(type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_lpg = """
ALTER TABLE lpg
ADD FOREIGN KEY(country_id)
REFERENCES country(country_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_lpg2 = """
ALTER TABLE lpg
ADD FOREIGN KEY(type_id)
REFERENCES car(type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_petrol = """
ALTER TABLE petrol
ADD FOREIGN KEY(country_id)
REFERENCES country(country_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_petrol2 = """
ALTER TABLE petrol
ADD FOREIGN KEY(type_id)
REFERENCES car(type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_diesel = """
ALTER TABLE diesel
ADD FOREIGN KEY(country_id)
REFERENCES country(country_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""

alter_diesel2 = """
ALTER TABLE diesel
ADD FOREIGN KEY(type_id)
REFERENCES car(type_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
"""
execute_query(connection, alter_bev)
execute_query(connection, alter_bev2)
execute_query(connection, alter_pheb)
execute_query(connection, alter_pheb2)
execute_query(connection, alter_hev)
execute_query(connection, alter_hev2)
execute_query(connection, alter_ngv)
execute_query(connection, alter_ngv2)
execute_query(connection, alter_lpg)
execute_query(connection, alter_lpg2)
execute_query(connection, alter_petrol)
execute_query(connection, alter_petrol2)
execute_query(connection, alter_diesel)
execute_query(connection, alter_diesel2)


