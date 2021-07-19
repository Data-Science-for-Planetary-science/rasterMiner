import pandas as pd

class createDenseDF:
    def __init__(self, inputFile):
        self.inputFile = inputFile

    def getDF(self):
        df = pd.read_table(self.inputFile, sep='\t', header=None)
        #tid = df[0].astype(str) + ',' + df[1].astype(str)
        #df = df.iloc[:,1:len(df.columns)]
        df = df.T
        df = df.rename(index=lambda s: 'band'+str(s))
        index = df.loc["band0"]
        #denseDF = pd.concat([tid, df], axis=1)
        df.rename(columns=index, inplace=True)
        df = df.drop('band0')
        return df

if __name__ == '__main__':
    obj = createDenseDF('spatialData_100.tsv')
    print(obj.getDF())