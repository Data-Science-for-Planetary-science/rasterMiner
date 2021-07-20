from tkinter import *
from tkinter import filedialog
# import re
# import ast
from tkinter import messagebox
# import final_code
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import numpy as np

class DBScan:
    def __init__(self,inputFile,outputDirectory,epsi,minpts,leafSize,power,metric,metricParams,alg):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.epsi = epsi
        self.minpts = minpts
        self.leafSize = leafSize
        self.power = power
        self.metric = metric
        self.metricParams = metricParams
        self.alg = alg

    def run(self):
        outputfile = self.outputDir + '/result_DBScan_' + str(self.epsi) + '_' + str(self.minpts) + '.csv'

        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")

        else:
            if self.metricParams == 'None':
                self.metricParams = None
            else:
                self.metricParams = dict(self.metricParams)
            if self.power == 'None':
                self.power = None
            else:
                self.power = float(self.power)
            of = open(outputfile, 'w')
            print(self.inputFile)
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
            z = np.array(data)
            X = StandardScaler().fit_transform(z)

            dbs = DBSCAN(eps=float(self.epsi),min_samples=int(self.minpts),metric=self.metric,metric_params=self.metricParams
                         ,algorithm=self.alg,leaf_size=int(self.leafSize),p=self.power).fit(X)
            labels = dbs.labels_

            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            n_noise_ = list(labels).count(-1)
            for p in range(len(z)):
                stri=str(','.join(pts[p])) +'\t'+str(labels[p])+'\n'
                of.write(stri)
            of.close()