import glob
import pandas as pd
from dataProcessing import raster2tsv
import re


class HorizontalExpansion:
    def __init__(self, inputFolder,fileExtension,outputFolder,startBand, endBand):
        self.path = inputFolder + '/*.'+fileExtension
        self.outputFolder = outputFolder
        self.startBand =startBand
        self.endBand = endBand

    def convert(self):
        # reading each file in a folder
        my_df = pd.DataFrame()
        file = glob.glob(self.path)
        listOfDataframes = []

        out_csv = (self.outputFolder + '/spatialData.tsv')
        text = ''
        for bandNo in range(self.startBand, self.endBand + 1):
            text = text + '-band ' + str(bandNo) + ' '

        for file in glob.glob(self.path):
            #extracting output filename
            parameters = text + file + ' ' + out_csv
            raster2tsv.raster2tsv(parameters)



if __name__ == '__main__':
    a = HorizontalExpansion('/Users/udaykiranrage/Dropbox/raashika/rasterMinerSampleData/horizontalExpansion_1','lbl', '/Users/udaykiranrage/Dropbox/raashika/rasterMinerSampleData', 1,9)
    a.convert()
