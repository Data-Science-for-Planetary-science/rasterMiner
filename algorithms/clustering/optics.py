from tkinter import *
from tkinter import filedialog
# import re
# import ast
from tkinter import messagebox
# import final_code
from GUI import main
from sklearn.cluster import OPTICS
from sklearn.metrics import pairwise_distances
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
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
        outputfile = self.outputDir + '/result_spectralClustering' + str(self.k) + '_' + str(self.eigenSolver) + '.csv'
        otc = self.outputDir + '/centers_spectralClustering' + str(self.k) + '_' + str(self.eigenSolver) + '.csv'

        if (self.inputFile == '' or self.outputDir == '' or self.k == '' or self.n_init==''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            if self.random_state == '':
                self.random_state = None


            of = open(outputfile, 'w')
            f = open(self.inputFile, 'r')
            oc = open(otc, 'w')
            data = []
            # data1=[]
            pts = []

            for i in f:
                j = i.strip('\n').split(' ')
                for r in range(1, len(j)):
                    j[r] = float(j[r])
                pts.append(j[0])
                data.append(j[1:])
            X = np.array(data)
            #X_precomputed = pairwise_distances(X, metric='manhattan')
            spectralClustering = OPTICS(n_clusters=int(self.k),=self.eigenSolver,random_state=self.random_state,
                                                    n_init=int(self.n_init),gamma=float(self.gamma),affinity=self.affinity,
                                                    n_neighbors=int(self.n_neighbor),assign_labels=self.assign_labels,degree=float(self.degree),
                                                    coef0=float(self.coef0)).fit(X)

            labels = spectralClustering.labels_

            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = pts[p] + ',' + str(labels[p]) + '\n'
                of.write(stri)
            of.close()
            print(spectralClustering.affinity_matrix_)