from tkinter import *
from tkinter import messagebox
from sklearn.cluster import SpectralClustering
import numpy as np
class spectralClustering:

    def __init__(self,*args):
        if len(args) == 3:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.eigenSolver = None
            self.n_init = 10
            self.gamma = 1.0
            self.random_state = None
            self.n_neighbors = 10
            self.assign_labels = 'kmeans'
            self.degree = 3
            self.coef0 = 1
            self.affinity = 'nearest_neighbors'

        elif len(args) == 4:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.eigenSolver = None
            self.n_init = 10
            self.gamma = 1.0
            self.random_state = None
            self.n_neighbors = 10
            self.assign_labels = 'kmeans'
            self.degree = 3
            self.coef0 = 1
            self.affinity = args[3]
        elif len(args) == 12:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.affinity = args[3]
            self.eigenSolver = args[4]
            self.n_init = args[5]
            self.gamma = args[6]
            self.random_state = args[7]
            self.n_neighbors = args[8]
            self.assign_labels = args[9]
            self.degree = args[10]
            self.coef0 = args[11]

    def run(self):
        outputfile = self.outputDir + '/result_spectralClustering' + str(self.k) + '_' + str(self.eigenSolver) + '.csv'
        # otc = self.outputDir + '/centers_spectralClustering' + str(self.k) + '_' + str(self.eigenSolver) + '.csv'

        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            if self.random_state == 'None':
                self.random_state = None
            of = open(outputfile, 'w')
            f = open(self.inputFile, 'r')
            # oc = open(otc, 'w')
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
            spectralClustering = SpectralClustering(n_clusters=int(self.k),eigen_solver=self.eigenSolver,random_state=self.random_state,
                                                    n_init=int(self.n_init),gamma=float(self.gamma),affinity=self.affinity,
                                                    n_neighbors=int(self.n_neighbors),assign_labels=self.assign_labels,degree=float(self.degree),
                                                    coef0=float(self.coef0)).fit(X)

            labels = spectralClustering.labels_

            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = str(','.join(pts[p])) + '\t' + str(labels[p]) + '\n'
                of.write(stri)
            of.close()
            # print(spectralClustering.affinity_matrix_)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        obj = spectralClustering(sys.argv[1], sys.argv[2], sys.argv[3])
        obj.run()
    elif len(sys.argv) == 5:
        obj = spectralClustering(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        obj.run()
    elif len(sys.argv) == 13:
        obj = spectralClustering(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
                                 ,sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12])
        obj.run()
    else:
        print('Please enter in one of the following format:'
              '1. python spectoralClustering.py <inputFile> <outputFile> <kValue>'
              '2. python spectoralClustering.py <inputFile> <outputFile> <kValue> <affinity>'
              '3. python spectoralClustering.py <inputFile> <outputFile> <kValue> <affinity> <eigen solver> <n_init> <gamma> <random_state>  ')
