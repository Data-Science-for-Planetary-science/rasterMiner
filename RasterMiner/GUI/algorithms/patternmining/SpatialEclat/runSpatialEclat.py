from SpatialEclat import SpatialEclat
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
    def __init__(self,iFile,oFolder,nFile,minSup):
        self.iFile = iFile
        self.nFile = nFile
        self.oFile = oFolder+"/result_spatialEclat.csv"
        self.minSup = float(minSup)




if __name__=="__main__":
    iFile = sys.argv[1]
    nFile = sys.argv[2]
    oFile = sys.argv[3]
    minSup = int(sys.argv[4])
    se = SpatialEclat(iFile,nFile,minSup)
    se.startMine()
    se.storePatternsInFile(oFile)