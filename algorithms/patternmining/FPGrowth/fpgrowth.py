from types import TracebackType
from collections import OrderedDict
import sys

class Node:
    def __init__(self):
        self.supportCount = 0
        self.children = {}
        self.prefix = []
        self.nextNode = None
        self.value = None
        self.parent = None

class Tree:
    def __init__(self) -> None:
        self.root = Node()
        self.nodeLinks = OrderedDict()
        self.nodeLastLinks = {}
        self.fpList = []

    def createNode(self,items,supportCount):
        currentNode = self.root
        for item in items:
            if item in currentNode.children:
                currentNode.children[item].supportCount +=  supportCount
            else:
                currentNode.children[item] = Node()
                currentNode.children[item].supportCount += supportCount
                currentNode.children[item].value = item
                currentNode.children[item].prefix = items[0:items.index(item)]
                currentNode.children[item].parent = currentNode
                self.linkNode(currentNode.children[item])
            currentNode = currentNode.children[item]
    
    def linkNode(self,node):
        if node.value in self.nodeLinks:
            self.nodeLastLinks[node.value].nextNode = node
            self.nodeLastLinks[node.value] = node
        else:
            self.nodeLinks[node.value] = node
            self.nodeLastLinks[node.value] = node
        
class FpGrowth:
    def __init__(self,iFile,oFile,minSup):
        self.finalPatterns = []
        self.transaction = []
        self.iFile = iFile
        self.oFile = oFile
        self.minSup = minSup
        self.fpList = []
        self.fpTree = Tree()
    
    def readDataBase(self):
        oneFrequentItem = {}
        with open(self.iFile,"r") as f:
            for line in f:
                l = line.rstrip().split(',')
                self.transaction.append(l)
                for item in l:
                    oneFrequentItem[item] = oneFrequentItem.get(item,0) + 1
        oneFrequentItem = {key:value for key,value in oneFrequentItem.items() if value >= self.minSup}
        self.fpList = list(dict(sorted(oneFrequentItem.items(),key=lambda x:x[1],reverse=True)))
        self.finalPatterns.extend(self.fpList)


    def sortTransaction(self):
        for i in range(len(self.transaction)):
            self.transaction[i] = [item for item in self.transaction[i] if item in self.fpList]
            self.transaction[i].sort(key=lambda value: self.fpList.index(value))


    def createFPTree(self):
        for items in self.transaction:
            self.fpTree.createNode(items,1)

    def createConditionalPatternBase(self,node):
        partialTree = Tree()
        currentNode = node
        while True:
            partialTree.createNode(currentNode.prefix,currentNode.supportCount)
            if currentNode.nextNode is None:
                break
            currentNode = currentNode.nextNode
        return partialTree
        
    def createAllFrequentPattern(self):
        for item in reversed(self.fpList):
            self.createFrequentPattern(self.fpTree.nodeLinks[item],self.fpTree.nodeLinks[item].value)

    def createFrequentPattern(self,node,suffixItem):
        pTree = self.createConditionalPatternBase(node)
        frequentItems = {}
        for item in reversed(pTree.nodeLinks):
            currentNode = pTree.nodeLinks[item]
            while currentNode is not None:
                frequentItems[item] = frequentItems.get(item,0) + currentNode.supportCount
                currentNode = currentNode.nextNode
        frequentItems = {key:value for key,value in frequentItems.items() if value >= self.minSup}

        if len(frequentItems) != 0:
            """print("suffixItem : ", suffixItem)
            print("frequentItems : ", frequentItems)"""
            for item in frequentItems:
                if type(suffixItem) == set:
                    pattern = suffixItem.union({item})
                else:
                    pattern = {suffixItem}.union({item})

                if pattern not in self.finalPatterns:
                    self.finalPatterns.append(pattern)
                    self.createFrequentPattern(pTree.nodeLinks[item], pattern)

    def startMine(self):
        self.readDataBase()
        self.sortTransaction()
        self.createFPTree()
        self.createAllFrequentPattern()


    def getFrequentPatterns(self):
        return self.finalPatterns


    def storePatternInFile(self):
        with open(self.oFile,"w") as f:
            for items in self.finalPatterns:
                for item in items:
                    pattern = str(item) + " "
                pattern += "\n"
                f.write(pattern)



if __name__=="__main__":
    """iFile = sys.argv[1]
    oFile = sys.argv[2]
    minSup = sys.argv[3]
    fp = FpGrowth(iFile,oFile,minSup)
    fp.readDataBase()
    fp.sortTransaction()
    fp.createFPTree()
    fp.createAllFrequentPattern()"""

    fp = FpGrowth("/Users/masuyudai/runDataTranspose/Data/transactional_T10I4D100K.csv","output.txt",1000)
    fp.readDataBase()
    fp.sortTransaction()
    fp.createFPTree()
    fp.createAllFrequentPattern()
    print(len(fp.finalPatterns))
