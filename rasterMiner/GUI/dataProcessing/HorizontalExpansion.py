import glob
import pandas as pd
from dataProcessing import raster2tsv
import os
from tkinter import messagebox



class HorizontalExpansion:
    def __init__(self, inputFolder,fileExtension,outputFolder,startBand, endBand):
        self.path = inputFolder + '/*.'+fileExtension
        self.outputFolder = outputFolder
        self.startBand = startBand
        self.endBand = endBand

    def convert(self):
        # reading each file in a folder
        my_df = pd.DataFrame()
        file = glob.glob(self.path)
        listOfDataframes = []
        mainDataFrame = pd.DataFrame
        out_csv = (self.outputFolder + '/rawData.tsv')
        text = ''
        header = ['0']
        for bandNo in range(self.startBand, self.endBand + 1):
            text = text + '-band ' + str(bandNo) + ' '
            header.append('-band' + str(bandNo))

        if os.path.exists(out_csv):
            os.remove(out_csv)

        for file in glob.glob(self.path):
            #extracting output filename
            parameters = text + file + ' ' + out_csv
            raster2tsv.raster2tsv(parameters)
            mainDataFrame = pd.read_csv(out_csv, header=None, sep='\t')
            mainDataFrame.columns = header
        #mainDataFrame = mainDataFrame.set_index('coordinate')
        print(mainDataFrame)
        mainDataFrame.to_csv(self.outputFolder + '/rawData.tsv', index=False, sep='\t')
        messagebox.showinfo('notification', 'Successfully completed')


if __name__ == '__main__':
    a = HorizontalExpansion('/Users/yukimaru/Downloads/rasterMinerSampleData/horizontalExpansion_1','lbl', '/Users/yukimaru/Desktops',3,9)
    a.convert()
