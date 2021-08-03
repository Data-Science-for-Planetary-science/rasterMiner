import sys
from tkinter import *
from tkinter import filedialog
# import re
# import ast
from tkinter import messagebox
from sklearn.cluster import OPTICS
import numpy as np

class optics:
    def __init__(self,*args):
        if len(args) == 3:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.minSamples = args[2]
            self.maxEps = 'inf'
            self.metric = 'minkowski'
            self.leafSize = 30
            self.p = 2
            self.metricParams = 'None'
            self.clusterMethod = 'xi'
            self.eps = 'None'
            self.xi = 0.05
            self.preCorrect = 'True'
            self.minClusterSize = 'None'
            self.alg = 'auto'
        elif len(args) == 4:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.minSamples = args[2]
            self.maxEps = args[3]
            self.metric = 'minkowski'
            self.leafSize = 30
            self.p = 2
            self.metricParams = 'None'
            self.clusterMethod = 'xi'
            self.eps = 'None'
            self.xi = 0.05
            self.preCorrect = 'True'
            self.minClusterSize = 'None'
            self.alg = 'auto'

        elif len(args) == 14:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.minSamples = args[2]
            self.maxEps = args[3]
            self.metric = args[4]
            self.leafSize = args[5]
            self.p = args[6]
            self.metricParams = args[7]
            self.clusterMethod = args[8]
            self.eps = args[9]
            self.xi = args[10]
            self.preCorrect = args[11]
            self.minClusterSize = args[12]
            self.alg = args[13]

    def run(self):
        outputfile = self.outputDir + '/result_optics' + str(self.eps) + '.csv'
        orderOutput = self.outputDir + '/cluster_ordering_optics' + str(self.eps) + '.csv'

        self.minSamples = int(self.minSamples)
        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            self.minSamples = float(self.minSamples)
            if self.minClusterSize == 'None':
                self.minClusterSize = None
            else:
                if self.minClusterSize < 1:
                    self.minClusterSize = float(self.minClusterSize)
                elif self.minClusterSize > 1:
                    self.minClusterSize = int(self.minClusterSize)
            if self.minSamples > 1:
                self.minSamples = int(self.minSamples)
            elif 0 <= self.minSamples <= 1:
                self.minSamples = float(self.minSamples)
            if self.metricParams == 'None':
                self.metricParams = None
            else:
                self.metricParams = dict(self.metricParams)
            if self.eps == 'None':
                self.eps = None
            else:
                self.eps = float(self.eps)
            if self.maxEps == 'inf':
                self.maxEps = np.inf
            else:
                self.maxEps = float(self.maxEps)

            of = open(outputfile, 'w')
            of2 = open(orderOutput,'w')
            f = open(self.inputFile, 'r')
            data = []
            # data1=[]
            pts = []
            header = f.readline()

            for i in f:
                j = i.strip('\n').split('\t')
                for r in range(2, len(j)):
                    j[r] = float(j[r])
                pts.append(j[0:1])
                data.append(j[1:])
            X = np.array(data)
            #X_precomputed = pairwise_distances(X, metric='manhattan')
            clustering = OPTICS(min_samples=self.minSamples,max_eps=self.maxEps,metric=self.metric,p=int(self.p)
                                ,metric_params=self.metricParams,cluster_method=self.clusterMethod,eps=self.eps,xi=self.xi
                                ,predecessor_correction=self.preCorrect,min_cluster_size=self.minClusterSize,algorithm=self.alg
                                ,leaf_size=self.leafSize).fit(X)
            wr = clustering.labels_
            ord = clustering.ordering_

            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = str(','.join(pts[p])) + '\t' + str(wr[p]) + '\n'
                of.write(stri)
            for j in range(len(X)):
                stri = str('.'.join(pts[j])) + '\t' + str(ord[j]) + '\n'
                of2.write(stri)
            messagebox.showinfo('notification', 'Successfully completed')


if __name__ == '__main__':
    if len(sys.argv) == 4:
        obj = optics(sys.argv[1], sys.argv[2], sys.argv[3])
        obj.run()
    elif len(sys.argv) == 5:
        obj = optics(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        obj.run()
    elif len(sys.argv) == 15:
        obj = optics(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]
                     ,sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14])
        obj.run()
    else:
        print('Please enter in one of the following format:'
              '1. python optics.py <inputFile> <outputFile> <minSamples>'
              '2. python optics.py <inputFile> <outputFile> <minSamples> <maxEps>'
              '3. python optics.py <inputFile> <outputFile> <minSamples> <maxEps> <metric> <leaf size> <power> <metric params> <cluster method> <eps> <xi> <predecessor_correction> <min_cluster_size> <algorithm>')
