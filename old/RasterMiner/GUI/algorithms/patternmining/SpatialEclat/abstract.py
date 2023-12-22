from abc import ABC, abstractmethod
import time
import csv
import pandas as pd
from collections import defaultdict
from itertools import combinations as c
import os
import os.path
import psutil


class frequentPatterns(ABC):
    """ This abstract base class defines the variables and methods that every frequent pattern mining algorithm must
    employ in PAMI
        ...
        Attributes
        ----------
        iFile : str
            Input file name or path of the input file
        minSup: float
            UserSpecified minimum support value. It has to be given in terms of count of total number of transactions
            in the input database/file
        startTime:float
            To record the start time of the algorithm
        endTime:float
            To record the completion time of the algorithm
        finalPatterns: dict
            Storing the complete set of patterns in a dictionary variable
        oFile : str
            Name of the output file to store complete set of frequent patterns
        memoryUSS : float
            To store the total amount of USS memory consumed by the program
        memoryRSS : float
            To store the total amount of RSS memory consumed by the program
        Methods
        -------
        startMine()
            Mining process will start from here
        getFrequentPatterns()
            Complete set of patterns will be retrieved with this function
        storePatternsInFile(oFile)
            Complete set of frequent patterns will be loaded in to a output file
        getPatternsInDataFrame()
            Complete set of frequent patterns will be loaded in to data frame
        getMemoryUSS()
            Total amount of USS memory consumed by the program will be retrieved from this function
        getMemoryRSS()
            Total amount of RSS memory consumed by the program will be retrieved from this function
        getRuntime()
            Total amount of runtime taken by the program will be retrieved from this function
    """

    def __init__(self, iFile, minSup):
        """
        :param iFile: Input file name or path of the input file
        :type iFile: str
        :param minSup: UserSpecified minimum support value. It has to be given in terms of count of total number of
        transactions in the input database/file
        :type minSup: float
        """

        self.iFile = iFile
        self.minSup = minSup

    @abstractmethod
    def iFile(self):
        """Variable to store the input file path/file name"""

        pass

    @abstractmethod
    def minSup(self):
        """Variable to store the user-specified minimum support value"""

        pass

    @abstractmethod
    def startTime(self):
        """Variable to store the start time of the mining process"""

        pass

    @abstractmethod
    def endTime(self):
        """Variable to store the end time of the complete program"""

        pass

    @abstractmethod
    def memoryUSS(self):
        """Variable to store the end time of the complete program"""

        pass

    @abstractmethod
    def memoryRSS(self):
        """Variable to store the end time of the complete program"""

        pass

    @abstractmethod
    def finalPatterns(self):
        """Variable to store the complete set of patterns in a dictionary"""

        pass

    @abstractmethod
    def oFile(self):
        """Variable to store the name of the output file to store the complete set of frequent patterns"""

        pass

    @abstractmethod
    def startMine(self):
        """Code for the mining process will start from this function"""

        pass

    @abstractmethod
    def getFrequentPatterns(self):
        """Complete set of frequent patterns generated will be retrieved from this function"""

        pass

    @abstractmethod
    def storePatternsInFile(self, oFile):
        """Complete set of frequent patterns will be saved in to an output file from this function
        :param oFile: Name of the output file
        :type oFile: file
        """

        pass

    @abstractmethod
    def getPatternsInDataFrame(self):
        """Complete set of frequent patterns will be loaded in to data frame from this function"""

        pass

    @abstractmethod
    def getMemoryUSS(self):
        """Total amount of USS memory consumed by the program will be retrieved from this function"""

        pass

    @abstractmethod
    def getMemoryRSS(self):
        """Total amount of RSS memory consumed by the program will be retrieved from this function"""
        pass

    @abstractmethod
    def getRuntime(self):
        """Total amount of runtime taken by the program will be retrieved from this function"""

        pass