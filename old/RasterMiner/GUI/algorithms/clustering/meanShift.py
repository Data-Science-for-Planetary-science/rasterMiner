from tkinter import messagebox
from sklearn.cluster import MeanShift
import numpy as np
import sys

class meanShift:
    def __init__(self,*args):
        if len(args) == 3:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.bandwidth = args[2]
            self.seeds = 'None'
            self.bin_seeding = 'False'
            self.min_bin_freq = 1
            self.cluster_all = 'True'
            self.max_iter = 300
        elif len(args) == 4:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.bandwidth = args[2]
            self.seeds = 'None'
            self.bin_seeding = 'False'
            self.min_bin_freq = 1
            self.cluster_all = 'True'
            self.max_iter = args[3]
        elif len(args) == 8:
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
                    j[r] = j[r].replace('"','')
                    j[r] = float(j[r])
                pts.append(j[0:1])
                data.append(j[1:])
            X = np.array(data,dtype='float64')
            meanshift = MeanShift(bandwidth=self.bandwidth, max_iter=int(self.max_iter),seeds=self.seeds, bin_seeding=bool(self.bin_seeding)
                            ,min_bin_freq=int(self.min_bin_freq),cluster_all=bool(self.cluster_all)).fit(X)

            print(meanshift.n_iter_)

            wr = meanshift.labels_
            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri = str(pts[p]) + ',' + str(wr[p]) + '\n'
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

            messagebox.showinfo('notification','Successfully completed')

if __name__ == '__main__':
    if len(sys.argv) == 4:
        obj = meanShift(sys.argv[1], sys.argv[2], sys.argv[3])
        obj.run()
    elif len(sys.argv) == 5:
        obj = meanShift(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        obj.run()
    elif len(sys.argv) == 15:
        obj = meanShift(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]
                     ,sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14])
        obj.run()
    else:
        print('Please enter in one of the following format:'
              '1. python meanShift.py <inputFile> <outputFile> <band width>'
              '2. python meanShift.py <inputFile> <outputFile> <band width> <maxIter>'
              '3. python meanShift.py <inputFile> <outputFile> <band width> <maxIter> <seeds> <bin seeding> <min bin freq> <cluster all> ')
