from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import main
from algorithms.clustering.spectralClustering import spectralClustering


class opticsGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Spectral Clustering')
        v = IntVar(self.root, 1)
        self.root.minsize(600, 400)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("All Files","*.txt")))
        return filename1
    def pathtooutfile(self):
        dirName=filedialog.askdirectory(initialdir="~/Desktop")
        return dirName
    def back(self):
        self.root.destroy()
        main.main()
    def Main(self):
        iFilename = StringVar()
        oFilename = StringVar()
        inputFile_Label=Label(self.root,text='Select the input file:')
        inputFile_Label.grid(column=0, row=0)

        inputFile_TB=Entry(self.root,textvariable=iFilename)
        inputFile_TB.grid(column=1,row=0)
        fileOpen_B=Button(self.root,text="Browse",command=lambda:iFilename.set(self.openFile()))
        fileOpen_B.grid(column=2,row=0)

        outputDir_label = Label(self.root,text='Select the output directory:')
        outputDir_label.grid(column=0, row=1)
        outputDir_label=Entry(self.root, textvariable=oFilename)
        outputDir_label.grid(column=1, row=1)
        fileOpen_B1=Button(self.root,text="Browse",command=lambda:oFilename.set(self.pathtooutfile()))
        fileOpen_B1.grid(column=2,row=1)

        minSamples_label=Label(self.root,text='Number of cluster')
        minSamples_label.grid(column=0,row=2)
        minSamples_Entry = Entry(self.root,textvariable='')
        minSamples_Entry.grid(column=1,row=2)

        maxEps_label=Label(self.root,text='Number of time the k-means alg')
        maxEps_label.grid(column=0, row=4)
        maxEps_Entry=Entry(self.root,textvariable='')
        maxEps_Entry.grid(column=1,row=4)

        p_label = Label(self.root, text='affinity')
        p_label.grid(column=0, row=5)
        p_Entry = Entry(self.root, textvariable='')
        p_Entry.grid(column=1, row=5)

        metric_label = Label(self.root, text='Number of neighbors')
        metric_label.grid(column=0, row=6)
        metric_Entry = Entry(self.root, textvariable='')
        metric_Entry.grid(column=1, row=6)

        clusterMethod_label = Label(self.root, text='random_state')
        clusterMethod_label.grid(column=0, row=8)
        clusterMethod_Entry = Entry(self.root, textvariable='')
        clusterMethod_Entry.grid(column=1, row=8)

        metricParams_label = Label(self.root, text='coefficient')
        metricParams_label.grid(column=0, row=9)
        metricParams_Entry = Entry(self.root, textvariable='')
        metricParams_Entry.grid(column=1, row=9)

        minClusterSize_label = Label(self.root, text='centroid initialization:')
        minClusterSize_label.grid(column=0, row=10)
        minClusterSize_Entry = Entry(self.root, textvariable='')
        minClusterSize_Entry.grid(column=1, row=10)

        leafSize_label = Label(self.root, text='centroid initialization:')
        leafSize_label.grid(column=0, row=10)
        leafSize_Entry = Entry(self.root, textvariable='')
        leafSize_Entry.grid(column=1, row=10)

        preCorrection_label = Label(self.root, text='eigen solver:')
        preCorrection_label.grid(column=0, row=3)
        preCorrectionOpt = ['True','False']
        preCorrectionVar =StringVar()
        preCorrection_CB = ttk.Combobox(self.root,textvariable=preCorrectionVar,values=preCorrectionOpt,state='readonly')
        preCorrectionVar.set(preCorrectionOpt[0])
        preCorrection_CB.grid(column=1, row=3)


        alg_label = Label(self.root, text='The strategy for assigning labels:')
        alg_label.grid(column=0, row=7)
        algOpt=['auto','ball_tree','kd_tree','brute']
        algVar=StringVar()
        alg_CB = ttk.Combobox(self.root,textvariable=algVar,values=algOpt,state='readonly')
        alg_CB.set(algOpt[0])
        alg_CB.grid(column=1, row=7)








        gamma_label = Label(self.root, text='gamma:')
        gamma_label.grid(column=0,row=11)
        gamma_Entry = Entry(self.root,textvariable='')
        gamma_Entry.grid(column=1,row=11)




        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')


        # nJobs_label.grid(column=0, row=10)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=10)

        submit=Button(self.root,text="submit",command=lambda :spectralClustering(iFilename.get(),oFilename.get(),cluster_Entry.get()
                                                                        ,eigenSolverVar.get(),nInit_Entry.get(),randomState_Entry.get(),
                                                                         gamma_Entry.get(),nNeighbors_Entry.get(),assignVar.get(),
                                                                         degree_Entry.get(),coef0_Entry.get(),affinity_Entry.get()).run())

        submit.grid(column=1,row=12)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=12)

        self.root.mainloop()

if __name__ == '__main__':
    spectralGUI().Main()