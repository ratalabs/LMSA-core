import pandas as pd


filename = '/Users/smccaffrey/Desktop/git/PIRT_ASU/PHY132_Fall2017.csv'

def parser(filename):
    df1 = pd.read_csv(filename, dtype=object, delimiter='\t', header=None)
    i = 1
    print(df1[0][i])
    return df1

parser(filename)
