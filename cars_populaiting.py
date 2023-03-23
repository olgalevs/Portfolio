#Populating tables
import mysql.connector
from mysql.connector import Error
import pandas as pd

#Connecting to the Database DEF#
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

#Reading Data
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

pw='###########'
db='cars'

#Populating the Tables#

connection = create_db_connection("###########", "###########", pw, db)

df_car = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=0)

#car table#
pop_car="""
INSERT INTO car VALUES
(1,'bev'),
(2,'pheb'),
(3,'hev'),
(4,'ngv'),
(5,'lpg'),
(6,'petrol'),
(7,'diesel');
"""
execute_query(connection, pop_car)

#country table#
df_country = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=7)
for index, df in df_country.iterrows():
    pop_country=f"INSERT INTO country VALUES ({df['Country_id']},'{df['Country_name']}')"
    #print(pop_bev)
    execute_query(connection, pop_country)

#BEV#
#clean if exists
df_bev = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=0)
clean_bev = "DELETE FROM cars.bev WHERE type_id IS NOT NULL;"
execute_query(connection, clean_bev)

#type id
id_bev="select * from car where type_name='bev'"
id_bev_res=(read_query(connection,id_bev))
type_id=id_bev_res[0][0]

for index, df in df_bev.iterrows():
    #country id
    country_value=[]
    country_id=str(df_country['Country_id'][df_country['Country_name']==df['Country']].values[0])
    #by years
    for i in range(1,len(df_bev.columns)):
        country_value.append(str(df[int(list(df_bev)[i])]))
    sent=",".join(country_value)
    pop_bev=(f"INSERT INTO bev VALUES ({type_id},{int(country_id)},{sent});")
    execute_query(connection, pop_bev)

#PHEB#
#clean if exists
df_pheb = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=1)
clean_pheb = "DELETE FROM cars.pheb WHERE type_id IS NOT NULL;"
execute_query(connection, clean_pheb)

#type id
id_pheb="select * from car where type_name='pheb'"
id_pheb_res=(read_query(connection,id_pheb))
type_id=id_pheb_res[0][0]

for index, df in df_pheb.iterrows():
    #country id
    qnt_value=[]
    country_id=str(df_country['Country_id'][df_country['Country_name']==df['Country']].values[0])
    for i in range(1,len(df_pheb.columns)):
        qnt_value.append(str(df[int(list(df_pheb)[i])]))
    sent=",".join(qnt_value)
    pop_pheb=(f"INSERT INTO pheb VALUES ({type_id},{int(country_id)},{sent});")
    execute_query(connection, pop_pheb)

#HEV#
#clean if exists
df_hev = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=2)
clean_hev = "DELETE FROM cars.hev WHERE type_id IS NOT NULL;"
execute_query(connection, clean_hev)

#type id
id_hev="select * from car where type_name='hev'"
id_hev_res=(read_query(connection,id_hev))
type_id=id_hev_res[0][0]

for index, df in df_hev.iterrows():
    #country id
    qnt_value=[]
    country_id=str(df_country['Country_id'][df_country['Country_name']==df['Country']].values[0])
    for i in range(1,len(df_hev.columns)):
        qnt_value.append(str(df[int(list(df_hev)[i])]))
    sent=",".join(qnt_value)
    pop_hev=(f"INSERT INTO hev VALUES ({type_id},{int(country_id)},{sent});")
    execute_query(connection, pop_hev)

#NGV#
#clean if exists
df_ngv = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=3)
clean_ngv = "DELETE FROM cars.ngv WHERE type_id IS NOT NULL;"
execute_query(connection, clean_ngv)

#type id
id_ngv="select * from car where type_name='ngv'"
id_ngv_res=(read_query(connection,id_ngv))
type_id=id_ngv_res[0][0]

for index, df in df_ngv.iterrows():
    #country id
    qnt_value=[]
    country_id=str(df_country['Country_id'][df_country['Country_name']==df['Country']].values[0])
    for i in range(1,len(df_ngv.columns)):
        qnt_value.append(str(df[int(list(df_ngv)[i])]))
    sent=",".join(qnt_value)
    pop_ngv=(f"INSERT INTO ngv VALUES ({type_id},{int(country_id)},{sent});")
    execute_query(connection, pop_ngv)

#LPG#
#clean if exists
df_lpg = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=4)
clean_lpg = "DELETE FROM cars.lpg WHERE type_id IS NOT NULL;"
execute_query(connection, clean_lpg)

#type id
id_lpg="select * from car where type_name='lpg'"
id_lpg_res=(read_query(connection,id_lpg))
type_id=id_lpg_res[0][0]

for index, df in df_lpg.iterrows():
    #country id
    qnt_value=[]
    country_id=str(df_country['Country_id'][df_country['Country_name']==df['Country']].values[0])
    for i in range(1,len(df_lpg.columns)):
        qnt_value.append(str(df[int(list(df_lpg)[i])]))
    sent=",".join(qnt_value)
    pop_lpg=(f"INSERT INTO lpg VALUES ({type_id},{int(country_id)},{sent});")
    execute_query(connection, pop_lpg)

#PETROL#
#clean if exists
df_petrol = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=5)
clean_petrol = "DELETE FROM cars.petrol WHERE type_id IS NOT NULL;"
execute_query(connection, clean_petrol)

#type id
id_petrol="select * from car where type_name='petrol'"
id_petrol_res=(read_query(connection,id_petrol))
type_id=id_petrol_res[0][0]

for index, df in df_petrol.iterrows():
    #country id
    qnt_value=[]
    country_id=str(df_country['Country_id'][df_country['Country_name']==df['Country']].values[0])
    for i in range(1,len(df_petrol.columns)):
        qnt_value.append(str(df[int(list(df_petrol)[i])]))
    sent=",".join(qnt_value)
    pop_petrol=(f"INSERT INTO petrol VALUES ({type_id},{int(country_id)},{sent});")
    execute_query(connection, pop_petrol)

#DIESEL#
#clean if exists
df_diesel = pd.read_excel(r'~/Documents/Data set EV/Main data.xlsx',sheet_name=6)
clean_diesel = "DELETE FROM cars.diesel WHERE type_id IS NOT NULL;"
execute_query(connection, clean_diesel)

#type id
id_petrol="select * from car where type_name='diesel'"
id_diesel_res=(read_query(connection,id_petrol))
type_id=id_diesel_res[0][0]

for index, df in df_diesel.iterrows():
    #country id
    qnt_value=[]
    country_id=str(df_country['Country_id'][df_country['Country_name']==df['Country']].values[0])
    for i in range(1,len(df_diesel.columns)):
        qnt_value.append(str(df[int(list(df_diesel)[i])]))
    sent=",".join(qnt_value)
    pop_diesel=(f"INSERT INTO diesel VALUES ({type_id},{int(country_id)},{sent});")
    execute_query(connection, pop_diesel)







