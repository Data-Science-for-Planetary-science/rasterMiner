import numpy as np
import time
import math
#from scipy.spatial.distance import directed_hausdorff
import sys

class OneNNHausdorff:
    """"""

    def __init__(self, inputTrainingFile, inputTestingFile):
        """Constructor for OneNNHausdorff"""
        self.training = np.loadtxt(inputTrainingFile, delimiter='\t')
        self.testing = np.loadtxt(inputTestingFile, delimiter='\t')
    def hausdorff(self, u, v):
        row, = u.shape
        lea_distance = 0
        for i in range(row):
            #for j in range(column):
            distance1 = np.amin(np.absolute((np.diff(u[i]-v))))
            if distance1 > lea_distance:
                lea_distance = distance1
        return lea_distance

    def run(self):
        num_rows_test, num_columns_test = self.testing.shape
        num_rows_train, num_columns_train = self.training.shape
        training_noclass=self.training[:,1:]
        testing_noclass=self.testing[:,1:]

        predicted_label = None
        correct = 0
        start_time = time.time()
        for i in range(num_rows_test):
            least_distance = float('inf')
            for j in range(num_rows_train):
                dist = max(self.hausdorff(testing_noclass[i], training_noclass[j]), self.hausdorff(training_noclass[j], testing_noclass[i]))  # math.sqrt(squaring)
                if dist < least_distance:
                    predicted_label = self.training[j][0]
                    least_distance = dist
            if predicted_label == self.testing[i][0]:
                correct = correct + 1


        accuracy = (correct/num_rows_test) * 100
        print("Datasetname:",sys.argv[1])

        print("Total Accuracy of oneNNHausdorff is:", accuracy)

        print("Total Execution time of oneNNHausdorff", time.time() - start_time)
        import os
        import psutil
        process = psutil.Process(os.getpid())
        memory = process.memory_full_info().uss
        memory_in_KB = memory /(1024)
        print("Total Memory of oneNNHausdorff inKB",memory_in_KB)  # in bytes
if __name__ == '__main__':
    obj = OneNNHausdorff(sys.argv[1], sys.argv[2])
    obj.run()