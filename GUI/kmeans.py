from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import main
from algorithms.clustering.kmeans import kMeans


class kmeansGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('k-means')
        v = IntVar(self.root, 1)
        self.root.minsize(600, 400)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("text Files","*.txt")))
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
        fileOpen_B=Button(self.root,text="Browse",command=lambda :iFilename.set(self.openFile()))
        fileOpen_B.grid(column=2,row=0)

        outputDir_label = Label(self.root,text='Select the output directory:')
        outputDir_label.grid(column=0, row=1)
        outputDir_label=Entry(self.root, textvariable=oFilename)
        outputDir_label.grid(column=1, row=1)
        fileOpen_B1=Button(self.root,text="Browse",command=lambda :oFilename.set(self.pathtooutfile()))
        fileOpen_B1.grid(column=2,row=1)

        cluster_label=Label(self.root,text='Number of cluster')
        cluster_label.grid(column=0,row=2)
        cluster_Entry=Entry(self.root,textvariable='')
        cluster_Entry.grid(column=1,row=2)

        init_label = Label(self.root, text='Method for initialization:')
        init_label.grid(column=0, row=3)
        initOpt = ['k-means++','random']
        initVar =StringVar()
        init_CB = ttk.Combobox(self.root,textvariable=initVar,values=initOpt,state='readonly')
        initVar.set(initOpt[0])
        init_CB.grid(column=1, row=3)

        itersval_label=Label(self.root,text='k-means alg run with the different centroid')
        itersval_label.grid(column=0, row=4)
        itersval_Entry=Entry(self.root,textvariable='')
        itersval_Entry.grid(column=1,row=4)

        maxIter_label = Label(self.root, text='Enter Max iterations value:')
        maxIter_label.grid(column=0, row=5)
        maxIter_Entry = Entry(self.root, textvariable='')
        maxIter_Entry.grid(column=1, row=5)

        # precomputeDist_label = Label(self.root, text='Precompute distances:')
        # precomputeDist_label.grid(column=0, row=6)
        # precomputeOpt=['auto','True','False']
        # precomputeVar=StringVar()
        # precomputeDist_CB = ttk.Combobox(self.root,textvariable=precomputeVar,values=precomputeOpt,state='readonly')
        # precomputeVar.set(precomputeOpt[0])
        # precomputeDist_CB.grid(column=1, row=6)

        randomState_label = Label(self.root, text='centroid initialization:')
        randomState_label.grid(column=0, row=7)
        randomState_Entry = Entry(self.root, textvariable='')
        randomState_Entry.grid(column=1, row=7)

        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')
        # nJobs_label.grid(column=0, row=8)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=8)

        alg_label = Label(self.root, text='Enter Max iterations value:')
        alg_label.grid(column=0, row=8)
        algOpt=['auto','full','elkan']
        algVar=StringVar()
        alg_CB=ttk.Combobox(self.root,textvariable=algVar,values=algOpt,state='readonly')
        algVar.set(algOpt[0])
        alg_CB.grid(column=1, row=8)

        submit=Button(self.root,text="submit",command=lambda:kMeans(iFilename.get(),oFilename.get(),cluster_Entry.get()
                                                             ,initVar.get(),itersval_Entry.get(),maxIter_Entry.get()
                                                             ,randomState_Entry.get(),algVar.get()).run())
        submit.grid(column=1,row=9)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=9)

        self.root.mainloop()

if __name__ == '__main__':
    kmeansGUI().Main()


