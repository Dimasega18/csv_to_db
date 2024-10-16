import unittest
import glob
import pandas as pd

x = glob.glob('./*.csv')

class TestStringMethods(unittest.TestCase):
    
    def test_fileexist(self):
        for y in x :
            csv = y
        self.assertEqual(bool(x),True)
        self.assertEqual(csv.endswith('.csv'),True)
        
    def test_pandastype(self):
        df =  pd.read_csv(y for y in x)
        self.assertEqual(type(df),pd.DataFrame)
        df = df.iloc[[0],:][df.columns[0]]
        self.assertEqual(type(df),pd.Series)

    def test_column(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

if __name__ == '__main__':
    unittest.main()
