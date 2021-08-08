import spatialFPGrowth as sfp


class runSpatialFpGrowth:
    def __init__(self, iFile, nFile, oFolder, minSup):
        self.iFile = iFile
        self.nFile = nFile
        self.oFile = oFolder+"/output_sfp.csv"
        self.minSup = int(minSup)


    def run(self):
        spatialFpGrowth = sfp.spatialFpGrowth(self.iFile, self.nFile, self.minSup)
        spatialFpGrowth.startMine()
        spatialFpGrowth.storePatternInFile(self.oFile)

