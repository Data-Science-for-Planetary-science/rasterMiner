import glob
import pandas as pd
#from rasterMiner.GUI.dataProcessing import raster2tsv
from dataProcessing import raster2tsv
import re
import os
from tkinter import messagebox



class verticalExpansion:
    def __init__(self, path,fileExtension,outputFolder):
        self.path = path+ '/*.'+fileExtension
        self.outputFolder=outputFolder

    def convert(self):
        # reading each file in a folder
        my_df = pd.DataFrame()
        file = glob.glob(self.path)
        listOfDataframes = []
        columnName = []
        filecounter = 0
        mainDataFrame = pd.DataFrame()

        for file in glob.glob(self.path):
            #extracting output filename
            # if filecounter == 0:
            temp = re.findall(r'\d+', file)
            res = list(map(int, temp))
            out_csv = (self.outputFolder + '/' + str(res[0]) + '.csv')

            # convert to csv file
            columnName.append(res[0])
            parameters = '-band 1 ' + file + ' ' + out_csv
            raster2tsv.raster2tsv(parameters)
            # expanding csv files
            df = pd.read_csv(out_csv,index_col=None,header=None)
            df = df[0].str.split('\t',expand=True)
            df = df.rename(index=df[0])
            listOfDataframes.append(df[1])
            mainDataFrame = pd.concat(listOfDataframes,axis=1,ignore_index=True)
            mainDataFrame.columns = sorted(columnName)
            os.remove(out_csv)
        mainDataFrame.insert(0,'coordinate',mainDataFrame.index)
        mainDataFrame.to_csv(self.outputFolder+'/rawData.tsv',sep='\t',index=False)
        messagebox.showinfo('notification', 'Successfully completed')
        #     else:
        #         temp = re.findall(r'\d+', file)
        #         res = list(map(int, temp))
        #         out_csv = (self.outputFolder + '/' + str(res[0]) + '.tsv')
        #
        #         # convert to csv file
        #         columnName.append(res[0])
        #         paramters = '-band 1 ' + file + ' ' + out_csv
        #         raster2tsv.raster2tsv(paramters)
        #         # expanding csv files
        #         df = pd.read_csv(out_csv, index_col=None, header=None)
        #         listOfDataframes.append(df)
        #         mainDataFrame = pd.concat(listOfDataframes, axis=1, ignore_index=True)
        #         mainDataFrame.columns = columnName
        #         os.remove(out_csv)
        #         print(mainDataFrame)
        #
        # df = mainDataFrame.to_csv("test.csv")


if __name__ == '__main__':
    a = verticalExpansion('/Users/yukimaru/Downloads/rasterMinerSampleData/virtialExpansion', 'nc', '/Users/yukimaru/Downloads/rasterMinerSampleData')
    a.convert()

