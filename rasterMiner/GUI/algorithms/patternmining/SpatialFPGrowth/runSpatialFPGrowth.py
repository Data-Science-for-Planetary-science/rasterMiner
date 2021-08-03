import spatialFPGrowth as sfp
import createDenseDF
import dense2DB
import euclidDistance

class runSpatialFpGrowth():
    def __init__(self, iFile, nFile, oFile, minSup, maxDist ,condition):
        self.iFile = iFile
        self.nFile = nFile
        self.oFile = oFile
        self.minSup = minSup
        self.maxDist = maxDist
        self.condition = condition

    def run(self):
        dataFrame = createDenseDF.createDenseDF(iFile)
        obj2 = dense2DB.dense2DB(obj.getDF(), condition, value)
        obj2.createTransactional("sampleTDB.csv")
        obj3 = euclidDistance.EuclidDistance(dFile, nFile, maxDist)
        obj3.run()
        spatialFpGrowth = sfp.spatialFpGrowth(obj2.getFileName(), obj3.getFileName(), oFile, minSup, maxDist)
        spatialFpGrowth.readDataBase()
        spatialFpGrowth.sortTransaction()
        spatialFpGrowth.createSpatialFPTree()
        spatialFpGrowth.createAllSpatialFrequentPattern()