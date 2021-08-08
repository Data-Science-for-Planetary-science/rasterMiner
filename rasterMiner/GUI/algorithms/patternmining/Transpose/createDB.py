from createDenseDF import *
from dense2DB import *
import sys

class createDB:
    def __init__(self, iFile, oFolder, condition, thresholdValue):
        self.iFile = iFile
        self.oFile = oFolder+"/sampleTDB.csv"
        self.condition = condition
        self.thresholdValue = thresholdValue

    def run(self):
        dataFrame = createDenseDF(self.iFile)
        dataFrame.getDF()
        dataBase = dense2DB(dataFrame,self.condition,self.thresholdValue)
        dataBase.createTemporal(self.oFile)


if __name__ == "__main__":
    cDB = createDB(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    cDB.run()

