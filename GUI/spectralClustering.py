from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
import webbrowser
from GUI import GUImain

from algorithms.clustering.spectralClustering import spectralClustering


class spectralGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Spectral Clustering')
        self.root.minsize(600, 400)
        self.clusterVar = StringVar()
        self.clusterVar.set(2)
        self.eigenSolverVar = StringVar()
        self.nInitVar = StringVar()
        self.nInitVar.set(10)
        self.affinityVar = StringVar()
        self.affinityVar.set('nearest_neighbors')
        self.nNeighborsVar = StringVar()
        self.nNeighborsVar.set(10)
        self.assignVar = StringVar()
        self.coef0Var = StringVar()
        self.coef0Var.set(1)
        self.degreeVar = StringVar()
        self.degreeVar.set(2)
        self.gammaVar = StringVar()
        self.gammaVar.set(1.0)
        self.randomStateVar = StringVar()
        self.randomStateVar.set('None')


    def enter_fg(self, event):
        event.widget['fg'] = 'blue'

    def leave_fg(self, event):
        event.widget['fg'] = 'black'

    def callBack(self, url):
        webbrowser.open_new(url)

    def openFile(self):
        filename1 = filedialog.askopenfilename(initialdir="~/Desktop", title="select a file",
                                               filetypes=(("csv", "*.csv"), ("Text", "*.txt"), ('tsv', '*.tsv')))
        return filename1

    def pathtooutfile(self):
        dirName = filedialog.askdirectory(initialdir="~/Desktop")
        return dirName

    def back(self):
        self.root.destroy()
        GUImain.GUImain().rootGUI()

    def Main(self):
        def makeAddOptions(bin):
            if bin.get():
                eigenSolver_label.grid(column=0, row=6)
                eigensolver_CB.grid(column=1, row=6)

                nInit_label.grid(column=0, row=7)
                nInit_Entry.grid(column=1, row=7)

                nNeighbors_label.grid(column=0, row=8)
                nNeighbors_Entry.grid(column=1, row=8)

                coef0_Entry.grid(column=1, row=9)
                coef0_label.grid(column=0, row=9)

                degree_label.grid(column=0, row=10)
                degree_Entry.grid(column=1, row=10)

                gamma_label.grid(column=0, row=11)
                gamma_Entry.grid(column=1, row=11)

            else:
                eigenSolver_label.grid_remove()
                eigensolver_CB.grid_remove()

                nInit_label.grid_remove()
                nInit_Entry.grid_remove()

                nNeighbors_label.grid_remove()
                nNeighbors_Entry.grid_remove()

                coef0_Entry.grid_remove()
                coef0_label.grid_remove()

                degree_label.grid_remove()
                degree_Entry.grid_remove()

                gamma_label.grid_remove()
                gamma_Entry.grid_remove()

        iFilename = StringVar()
        oFilename = StringVar()
        inputFile_Label = Label(self.root, text='Select the input file:')
        inputFile_Label.grid(column=0, row=0)

        inputFile_TB = Entry(self.root, textvariable=iFilename)
        inputFile_TB.grid(column=1, row=0)
        fileOpen_B = Button(self.root, text="Browse", command=lambda: iFilename.set(self.openFile()))
        fileOpen_B.grid(column=2, row=0)

        outputDir_label = Label(self.root, text='Select the output directory:')
        outputDir_label.grid(column=0, row=1)
        outputDir_label = Entry(self.root, textvariable=oFilename)
        outputDir_label.grid(column=1, row=1)
        fileOpen_B1 = Button(self.root, text="Browse", command=lambda: oFilename.set(self.pathtooutfile()))
        fileOpen_B1.grid(column=2, row=1)

        cluster_label = Label(self.root, text='Number of cluster')
        cluster_label.grid(column=0, row=2)
        cluster_Entry = Entry(self.root, textvariable=self.clusterVar)
        cluster_Entry.grid(column=1, row=2)

        randomState_label = Label(self.root, text='random_state')
        randomState_label.grid(column=0, row=3)
        randomState_Entry = Entry(self.root, textvariable=self.randomStateVar)
        randomState_Entry.grid(column=1, row=3)

        affinity_label = Label(self.root, text='affinity')
        affinity_label.grid(column=0, row=4)
        affinity_Entry = Entry(self.root, textvariable=self.affinityVar)
        affinity_Entry.grid(column=1, row=4)

        assign_label = Label(self.root, text='The strategy for assigning labels:')
        assign_label.grid(column=0, row=5)
        assignOpt = ['kmeans', 'discretize']
        assign_CB = ttk.Combobox(self.root, textvariable=self.assignVar, values=assignOpt, state='readonly')
        self.assignVar.set(assignOpt[0])
        assign_CB.grid(column=1, row=5)

        eigenSolver_label = Label(self.root, text='eigen solver:')
        eigenSolverOpt = ['arpack', 'lobpcg', 'amg']
        self.eigenSolverVar.set(eigenSolverOpt[0])
        eigensolver_CB = ttk.Combobox(self.root, textvariable=self.eigenSolverVar, values=eigenSolverOpt,
                                      state='readonly')

        nInit_label = Label(self.root, text='Number of time the k-means alg')
        nInit_Entry = Entry(self.root, textvariable=self.nInitVar)

        nNeighbors_label = Label(self.root, text='Number of neighbors')
        nNeighbors_Entry = Entry(self.root, textvariable=self.nNeighborsVar)

        coef0_label = Label(self.root, text='coefficient')
        coef0_Entry = Entry(self.root, textvariable=self.coef0Var)

        degree_label = Label(self.root, text='centroid initialization:')
        degree_Entry = Entry(self.root, textvariable=self.degreeVar)

        gamma_label = Label(self.root, text='gamma:')
        gamma_Entry = Entry(self.root, textvariable=self.gammaVar)

        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')
        # nJobs_label.grid(column=0, row=10)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=10)

        helpLink = Label(self.root, text="help", fg="black", font=("Arial", 20))
        helpLink.place(relx=0.01, rely=0.9)
        helpLink.bind('<Button-1>',
                      lambda e: self.callBack(
                          'https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html'))
        helpLink.bind('<Enter>', self.enter_fg)
        helpLink.bind('<Leave>', self.leave_fg)

        bin = BooleanVar()
        bin.set(False)
        detailOptions_CHB = ttk.Checkbutton(self.root, text='add options', variable=bin,
                                            command=lambda: makeAddOptions(bin))
        detailOptions_CHB.grid(column=3, row=13)

        submit = Button(self.root, text="submit",
                        command=lambda: spectralClustering(iFilename.get(), oFilename.get(), self.clusterVar.get()
                                                           , self.affinityVar.get(), self.eigenSolverVar.get(),
                                                           self.nInitVar.get(), self.gammaVar.get(),self.randomStateVar.get(),
                                                           self.nNeighborsVar.get(), self.assignVar.get(),self.degreeVar.get(),
                                                           self.coef0Var.get()).run())

        submit.grid(column=1, row=12)
        back = Button(self.root, text="Back", command=self.back)
        back.grid(column=2, row=12)

        self.root.mainloop()


if __name__ == '__main__':
    spectralGUI().Main()
