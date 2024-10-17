import unittest
import glob
import pandas as pd
import argparse
from sqlalchemy import create_engine

def connections(args):
    username = args.user
    password = args.password
    port = args.port
    dbname = args.name
    dbms = args.dbms
    host = str(args.host)
    data = [username,password,port,dbname,dbms,host]

    return data
    
def url_engine(args):
    data_conn = connections(args)
    url_engine = f'{data_conn[4]}://{data_conn[0]}:{data_conn[1]}@{data_conn[5]}:{data_conn[2]}/{data_conn[3]}'
    return url_engine

def csv_file():
    x = glob.glob('./*.csv')
    return x

class TestStringMethods(unittest.TestCase):
    
    def test_connection(self):
        
        engine = create_engine(url_engine(args))
        self.assertEqual(bool(engine.connect()),True)

    def test_fileexist(self):
        self.assertEqual(bool(csv_file()),True)
        self.assertEqual(len(csv_file())==1,True)
        for x in csv_file():
            path = x
        self.assertEqual(path.endswith('.csv'),True)

    def test_pandastype(self):
        df =  pd.read_csv(csv_file())
        self.assertEqual(type(df)==pd.DataFrame,True)
        df = df.iloc[[0],:][df.columns[0]]
        self.assertEqual(type(df)==pd.Series,True)

    def test_column(self):
        for x in csv_file():
            path = x
        df =  pd.read_csv(path)
        self.assertEqual('Unnamed: 0' in list(df.columns),False)
        self.assertEqual(len(list(df.columns))>1,True)

    def test_null(self):
        for x in csv_file():
            path = x
        df =  pd.read_csv(path)
        x = list(df.isna().sum().values)
        y = [True if j == 0 else False for j in x]
        self.assertEqual(all(y),True)

    def test_row(self):
        for x in csv_file():
            path = x
        df =  pd.read_csv(path)
        self.assertEqual(len(df.values)>1,True)
    
    def test_input(self):
        self.assertEqual(connections(args)[2].isnumeric(),True)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='connect your db')

    parser.add_argument('-db','--dbms',help='name your dbms',choices=('postgresql','mysql'))
    parser.add_argument('-u','--user',help='your db username')
    parser.add_argument('-hs','--host',help='your hostname',default='localhost')
    parser.add_argument('-pw','--password',help='your db password')
    parser.add_argument('-p','--port',help='your db port',type=int)
    parser.add_argument('-n','--name',help='your db name')

    args = parser.parse_args()

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
