from tkinter import *
from tkinter import filedialog
# import re
# import ast
from tkinter import messagebox
from sklearn.cluster import OPTICS
import numpy as np

class optics:
    def __init__(self,inputFile,outputDirectory,minSamples,maxEps,metric,p,metricParams,clusterMethod,eps,xi,preCorrect,leafSize,minClusterSize,alg):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.minSamples = minSamples
        self.maxEps = maxEps
        self.metric = metric
        self.leafSize = leafSize
        self.p = p
        self.metricParams = metricParams
        self.clusterMethod = clusterMethod
        self.eps = eps
        self.xi = xi
        self.preCorrect = preCorrect
        self.minClusterSize = minClusterSize
        self.alg = alg

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
                for r in range(1, len(j)):
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
                stri = str(','.join(pts[p])) + ',' + str(wr[p]) + '\n'
                of.write(stri)
            for j in range(len(X)):
                stri = str('.'.join(pts[j])) + ',' + str(ord[j]) + '\n'
                of2.write(stri)