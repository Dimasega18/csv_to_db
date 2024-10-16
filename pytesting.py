import unittest
import glob
import pandas as pd
import argparse
from sqlalchemy import create_engine

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

    data = [username,password,port,dbname,dbms,host]

    if None in data :
        raise ValueError("Insert all requirement")
    
    return data

url_engine = f'{connections()[4]}://{connections()[0]}:{connections()[1]}@{connections()[5]}:{connections()[2]}/{connections()[3]}'

x = glob.glob('./*.csv')
for y in x :
    path = y

class TestStringMethods(unittest.TestCase):
    
    def test_fileexist(self):
        for y in x :
            csv = y
        self.assertEqual(bool(x),True)
        self.assertEqual(csv.endswith('.csv'),True)
        
    def test_pandastype(self):
        df =  pd.read_csv(path)
        self.assertEqual(type(df)==pd.DataFrame,True)
        df = df.iloc[[0],:][df.columns[0]]
        self.assertEqual(type(df)==pd.Series,True)

    def test_column(self):
        df =  pd.read_csv(path)
        self.assertEqual('Unnamed: 0' in list(df.columns),False)
        self.assertEqual(len(list(df.columns))>1,True)

    def test_null(self):
        df =  pd.read_csv(path)
        x = list(df.isna().sum().values)
        y = [True if j == 0 else False for j in x]
        self.assertEqual(all(y),True)

    def test_row(self):
        df =  pd.read_csv(path)
        self.assertEqual(len(df.values)>1,True)
    
    def test_connection(self):
        engine = create_engine(url_engine)
        self.assertEqual(bool(engine.connect()),True)

if __name__ == '__main__':
    unittest.main()
