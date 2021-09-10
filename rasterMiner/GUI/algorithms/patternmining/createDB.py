from algorithms.patternmining import createDenseDF
from algorithms.patternmining import dense2DB
import sys

class createDB:
    def __init__(self, iFile, oFolder, condition, thresholdValue):
        self.iFile = iFile
        self.oFile = oFolder+"/sampleTDB.csv"
        self.condition = condition
        self.thresholdValue = thresholdValue

    def run(self):
        dataFrame = createDenseDF.createDenseDF(self.iFile)
        dataBase = dense2DB.dense2DB(dataFrame.getDF(),self.condition,self.thresholdValue)
        dataBase.createTransactional(self.oFile)


if __name__ == "__main__":
    cDB = createDB(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    cDB.run()

