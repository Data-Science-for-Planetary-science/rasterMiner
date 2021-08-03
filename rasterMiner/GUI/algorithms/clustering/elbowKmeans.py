from tkinter import *
from tkinter import messagebox
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sklearn.cluster import KMeans
import numpy as np
import mplcursors
import tkinter as tk


class elbowKmeans:
    def __init__(self,*args):
        if len(args) == 6:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.init = 'random'
            self.n_init = 10
            self.max_iter = 300
            #cls.precompute_dist = precompute_dist
            self.random_state = None
            self.alg = 'auto'
            self.mink = args[3]
            self.maxk = args[4]
            self.inc = args[5]
        elif len(args) == 7:
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.init = args[3]
            self.n_init = 10
            self.max_iter = 300
            self.random_state = None
            self.alg = 'auto'
            self.mink = args[4]
            self.maxk = args[5]
            self.inc = args[6]
        elif len(args) == 11:
            print(args)
            self.inputFile = args[0]
            self.outputDir = args[1]
            self.k = args[2]
            self.init = args[3]
            self.n_init = args[4]
            self.max_iter = args[5]
            # self.precompute_dist = precompute_dist
            self.random_state = args[6]
            self.alg = args[7]
            self.mink = args[8]
            self.maxk = args[9]
            self.inc = args[10]
        else:
            print('Error message print')
    def run(self):
        outputfile = self.outputDir + '/result_K-means_' + str(self.k) + '_' + str(self.max_iter) + '.csv'

        if (self.inputFile == '' or self.outputDir == ''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            if self.random_state == 'None':
                self.random_state = None
            else:
                self.random_state = int(self.random_state)
            of = open(outputfile, 'w')
            f = open(self.inputFile, 'r')
            data = []
            pts = []
            header = f.readline()
            for i in f:
                j = i.strip('\n').split('\t')
                for r in range(2, len(j)):
                    j[r] = float(j[r])
                pts.append(j[0:1])
                data.append(j[1:])
            X = np.array(data)
            gx=[]
            gy=[]
            # g2y=[]
            for i in range(int(self.mink), int(self.maxk) + 1, int(self.inc)):
                kmeans = KMeans(n_clusters=int(self.k), init=self.init, max_iter=int(self.max_iter)
                                , n_init=int(self.n_init), random_state=self.random_state, algorithm=self.alg).fit(X)
                gy.append(kmeans.inertia_)
                gx.append(i)
                stri = str(i) + '\t' + str(kmeans.inertia_) + '\n'
                of.write(stri)
            messagebox.showinfo('notification', 'Successfully completed')

            of.close()
            root=tk.Tk()
            root.title('elbow k-means')
            f=Figure(figsize=(5,5),dpi=100)
            a=f.add_subplot(111,facecolor='white')
            a.set_title('Elbow KMeans')
            a.set_xlabel('k value')
            a.set_ylabel('WSSE')
            a.set_xticks(gx)
            a.plot(gx,gy, marker='o',color='k')
            canvas=FigureCanvasTkAgg(f,root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=True)
            toolbar=NavigationToolbar2Tk(canvas,root)
            mplcursors.cursor(a).connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
            canvas._tkcanvas.pack(side=TOP,fill=BOTH,expand=True)
            root.mainloop()