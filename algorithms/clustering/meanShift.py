from tkinter import messagebox
from sklearn.cluster import MeanShift
import numpy as np

class meanShift:
    def __init__(self,*args):
        if len(args) == 8:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.bandwidth = args[2]
            self.seeds = args[3]
            self.bin_seeding = args[4]
            self.min_bin_freq = args[5]
            self.cluster_all = args[6]
            self.max_iter = args[7]
    def run(self):
        outputfile = self.outputDir + '/result_MeanShift_' + str(self.max_iter) + '.csv'
        otc = self.outputDir + '/centers_MeanShift_' + str(self.max_iter) + '.csv'

        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")

        else:
            if self.seeds == 'None':
                self.seeds = None
            else:
                self.seeds = list(self.seeds)

            if self.bandwidth == 'None':
                self.bandwidth = None
            else:
                self.bandwidth = float(self.bandwidth)
            of = open(outputfile, 'w')
            print(self.inputFile)
            f = open(self.inputFile, 'r')
            oc = open(otc, 'w')
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
            meanshift = MeanShift(bandwidth=self.bandwidth, max_iter=self.max_iter,seeds=self.seeds, bin_seeding=bool(self.bin_seeding)
                            ,min_bin_freq=int(self.min_bin_freq),cluster_all=bool(self.cluster_all)).fit(X)

            print(meanshift.n_iter_)

            wr = meanshift.labels_
            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = pts[p] + ',' + str(wr[p]) + '\n'
                of.write(stri)
            of.close()
            co = 1
            for j in meanshift.cluster_centers_:
                text = 'Center-' + str(co)
                for d in j:
                    text += '\t' + str(d)
                # print(text)
                text += '\n'
                oc.write(text)
                co += 1
            oc.close()