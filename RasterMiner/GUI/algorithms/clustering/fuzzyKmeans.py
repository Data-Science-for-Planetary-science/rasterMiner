from tkinter import messagebox
from sklearn_extensions.fuzzy_kmeans import FuzzyKMeans
import numpy as np
import sys
import csv

class fuzzyKmeans:
    def __init__(self, *args):
        if len(args) == 3:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            #assert m > 1
            self.m = 2
            self.max_iter = 100
            self.random_state = 0
            self.tol = 1e-4
        elif len(args) == 7:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            assert int(args[3]) > 1
            self.m = args[3]
            self.max_iter = args[4]
            self.random_state = args[5]
            self.tol = args[6]
        else:
            print('Error message print')


    def run(self):
        outputfile = self.outputDir + '/result_fuzzy-K-means_' + str(self.k) + '_' + str(self.max_iter) + '.csv'
        otc = self.outputDir + '/centers_fuzzy-K-means_' + str(self.k) + '_' + str(self.max_iter) + '.csv'

        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")

        else:
            if self.random_state == 'None':
                self.random_state = None
            else:
                self.random_state = self.random_state
            of = open(outputfile, 'w')
            print(self.inputFile)
            f = open(self.inputFile, 'r')
            header = f.readline()

            oc = open(otc, 'w')
            data = []
            # data1=[]
            pts = []
            for i in f:
                j = i.strip('\n').split('\t')
                for r in range(2, len(j)):
                    # print(j[r])
                    j[r] = j[r].replace('"','')
                    j[r] = float(j[r])
                pts.append(j[0:1])
                data.append(j[1:])
                # print(pts)

            X = np.array(data,dtype='float64')
            # X = np.mean(np.var(X,0))
            fuzzykmeans = FuzzyKMeans(k=int(self.k),m=int(self.m),max_iter=int(self.max_iter),random_state=int(self.random_state),tol=float(self.tol))
            fuzzykmeans.fit(X)
            wr = fuzzykmeans.labels_
            # WSSE = kmeans.inertia_
            # wr = kmeans.labels_
            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = str(','.join(pts[p])) + '\t' + str(wr[p]) + '\n'
                of.write(stri)
            of.close()
            co = 1
            print(fuzzykmeans.cluster_centers_)
            for j in fuzzykmeans.cluster_centers_:
                text = 'Center-' + str(co)
                for d in j:
                    text += '\t' + str(d)
                # print(text)
                text += '\n'
                oc.write(text)
                co += 1
            oc.close()
            messagebox.showinfo('notification', 'Successfully completed')


if __name__ == '__main__':
    if len(sys.argv) == 4:
        obj = fuzzyKmeans(sys.argv[1],sys.argv[2],sys.argv[3])
        obj.run()
    elif len(sys.argv) == 8:
        obj = fuzzyKmeans(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
        obj.run()
    else:
        print('Please enter in one of the following format:'
              '1. python fuzzyKmeans.py <inputFile> <outputFile> <kValue>'
              '2. python fuzzyKmeans.py <inputFile> <outputFile> <kValue> <fuzzy-ness parameter> <max_iter> <random_state> <tol> ')