from createDenseDF import createDenseDF
from dense2DB import dense2DB
from fpgrowth import FpGrowth
import sys



class runFpGrowth:
    """
    Attributes:
    -----------
        dFile : str
            data file
        oFile : str
            output file
        minSup : int
            minimum support
        condition :　str
            It is condition to judge the value in dataframe
        value : int
            Create database based on this value

    Methods:
    --------

    """

    def __init__(self,dFile,oFile,minSup,condition,value):
        self.dFile = dFile
        self.oFile = oFile
        self.minSup = minSup
        self.condition = condition
        self.value = value
        self.fp = None

    def run(self):
        obj = createDenseDF(self.dFile)
        obj2 = dense2DB(obj.getDF(), self.condition, self.value)
        obj2.createTemporal("sampleTDB.csv")
        self.fp = FpGrowth(r"sampleTDB.csv",self.minSup)
        self.fp.startMine()


if __name__=="__main__":
    """dataFile = sys.argv[1]
    oFile = sys.argv[2]
    minSup = int(sys.argv[3])
    condition = sys.argv[4]
    value = int(sys.argv[5])
    obj = createDenseDF(dataFile)
    obj2 = dense2DB(obj.getDF(), condition, value)
    obj2.createTemporal("sampleTDB.csv")"""
    fp = FpGrowth("/Users/masuyudai/runDataTranspose/Data/transactional_T10I4D100K.csv",1000)
    fp.startMine()
    print(len(fp.getFrequentPatterns()))

