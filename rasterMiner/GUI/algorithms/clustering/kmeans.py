from tkinter import messagebox
from sklearn.cluster import KMeans
import numpy as np
import sys
import csv

class kMeans:
    def __init__(self, *args):
        if len(args) == 3:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.init = 'random'
            self.n_init = 10
            self.max_iter = 300
            #cls.precompute_dist = precompute_dist
            self.random_state = 'None'
            self.alg = 'auto'
        elif len(args) == 4:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.init = args[3]
            self.n_init = 10
            self.max_iter = 300
            self.random_state = 'None'
            self.alg = 'auto'
        elif len(args) == 8:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.init = args[3]
            self.n_init = args[4]
            self.max_iter = args[5]
            # self.precompute_dist = precompute_dist
            self.random_state = args[6]
            self.alg = args[7]
        else:
            print('Error message print')


    def run(self):
        outputfile = self.outputDir + '/result_K-means_' + str(self.k) + '_' + str(self.max_iter) + '.csv'
        otc = self.outputDir + '/centers_K-means_' + str(self.k) + '_' + str(self.max_iter) + '.csv'

        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")

        else:
            if self.random_state == 'None':
                self.random_state = None
            else:
                self.random_state = int(self.random_state)
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

            X = np.array(data)
            kmeans = KMeans(n_clusters=int(self.k), init=self.init, max_iter=int(self.max_iter)
                            ,n_init=int(self.n_init),random_state=self.random_state,algorithm=self.alg).fit(X)
            WSSE = kmeans.inertia_
            wr = kmeans.labels_
            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = str(','.join(pts[p])) + '\t' + str(wr[p]) + '\n'
                of.write(stri)
            of.close()
            co = 1
            for j in kmeans.cluster_centers_:
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
        obj = kMeans(sys.argv[1],sys.argv[2],sys.argv[3])
        obj.run()
    elif len(sys.argv) == 5:
        obj = kMeans(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
        obj.run()
    elif len(sys.argv) == 8:
        obj = kMeans(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
        obj.run()
    else:
        print('Please enter in one of the following format:'
              '1. python kmeans.py <inputFile> <outputFile> <kValue>'
              '2. python kmeans.py <inputFile> <outputFile> <kValue> <initialize>'
              '3. python kmeans.py <inputFile> <outputFile> <kValue> <initialize method> <number of initialize> <max_iter> <random_state> <algorithm> ')