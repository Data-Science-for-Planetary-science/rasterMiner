from collections import OrderedDict
import createDenseDF
import dense2DB
import euclidDistance


class Node:
    def __init__(self):
        self.supportCount = 0
        self.children = {}
        self.prefix = []
        self.nextNode = None
        self.coordinates = []
        self.neighbour = []
        self.parent = None
        self.value = None


class Tree:
    def __init__(self) -> None:
        self.root = Node()
        self.nodeLinks = OrderedDict()
        self.nodeLastLinks = {}
        self.fpList = []

    def createNode(self, items, supportCount):
        currentNode = self.root
        for item in items:
            if item in currentNode.children:
                currentNode.children[item].supportCount += supportCount
            else:
                currentNode.children[item] = Node()
                currentNode.children[item].supportCount += supportCount
                currentNode.children[item].value = item
                currentNode.children[item].prefix = items[0:items.index(item)]
                currentNode.children[item].parent = currentNode
                self.linkNode(currentNode.children[item])
            currentNode = currentNode.children[item]

    """def createSNode(self,prefix,supportCount):
        currentNode = self.root
        for item in prefix:
            if item in currentNode.children:
                currentNode.children[item].supportCount += supportCount
            else:
                currentNode.children[item] = Node()
                currentNode.children[item].supportCount += supportCount
                currentNode.children[item].value = item
                currentNode.children[item].prefix = prefix[0:prefix.index(item)]
                currentNode.children[item].parent = currentNode
                self.linkNode(currentNode.children[item])
            currentNode = currentNode.children[item]"""

    def linkNode(self, node):
        if node.value in self.nodeLinks:
            self.nodeLastLinks[node.value].nextNode = node
            self.nodeLastLinks[node.value] = node
        else:
            self.nodeLinks[node.value] = node
            self.nodeLastLinks[node.value] = node


class spatialFpGrowth:
    def __init__(self, iFile, nFile, minSup):
        self.finalPatterns = []
        self.transaction = []
        self.iFile = iFile
        self.nFile = nFile
        self.neighbourList = {}
        self.minSup = minSup
        self.fpList = []
        self.fpTree = Tree()

    def readDataBase(self):
        oneFrequentItem = {}

        with open(self.iFile, "r") as f:
            for line in f:
                l = line.rstrip().split('\t')
                l = [tuple(item.rstrip().split(' ')) for item in l]
                self.transaction.append(l)
                for item in l:
                    oneFrequentItem[item] = oneFrequentItem.get(item, 0) + 1
        oneFrequentItem = {key: value for key, value in oneFrequentItem.items() if value >= self.minSup}
        self.fpList = list(dict(sorted(oneFrequentItem.items(), key=lambda x: x[1], reverse=True)))
        self.finalPatterns.extend(self.fpList)
        print("the number of self.fplist : ",len(self.fpList))

        with open(self.nFile,"r") as nf:
            for line in nf:
                l = line.rstrip().split('\t')
                key = tuple(l[0].rstrip().split(' '))
                for i in range(len(l)):
                    if i == 0:
                        self.neighbourList[key] = []
                    else:
                        self.neighbourList[key].append(tuple(l[i].rstrip().split(' ')))



    def sortTransaction(self):
        for i in range(len(self.transaction)):
            self.transaction[i] = [item for item in self.transaction[i] if item in self.fpList]
            self.transaction[i].sort(key=lambda value: self.fpList.index(value))


    def createSpatialFPTree(self):
        for items in self.transaction:
            self.fpTree.createNode(items, 1)


    def createSpatialConditionalPatternBase(self, node):
        partialTree = Tree()
        currentNode = node
        while True:
            currentNode.prefix = [item for item in currentNode.prefix if item in self.neighbourList[currentNode.value]]
            partialTree.createNode(currentNode.prefix,currentNode.supportCount)
            if currentNode.nextNode is None:
                break
            currentNode = currentNode.nextNode
        return partialTree


    def createAllSpatialFrequentPattern(self):
        for item in reversed(self.fpList):
            self.createSpatialFrequentPattern(self.fpTree.nodeLinks[item],self.fpTree.nodeLinks[item].value)


    def createSpatialFrequentPattern(self, node, suffixItem):
        pTree = self.createSpatialConditionalPatternBase(node)
        frequentItems = {}
        for item in reversed(pTree.nodeLinks):
            currentNode = pTree.nodeLinks[item]
            while True:
                frequentItems[item] = frequentItems.get(item, 0) + currentNode.supportCount
                if currentNode.nextNode is None:
                    break
                currentNode = currentNode.nextNode
        frequentItems = {key:value for key,value in frequentItems.items() if value >= self.minSup}
        if len(frequentItems) != 0:
            for item in frequentItems:
                if type(suffixItem) == set:
                    pattern = suffixItem.union({item})
                else:
                    pattern = {suffixItem}.union({item})

                if pattern not in self.finalPatterns:
                    self.finalPatterns.append(pattern)
                    self.createSpatialFrequentPattern(pTree.nodeLinks[item], pattern)

    def getFrequentPatterns(self):
        return self.finalPatterns

    def storePatternInFile(self, oFile):
        with open(oFile,"w") as f:
            self.finalPatterns.sort(key=len)
            for items in self.finalPatterns:
                pattern = ""
                for item in items:
                    pattern += str(item) + " "
                pattern += "\n"
                f.write(pattern)

    def startMine(self):
        self.readDataBase()
        self.sortTransaction()
        self.createSpatialFPTree()
        self.createAllSpatialFrequentPattern()


if __name__ == "__main__":
    dFile = "/Users/masuyudai/runDataTranspose/Data/spatialData_100.tsv"
    oFile = "output.txt"
    nFile = "neighbour.txt"
    minSup = 3
    condition = ">="
    value = 4500
    maxDist = 50
    obj = createDenseDF.createDenseDF(dFile)
    obj2 = dense2DB.dense2DB(obj.getDF(), condition, value)
    obj2.createTransactional("sampleTDB.csv")
    obj3 = euclidDistance.EuclidDistance(dFile, nFile, maxDist)
    obj3.run()
    spatialFpGrowth = spatialFpGrowth(obj2.getFileName(), obj3.getFileName(), oFile, minSup)
    spatialFpGrowth.readDataBase()
    spatialFpGrowth.sortTransaction()
    spatialFpGrowth.createSpatialFPTree()
    spatialFpGrowth.createAllSpatialFrequentPattern()
    """print(spatialFpGrowth.neighbourList)"""
    print("spatial frequent pattern")
    print("the number of frequent patterns : ",len(spatialFpGrowth.getFrequentPatterns()))
    spatialFpGrowth.storePatternInFile()
    """for i in spatialFpGrowth.finalPatterns:
        if len(i) <= 2:
            print(i)"""

