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
        self.root.title('')
        self.root.minsize(600, 400)

    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("All Files","*.txt")))
        return filename1
    def pathtooutfile(self):
        dirName=filedialog.askdirectory(initialdir="~/Desktop")
        return dirName
    def back(self):
        self.root.destroy()
        GUImain.GUImain()
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

        threshhold_label=Label(self.root,text='Threshold')
        threshhold_label.grid(column=0,row=2)
        threshhold_Entry = Entry(self.root,textvariable='')
        threshhold_Entry.grid(column=1,row=2)

        computeLabels_label = Label(self.root, text='Compute Labels:')
        computeLabels_label.grid(column=0, row=3)
        computeLabelsOpt = ['True','False']
        computeLabelsVar =StringVar()
        computeLabels_CB = ttk.Combobox(self.root,textvariable=computeLabelsVar,values=computeLabelsOpt,state='readonly')
        computeLabelsVar.set(computeLabelsOpt[0])
        computeLabels_CB.grid(column=1, row=3)

        nCluster_label=Label(self.root,text='Number of cluster')
        nCluster_label.grid(column=0, row=4)
        nCluster_Entry=Entry(self.root,textvariable='')
        nCluster_Entry.grid(column=1,row=4)


        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')


        # nJobs_label.grid(column=0, row=10)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=10)

        submit=Button(self.root,text="submit",command=lambda :BIRCH(iFilename.get(),oFilename.get(),cluster_Entry.get()
                                                                        ,eigenSolverVar.get(),nInit_Entry.get(),randomState_Entry.get(),
                                                                         gamma_Entry.get(),nNeighbors_Entry.get(),assignVar.get(),
                                                                         degree_Entry.get(),coef0_Entry.get(),affinity_Entry.get()).run())

        submit.grid(column=1,row=5)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=5)

        self.root.mainloop()

if __name__ == '__main__':
    spectralGUI().Main()