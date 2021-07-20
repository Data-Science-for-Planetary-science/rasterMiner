from tkinter import *
from tkinter import filedialog
# import re
# import ast
from tkinter import messagebox
# import final_code
from GUI import GUImain
from sklearn.cluster import Birch
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import numpy as np

class BIRCH:
    def __init__(self,inputFile,outputDirectory,threshold,branchingFactor,computeLabels,n_cluster):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.threshold = threshold
        self.branchFactor = branchingFactor
        self.computeLabels = computeLabels
        self.nCluster = n_cluster
    def run(self):

        outputfile = self.outputDir + '/result_birch' + str(self.threshold) + '_' + str(self.threshold) + '.csv'
        # otc = self.outputDir + '/centers_K-means_' + str(self.k) + '_' + str(self.threshold) + '.csv'
        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:

            of = open(outputfile, 'w')
            print(self.inputFile)
            f = open(self.inputFile, 'r')
            header = f.readline()
            # oc = open(otc, 'w')
            data = []
            # data1=[]
            pts = []
            for i in f:
                j = i.strip('\n').split('\t')
                for r in range(2, len(j)):
                    j[r] = float(j[r])
                pts.append(j[0:1])
                data.append(j[1:])
            X = np.array(data)
            birch = Birch(n_clusters=int(self.nCluster),threshold=float(self.threshold),branching_factor=int(self.branchFactor)
                            ,compute_labels=bool(self.computeLabels)).fit(X)
            wr = birch.labels_
            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = pts[p] + '\t' + str(wr[p]) + '\n'
                of.write(stri)
            of.close()
            # for j in birch.cluster_centers_:
            #     text = 'Center-' + str(co)
            #     for d in j:
            #         text += ',' + str(d)
            #     text += '\n'
            #     oc.write(text)
            #     co += 1
            # oc.close()

