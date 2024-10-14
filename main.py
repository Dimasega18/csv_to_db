import pandas as pd
from sqlalchemy import create_engine
import argparse
from time import perf_counter
import time
import glob

parser = argparse.ArgumentParser(prog='connect your db')

parser.add_argument('-db','--dbms',help='name your dbms',choices=('postgresql','mysql'))
parser.add_argument('-u','--user',help='your db username')
parser.add_argument('-hs','--host',help='your hostname',default='localhost')
parser.add_argument('-ps','--password',help='your db password')
parser.add_argument('-p','--port',help='your db port',type=int)
parser.add_argument('-n','--name',help='your db name')
parser.add_argument('-tb','--tbname',help='your table name')

args = parser.parse_args()

def connections():
    username = args.user
    password = args.password
    port = args.port
    dbname = args.name
    dbms = args.dbms
    host = str(args.host)
    tbname = args.tbname
    csv_path = glob.glob('./*.csv')

    if len(csv_path) == 0:
        raise ValueError("Csv file not found")

    for x in csv_path:
        path = x

    data = [username,password,port,dbname,dbms,host,path,tbname]

    if None in data :
        raise ValueError("Insert all requirement")
    
    return data

url_engine = f'{connections()[4]}://{connections()[0]}:{connections()[1]}@{connections()[5]}:{connections()[2]}/{connections()[3]}'

engine = create_engine(url_engine)
connection = engine.connect()

try :
    if (bool(connection) == True) and (connections()[6].endswith('.csv') == True) :
        print("Connection Accepted")
        
        df = pd.read_csv(connections()[6],chunksize=10,iterator=True,low_memory=True,encoding='latin-1')
    
        row = 10
        while True :
            try :
                time_start =  perf_counter()

                df_new = next(df).iloc[:,1:]
                import_db = df_new.to_sql (connections()[7],con=engine,index=True,if_exists='append')

                time_end = perf_counter()
                
                print(f"{row} Row Inserted In {time_end-time_start} Second")
                
                time.sleep(10)

                if row == 50 :
                    print("All data has been inserted.")
                    break
                
                row += 10
            
            except Exception as e :
                print(f"insert data error : {e}")
                connection.close()
                break
    else:
        raise ValueError()
    
except Exception as e :

    print(f"Error connection {e}")