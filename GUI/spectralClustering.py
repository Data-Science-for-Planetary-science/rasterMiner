from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import GUImain

from algorithms.clustering.spectralClustering import spectralClustering


class spectralGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Spectral Clustering')
        v = IntVar(self.root, 1)
        self.root.minsize(600, 400)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("Text","*.txt"),('tsv','*.tsv')))
        return filename1
    def pathtooutfile(self):
        dirName=filedialog.askdirectory(initialdir="~/Desktop")
        return dirName
    def back(self):
        self.root.destroy()
        GUImain.main()
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

        cluster_label=Label(self.root,text='Number of cluster')
        cluster_label.grid(column=0,row=2)
        cluster_Entry = Entry(self.root,textvariable='')
        cluster_Entry.grid(column=1,row=2)

        eigenSolver_label = Label(self.root, text='eigen solver:')
        eigenSolver_label.grid(column=0, row=3)
        eigenSolverOpt = ['arpack','lobpcg','amg']
        eigenSolverVar =StringVar()
        eigensolver_CB = ttk.Combobox(self.root,textvariable=eigenSolverVar,values=eigenSolverOpt,state='readonly')
        eigenSolverVar.set(eigenSolverOpt[0])
        eigensolver_CB.grid(column=1, row=3)

        nInit_label=Label(self.root,text='Number of time the k-means alg')
        nInit_label.grid(column=0, row=4)
        nInit_Entry=Entry(self.root,textvariable='')
        nInit_Entry.grid(column=1,row=4)

        affinity_label = Label(self.root, text='affinity')
        affinity_label.grid(column=0, row=5)
        affinity_Entry = Entry(self.root, textvariable='')
        affinity_Entry.grid(column=1, row=5)

        nNeighbors_label = Label(self.root, text='Number of neighbors')
        nNeighbors_label.grid(column=0, row=6)
        nNeighbors_Entry = Entry(self.root, textvariable='')
        nNeighbors_Entry.grid(column=1, row=6)

        assign_label = Label(self.root, text='The strategy for assigning labels:')
        assign_label.grid(column=0, row=7)
        assignOpt=['kmeans','discretize']
        assignVar=StringVar()
        assign_CB = ttk.Combobox(self.root,textvariable=assignVar,values=assignOpt,state='readonly')
        assign_CB.set(assignOpt[0])
        assign_CB.grid(column=1, row=7)

        randomState_label = Label(self.root, text='random_state')
        randomState_label.grid(column=0, row=8)
        randomState_Entry = Entry(self.root, textvariable='')
        randomState_Entry.grid(column=1, row=8)

        coef0_label = Label(self.root, text='coefficient')
        coef0_label.grid(column=0, row=9)
        coef0_Entry = Entry(self.root, textvariable='')
        coef0_Entry.grid(column=1, row=9)

        degree_label = Label(self.root, text='centroid initialization:')
        degree_label.grid(column=0, row=10)
        degree_Entry = Entry(self.root, textvariable='')
        degree_Entry.grid(column=1, row=10)


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

