import unittest
import glob
import pandas as pd
from sqlalchemy import create_engine
import sys

def connections():
    data = sys.argv[1:]
    return data
    
def url_engine():
    data_conn = connections()
    url_engine = f'{data_conn[4]}://{data_conn[0]}:{data_conn[1]}@{data_conn[5]}:{data_conn[2]}/{data_conn[3]}'
    return url_engine

def csv_file():
    return glob.glob('./*.csv')
    

class TestStringMethods(unittest.TestCase):
    
    def test_connection(self):
        engine = create_engine(url_engine())
        self.assertEqual(bool(engine.connect()),True,msg="Engine not connected")

    def test_fileexist(self):
        self.assertEqual(bool(csv_file()),True,msg="The CSV file is missing")
        self.assertEqual(len(csv_file())==1,True,msg="CSV files cannot be more than one")
        self.assertEqual(csv_file()[0].endswith('.csv'),True,msg="The CSV file does not have a .csv extension")

    def test_pandastype(self):
        df =  pd.read_csv(csv_file()[0])
        self.assertEqual(type(df)==pd.DataFrame,True,msg="The object is not a DataFrame")
        df = df.iloc[[0],:][df.columns[0]]
        self.assertEqual(type(df)==pd.Series,True,msg="The object is not a DataFrame")

    def test_column(self):
        df =  pd.read_csv(csv_file()[0])
        self.assertEqual('Unnamed: 0' in list(df.columns),False,msg="There is an unnamed column")
        self.assertEqual(len(list(df.columns))>1,True,msg="Columns must be more than one")

    def test_null(self):
        df =  pd.read_csv(csv_file()[0])
        null_val = list(df.isna().sum().values)
        null_check = [True if j == 0 else False for j in null_val]
        self.assertEqual(all(null_check),True,msg="There are null values")

    def test_row(self):
        df =  pd.read_csv(csv_file()[0])
        self.assertEqual(len(df.values)>1,True,msg="Rows must be more than one")
    
    def test_input(self):
        self.assertEqual(connections()[2].isnumeric(),True,msg="Port must be numeric")


if __name__ == '__main__':
    unittest.main(argv=sys.argv[:1])
