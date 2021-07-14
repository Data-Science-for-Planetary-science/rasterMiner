from tkinter import *
from tkinter import filedialog
# import re
# import ast
from tkinter import messagebox
# import final_code
from GUI import GUImain
from sklearn.cluster import dbscan
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import numpy as np

class :
    def __init__(self,inputFile,outputDirectory,epsi,minpts):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.epsi = epsi
        self.minpts = minpts

    def run(self):
        outputfile = self.outputDir.get() + '/result_DBScan_' + str(self.epsi) + '_' + str(self.minpts) + '.csv'

        if (self.inputFile == '' or self.outputDir == '' or self.epsi == '' or self.minpts==''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            of = open(outputfile, 'w')
            print(self.inputFile)
            f = open(self.inputFile, 'r')
            data = []
            # data1=[]
            pts = []
            for i in f:
                j = i.strip('\n').split(' ')
                for r in range(1, len(j)):
                    j[r] = float(j[r])
                pts.append(j[0])
                data.append(j[1:])
            z = np.array(data)
            X = StandardScaler().fit_transform(z)

            dbs = dbscan().fit(X)
            labels = dbs.labels_

            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            n_noise_ = list(labels).count(-1)
            for p in range(len(z)):
                stri=pts[p]+','+str(labels[p])+'\n'
                of.write(stri)
            of.close()