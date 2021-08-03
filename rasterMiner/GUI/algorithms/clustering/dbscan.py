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
    def __init__(self,*args):
        if len(args) == 3:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.epsi = args[2]
            self.minpts = 5
            self.leafSize = 30
            self.power = 'None'
            self.metric = 'euclidean'
            self.metricParams = 'None'
            self.alg = 'auto'
        elif len(args) == 4:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.epsi = args[2]
            self.minpts = args[3]
            self.leafSize = 30
            self.power = 'None'
            self.metric = 'euclidean'
            self.metricParams = 'None'
            self.alg = 'auto'

        elif len(args) == 9:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.epsi = args[2]
            self.minpts = args[3]
            self.leafSize = args[4]
            self.power = args[5]
            self.metric = args[6]
            self.metricParams = args[7]
            self.alg = args[8]

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
            messagebox.showinfo('notification', 'Successfully completed')

if __name__ == '__main__':
    if len(sys.argv) == 4:
        obj = DBScan(sys.argv[1], sys.argv[2], sys.argv[3])
        obj.run()
    elif len(sys.argv) == 5:
        obj = DBScan(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        obj.run()
    elif len(sys.argv) == 10:
        obj = DBScan(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
        obj.run()
    else:
        print('Please enter in one of the following format:'
              '1. python dbscan.py <inputFile> <outputFile> <eps>'
              '2. python dbscan.py <inputFile> <outputFile> <eps> <minSample>'
              '3. python dbscan.py <inputFile> <outputFile> <eps> <minSample> <leaf size> <power> <metric> <metric params> <algorithm> ')
