from tkinter import messagebox
from sklearn.cluster import MeanShift
import numpy as np

class meanShift:
    def __init__(self,inputFile,outputDirectory,bandwidth,seeds,bin_seeding,min_bin_freq,cluster_all,max_iter):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.bandwidth = bandwidth
        self.seeds = seeds
        self.bin_seeding = bin_seeding
        self.min_bin_freq = min_bin_freq
        self.cluster_all = cluster_all
        self.max_iter = max_iter
    def run(self):
        outputfile = self.outputDir + '/result_MeanShift_' + str(self.max_iter) + '.csv'
        otc = self.outputDir + '/centers_MeanShift_' + str(self.max_iter) + '.csv'

        if (self.inputFile == '' or self.outputDir == '' or self.max_iter == ''):
            messagebox.showerror("Error", "Please fill the fields properly")

        else:
            if self.seeds == '':
                self.seeds = None

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
            meanshift = MeanShift(bandwidth=float(self.bandwidth), max_iter=self.max_iter,seeds=None, bin_seeding=bool(self.bin_seeding)
                            ,min_bin_freq=int(self.min_bin_freq),cluster_all=self.cluster_all).fit(X)

            print(meanshift.labels_)
            print(meanshift.cluster_centers_)
            print(meanshift.n_iter_)






            # wr = meanshift.labels_
            # for p in range(len(X)):
            #     # print(p)
            #     # wr=kmeans.predict(p)
            #     stri = pts[p] + ',' + str(wr[p]) + '\n'
            #     of.write(stri)
            # of.close()
            # co = 1
            # for j in meanshift.cluster_centers_:
            #     text = 'Center-' + str(co)
            #     for d in j:
            #         text += ',' + str(d)
            #     # print(text)
            #     text += '\n'
            #     oc.write(text)
            #     co += 1
            # oc.close()