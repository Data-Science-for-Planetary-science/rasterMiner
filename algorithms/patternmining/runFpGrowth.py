from algorithms.patternmining.createDenseDF import createDenseDF
from algorithms.patternmining.dense2DB import dense2DB
from fpGrowth import *
import sys


class runFpGrowth():
    def __init__(self,dFile,oFile,minSup,condition,value):
        self.dFile = dFile
        self.oFile = oFile
        self.minSup = minSup
        self.condition = condition
        self.value = value

    def startMine(self):
        obj = createDenseDF(self.dFile)
        obj2 = dense2DB(obj.getDF(), self.condition, self.value)
        obj2.createTemporal("sampleTDB.csv")
        fp = Fpgrowth(r"sampleTDB.csv",self.minSup)
        fp.startMine()


if __name__=="__main__":
    dataFile = sys.argv[1]
    oFile = sys.argv[2]
    minSup = sys.argv[3]
    condition = sys.argv[4]
    value = int(sys.argv[5])
    obj = createDenseDF(dataFile)
    obj2 = dense2DB(obj.getDF(), condition, value)
    obj2.createTemporal("sampleTDB.csv")
    fp = Fpgrowth(r"sampleTDB.csv",minSup)
    fp.startMine()