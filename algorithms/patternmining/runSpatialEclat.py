from algorithms.patternmining.createDenseDF import createDenseDF
from algorithms.patternmining.dense2DB import dense2DB
from SpatialEclat import *
import sys


class runSpatialEclat():
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
        se = SpatialEclat(r"sampleTDB.csv",self.minSup)
        se.startMine()


if __name__=="__main__":
    dataFile = sys.argv[1]
    oFile = sys.argv[2]
    minSup = int(sys.argv[3])
    condition = sys.argv[4]
    value = int(sys.argv[5])
    obj = createDenseDF(dataFile)
    obj2 = dense2DB(obj.getDF(), condition, value)
    obj2.createTemporal("sampleTDB.csv")
    se = SpatialEclat(r"sampleTDB.csv",minSup)
    se.startMine()