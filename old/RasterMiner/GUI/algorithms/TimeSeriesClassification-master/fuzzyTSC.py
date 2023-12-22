#import pandas as pd
import numpy as np
#from _collections import defaultdict
#import matplotlib.pyplot as plt
import time
import os
import psutil
import gc
import sys

class fuzzyTSC():
    """"""

    def __init__(self, inputTrainingFile, inputTestingFile):
        """Constructor for fuzzyTSC"""
        self.training = np.loadtxt(inputTrainingFile, delimiter='\t')
        self.testing = np.loadtxt(inputTestingFile, delimiter='\t')
    def run(self):
        start_time = time.time()
        mean_data = {} #defaultdict()
        min_data = {}#defaultdict()
        max_data= {}#defaultdict()


        # seperating classes into different dictionary variables and creating mean, min and max curves
        for i in (np.unique(self.training[:,0])):
            max_data[i] = np.amax(self.training[self.training[:,0] == i], axis = 0)
            mean_data[i] = np.mean(self.training[self.training[:,0] == i], axis= 0)
            min_data[i]= np.amin(self.training[self.training[:,0] == i], axis=0)

        del self.training
        gc.collect()


        # Classification Phase

        counter = {}#defaultdict()
        num_rows, num_columns = self.testing.shape
        correct = 0
        #mem = defaultdict()
        #start_time = time.time()
        for i in range(num_rows):
            for k in (np.unique(self.testing[:,0])):
                counter[k] = 0.0
                for j in range(num_columns-1):
                    if self.testing[i][j+1] >= mean_data[k][j+1]:
                        if self.testing[i][j+1]<= max_data[k][j+1]:
                            counter[k] = counter[k] + 0.5* (self.testing[i][j+1] - mean_data[k][j+1]) / (max_data[k][j+1] - mean_data[k][j+1])
                        else:
                            counter[k] = counter[k]+ 1
                    else:
                        if self.testing[i][j+1] >= min_data[k][j+1]:
                            counter[k] = counter[k] + 0.5 * (mean_data[k][j+1] - self.testing[i][j+1]) / (mean_data[k][j+1] - min_data[k][j+1])
                        else:
                            counter[k] = counter[k]+1
                #counter[k] = counter[k]/num_columns-1

            for k in (np.unique(self.testing[:,0])):
                counter[k] = (counter[k]) / num_columns-1

            if min(counter, key=counter.get) == self.testing[i][0]:
                correct = correct + 1
        accuracy = (correct / num_rows) * 100
        #gc.collect()
        print("Dataset name:", sys.argv[1])
        print("Total Accuracy of proposedAlgo is:", accuracy)

        print("Total Execution time of proposedAlgo", time.time() - start_time)
            # print(testing[i,0])
        process = psutil.Process(os.getpid())
        memory = process.memory_full_info().uss
        memory_in_KB = memory / (1024 )
        print("Memory of proposedAlgo in KB:",memory_in_KB)  # in bytes

if __name__ == '__main__':
    obj = fuzzyTSC(sys.argv[1], sys.argv[2])
    obj.run()
