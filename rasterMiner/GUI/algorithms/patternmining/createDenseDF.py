import pandas as pd

class createDenseDF:
    def __init__(self, inputFile):
        self.inputFile = inputFile

    def getDF(self):
        df = pd.read_csv(self.inputFile, sep='\t', header=None)
        df[0] = df[0].str.replace('[^0-9. ]',"")
        df = df.T
        df = df.rename(index=lambda s: 'band'+str(s))
        index = df.loc["band0"]
        df.rename(columns=index, inplace=True)
        df = df.drop('band0')
        return df

if __name__ == '__main__':
    obj = createDenseDF('/Users/masuyudai/runDataTranspose/Data/spatialData_1000.tsv')
    obj.getDF()