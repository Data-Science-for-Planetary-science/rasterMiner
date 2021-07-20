from algorithms.patternmining.createDenseDF import createDenseDF
from algorithms.patternmining.dense2DB import dense2DB
from euclidDistance import *
from SpatialEclat import *
import sys


class runSpatialEclat:
    """
        Attributes
        ----------
            dFile : str
                data file name
            nFile : str
                neighbourhood file name which is made from data file
            oFile : str
                output file name
            minSup : int
                this value is used in SpatialEclat data mining
            condition : str
                It is condition to judge the value in dataframe
            value : int
                Create database based on this value
            threshold : int
                when make neighbourhood file, we use this value
            se : SpatialEclat
                object of SpatialEclat class


    """
    def __init__(self,dFile,oFile,nFile,minSup,condition,value,threshold):
        self.dFile = dFile
        self.nFile = nFile
        self.oFile = oFile
        self.minSup = minSup
        self.condition = condition
        self.value = value
        self.threshold = threshold
        self.se = None

    def run(self):
        obj = createDenseDF(self.dFile)
        obj2 = dense2DB(obj.getDF(), self.condition, self.value)
        obj3 = EuclidDistance(self.dFile,self.nFile,self.threshold)
        obj3.run()
        obj2.createTemporal("sampleTDB.csv")
        self.se = SpatialEclat(obj2.getFileName(),obj3.getFileName(),self.minSup)
        self.se.startMine()
        self.se.storePatternsInFile(self.oFile)


if __name__=="__main__":
    dataFile = sys.argv[1]
    nFile = sys.argv[2]
    oFile = sys.argv[3]
    minSup = int(sys.argv[4])
    condition = sys.argv[5]
    value = int(sys.argv[6])
    threshold = int(sys.argv[7])
    obj = createDenseDF(dataFile)
    obj2 = dense2DB(obj.getDF(), condition, value)
    obj2.createTemporal("sampleTDB.csv")
    obj3 = EuclidDistance(dataFile,nFile,threshold)
    obj3.run()
    se = SpatialEclat(obj2.getFileName(),obj3.getFileName(),minSup)
    se.startMine()