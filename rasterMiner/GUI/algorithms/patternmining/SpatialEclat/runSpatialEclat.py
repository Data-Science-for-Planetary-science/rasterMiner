from SpatialEclat import SpatialEclat
from createDenseDF import createDenseDF
from dense2DB import dense2DB
from euclidDistance import *


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
        self.oFile = "/Users/masuyudai/rasterMiner2/algorithms/patternmining/Output/"+oFile
        self.minSup = float(minSup)
        self.condition = str(condition)
        self.value = int(value)
        self.threshold = int(threshold)


    def run(self):
        obj = createDenseDF(self.dFile)
        df = obj.getDF()
        obj2 = dense2DB(df, self.condition, self.value)
        obj3 = EuclidDistance(self.dFile,self.nFile,self.threshold)
        obj3.run()
        obj2.createTemporal("sampleTDB.csv")
        se = SpatialEclat(obj2.getFileName(),obj3.getFileName(),self.minSup)
        se.startMine()
        se.storePatternsInFile(self.oFile)
        print(len(se.getFrequentPatterns()))


if __name__=="__main__":
    dataFile = sys.argv[1]
    oFile = sys.argv[2]
    minSup = int(sys.argv[3])
    condition = sys.argv[4]
    value = int(sys.argv[5])
    threshold = int(sys.argv[6])
    obj = createDenseDF(dataFile)
    obj2 = dense2DB(obj.getDF, condition, value)
    obj2.createTemporal("sampleTDB.csv")
    obj3 = EuclidDistance(dataFile,"sample.txt",threshold)
    obj3.run()
    se = SpatialEclat(obj2.getFileName(),obj3.getFileName(),minSup)
    se.startMine()
    frequentPatterns = se.getFrequentPatterns()
    print("Total number of Spatial Frequent Patterns:", len(frequentPatterns))