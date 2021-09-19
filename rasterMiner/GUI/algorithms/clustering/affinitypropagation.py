from tkinter import *
from tkinter import messagebox
from sklearn.cluster import AffinityPropagation
import numpy as np
from sklearn.preprocessing import StandardScaler


class affinityPropagation:
    def __init__(self, *args):
        if len(args) == 4:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.damping = args[2]
            self.maxIter = args[3]
            self.convergenceIter = 15
            self.preference = None
            self.affinity = 'euclidean'
            self.randomState = 0

        elif len(args) == 8:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.damping = args[2]
            self.maxIter = args[3]
            self.convergenceIter = args[4]
            self.preference = args[5]
            self.affinity = args[6]
            self.randomState = args[7]

    def run(self):
        outputfile = self.outputDir + '/result_AffinityPropagation_' + str(self.damping) + '_' + str(self.maxIter) + '.csv'
        otc = self.outputDir + '/centers_AffinityPropagation_' + str(self.damping) + '_' + str(self.maxIter) + '.csv'
        afMatrixOutput = self.outputDir + '/affinityMatrix' + str(self.damping) + '_' + str(self.maxIter) + '.csv'
        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")

        else:
            if self.randomState == 'None':
                self.randomState = None
            else:
                self.randomState = int(self.randomState)

            if self.preference == 'None':
                self.preference = None
            else:
                self.preference = float(self.preference)


            of = open(outputfile, 'w')
            print(self.inputFile)
            f = open(self.inputFile, 'r')
            oc = open(otc, 'w')
            afmo = open(afMatrixOutput, 'w')
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
            z = np.array(data)
            X = StandardScaler().fit_transform(z)

            clustering = AffinityPropagation(damping=float(self.damping), max_iter=int(self.maxIter), convergence_iter=int(self.convergenceIter),
                                      affinity=self.affinity, preference=self.preference, random_state=self.randomState).fit(X)
            labels = clustering.labels_

            for p in range(len(z)):
                stri = str(','.join(pts[p])) + '\t' + str(labels[p]) + '\n'
                of.write(stri)
            of.close()

            co = 1
            for j in clustering.cluster_centers_:
                text = 'Center-' + str(co)
                for d in j:
                    text += '\t' + str(d)
                # print(text)
                text += '\n'
                oc.write(text)
                co += 1
            oc.close()
            for k in clustering.affinity_matrix_:
                text += '\t' + str(k)
                text += '\n'
                afmo.write(text)

            messagebox.showinfo('notification', 'Successfully completed')

if __name__ == '__main__':
    if len(sys.argv) == 5:
        obj = affinityPropagation(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        obj.run()

    elif len(sys.argv) == 9:
        affinityPropagation(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4],sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8],)