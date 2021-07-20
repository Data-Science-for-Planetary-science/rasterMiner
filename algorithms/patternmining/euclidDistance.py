import sys
from math import sqrt

class EuclidDistance:
    def __init__(self,iFile,oFile,threshold):
        self.iFile = iFile
        self.oFile = oFile
        self.threshold = threshold

    def run(self):
        coordinates = []
        result = {}
        with open(self.iFile,"r") as f:
            for line in f:
                l = line.rstrip().split("\t")
                coordinates.append(l[0].rstrip().split(" "))

        for i in range(len(coordinates)):
            for j in range(len(coordinates)):
                if i != j:
                    firstCoordinate = coordinates[i]
                    secondCoordinate = coordinates[j]
                    x1 = float(firstCoordinate[0])
                    y1 = float(firstCoordinate[1])
                    x2 = float(secondCoordinate[0])
                    y2 = float(secondCoordinate[1])
                    ansX = x2-x1
                    ansY = y2-y1
                    dist = abs(pow(ansX,2) - pow(ansY,2))
                    norm = sqrt(dist)
                    print(norm)
                    if norm <= float(self.threshold):
                        result[tuple(firstCoordinate)] = result.get(tuple(firstCoordinate),[])
                        result[tuple(firstCoordinate)].append(secondCoordinate)

        with open(self.oFile,"w") as f:
            for i in result:
                # s = str(i)+"\t"
                f.write(f"{i[0]} {i[1]}\t")
                for j in result[i]:
                    f.write(f"{j[0]} {j[1]}\t")    
                f.write("\n")

    def getFileName(self):
        return self.oFile

if __name__ == "__main__":
    euclid = EuclidDistance(sys.argv[1],sys.argv[2],sys.argv[3])
    euclid.startMine()

