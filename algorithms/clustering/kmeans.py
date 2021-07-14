from tkinter import messagebox
from sklearn.cluster import KMeans
import numpy as np


class kMeans:
    def __init__(self,inputFile,outputDirectory,k,init,n_init,max_iter,random_state,alg):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.k = k
        self.init = init
        self.n_init = n_init
        self.max_iter = max_iter
        # self.precompute_dist = precompute_dist
        self.random_state = random_state
        self.alg = alg

    def run(self):
        outputfile = self.outputDir + '/result_K-means_' + str(self.k) + '_' + str(self.max_iter) + '.csv'
        otc = self.outputDir + '/centers_K-means_' + str(self.k) + '_' + str(self.max_iter) + '.csv'

        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")

        else:
            if self.random_state == '':
                self.random_state = None
            else:
                self.max_iter = int(self.max_iter)
            of = open(outputfile, 'w')
            print(self.inputFile)
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
            print(X)
            kmeans = KMeans(n_clusters=int(self.k), init=self.init, max_iter=self.max_iter
                            ,n_init=int(self.n_init),random_state=self.random_state,algorithm=self.alg).fit(X)
            WSSE = kmeans.inertia_
            wr = kmeans.labels_
            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = pts[p] + ',' + str(wr[p]) + '\n'
                of.write(stri)
            of.close()
            co = 1
            for j in kmeans.cluster_centers_:
                text = 'Center-' + str(co)
                for d in j:
                    text += ',' + str(d)
                # print(text)
                text += '\n'
                oc.write(text)
                co += 1
            oc.close()

