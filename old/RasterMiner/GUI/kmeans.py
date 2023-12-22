from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
from algorithms.clustering.kmeans import kMeans
import rasterMiner
import webbrowser


class kmeansGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('k-means')
        self.root.minsize(600, 400)
        self.initVar = StringVar()
        self.algVar = StringVar()
        self.iFilename = StringVar()
        self.oFilename = StringVar()
        self.clusterVar = StringVar()
        self.clusterVar.set(8)
        self.randomStateVar = StringVar()
        self.randomStateVar.set(None)
        self.iterVar = StringVar()
        self.iterVar.set(10)
        self.maxIterVar = StringVar()
        self.maxIterVar.set(300)
    def enter_fg(self,event):
        event.widget['fg'] = 'blue'
    def leave_fg(self,event):
        event.widget['fg'] = 'black'
    def callBack(self,url):
        webbrowser.open_new(url)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),
                                                                                                     ("text Files","*.txt"),
                                                                                                     ('tsv file','*.tsv')))
        return filename1
    def pathtooutfile(self):
        dirName=filedialog.askdirectory(initialdir="~/Desktop")
        return dirName
    def back(self):
        self.root.destroy()
        rasterMiner.GUImain().rootGUI()

    def Main(self):
        def makeAddOptions(bin):
            if bin.get():
                init_label.grid(column=0, row=4)
                init_CB.grid(column=1, row=4)

                itersval_label.grid(column=0, row=5)
                itersval_Entry.grid(column=1, row=5)

                maxIter_label.grid(column=0, row=6)
                maxIter_Entry.grid(column=1, row=6)

                alg_label.grid(column=0, row=7)
                alg_CB.grid(column=1, row=7)
            else:
                init_label.grid_remove()
                init_CB.grid_remove()

                itersval_Entry.grid_remove()
                itersval_label.grid_remove()

                maxIter_Entry.grid_remove()
                maxIter_label.grid_remove()

                alg_CB.grid_remove()
                alg_label.grid_remove()

        inputFile_Label = Label(self.root, text='Select the input file:')
        inputFile_Label.grid(column=0, row=0)

        inputFile_TB = Entry(self.root, textvariable=self.iFilename)
        inputFile_TB.grid(column=1, row=0)
        fileOpen_B = Button(self.root, text="Browse", command=lambda: self.iFilename.set(self.openFile()))
        fileOpen_B.grid(column=2, row=0)

        outputDir_label = Label(self.root, text='Select the output directory:')
        outputDir_label.grid(column=0, row=1)
        outputDir_label = Entry(self.root, textvariable=self.oFilename)
        outputDir_label.grid(column=1, row=1)
        fileOpen_B1 = Button(self.root, text="Browse", command=lambda: self.oFilename.set(self.pathtooutfile()))
        fileOpen_B1.grid(column=2, row=1)

        cluster_label = Label(self.root, text='Number of cluster')
        cluster_label.grid(column=0, row=2)
        cluster_Entry = Entry(self.root, textvariable=self.clusterVar)
        cluster_Entry.grid(column=1, row=2)

        randomState_label = Label(self.root, text='random state:')
        randomState_label.grid(column=0, row=3)
        randomState_Entry = Entry(self.root, textvariable=self.randomStateVar)
        randomState_Entry.grid(column=1, row=3)

        init_label = Label(self.root, text='Method for initialization:')
        initOpt = ['k-means++', 'random']
        init_CB = ttk.Combobox(self.root, textvariable=self.initVar, values=initOpt, state='readonly')
        self.initVar.set(initOpt[0])

        itersval_label = Label(self.root, text='n_init')
        itersval_Entry = Entry(self.root, textvariable=self.iterVar)

        maxIter_label = Label(self.root, text='Enter Max iterations value:')
        maxIter_Entry = Entry(self.root, textvariable=self.maxIterVar)

        alg_label = Label(self.root, text='Enter Max iterations value:')
        algOpt = ['auto', 'full', 'elkan']

        alg_CB = ttk.Combobox(self.root, textvariable=self.algVar, values=algOpt, state='readonly')
        self.algVar.set(algOpt[0])

        helpLink = Label(self.root, text="help", fg="black",font=("Arial", 20))
        helpLink.place(relx=0.01,rely=0.9)
        helpLink.bind('<Button-1>',
                        lambda e: self.callBack('https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html'))
        helpLink.bind('<Enter>',self.enter_fg)
        helpLink.bind('<Leave>',self.leave_fg)

        bin = BooleanVar()
        bin.set(False)
        detailOptions_CHB = ttk.Checkbutton(self.root, text='more options',variable=bin,command=lambda :makeAddOptions(bin))
        detailOptions_CHB.grid(column=0,row=8)


        # precomputeDist_label = Label(self.root, text='Precompute distances:')
        # precomputeDist_label.grid(column=0, row=6)
        # precomputeOpt=['auto','True','False']
        # precomputeVar=StringVar()
        # precomputeDist_CB = ttk.Combobox(self.root,textvariable=precomputeVar,values=precomputeOpt,state='readonly')
        # precomputeVar.set(precomputeOpt[0])
        # precomputeDist_CB.grid(column=1, row=6)



        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')
        # nJobs_label.grid(column=0, row=8)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=8)


        submit=Button(self.root,text="submit",command=lambda:kMeans(self.iFilename.get(),self.oFilename.get(),self.clusterVar.get()
                                                             ,self.initVar.get(),self.iterVar.get(),self.maxIterVar.get()
                                                             ,self.randomStateVar.get(),self.algVar.get()).run())
        submit.grid(column=1,row=8)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=8)


        self.root.mainloop()

if __name__ == '__main__':
    kmeansGUI().Main()


