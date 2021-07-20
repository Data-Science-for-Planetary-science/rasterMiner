from tkinter import *
from tkinter import messagebox
from sklearn.cluster import AffinityPropagation
import numpy as np
from sklearn.preprocessing import StandardScaler


class affinityPropagation:
    def __init__(self, inputFile, outputDirectory, damping, maxIter, convergenceIter, preference, affinity, randomState):
        self.inputFile = inputFile
        self.outputDir = outputDirectory
        self.damping = damping
        self.maxIter = maxIter
        self.convergenceIter = convergenceIter
        self.preference = preference
        self.affinity = affinity
        self.randomState = randomState
    def run(self):
        outputfile = self.outputDir + '/result_AffinityPropagation_' + str(self.damping) + '_' + str(self.maxIter) + '.csv'
        otc = self.outputDir + '/centers_AffinityPropagation_' + str(self.damping) + '_' + str(self.maxIter) + '.csv'
        afMatrixOutput = '/affinityMatrix' + str(self.damping) + '_' + str(self.maxIter) + '.csv'
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
