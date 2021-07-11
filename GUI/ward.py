from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import startApp
from algorithms.clustering.ward import


class wardGUI:
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
        startApp.main()
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

        memory_label=Label(self.root,text='memory')
        memory_label.grid(column=0, row=3)
        memory_Entry=Entry(self.root,textvariable='')
        memory_Entry.grid(column=1,row=3)

        nComponent_label = Label(self.root, text='The Number of connection of the tree')
        nComponent_label.grid(column=0, row=4)
        nComponent_Entry = Entry(self.root, textvariable='')
        nComponent_Entry.grid(column=1, row=4)

        computeFullTree_label = Label(self.root, text='random_state')
        computeFullTree_label.grid(column=0, row=5)
        computeFullTree_Entry = Entry(self.root, textvariable='')
        computeFullTree_Entry.grid(column=1, row=5)


        submit=Button(self.root,text="submit",command=lambda :(iFilename.get(),oFilename.get(),cluster_Entry.get()
                                                                        ,eigenSolverVar.get(),nInit_Entry.get(),randomState_Entry.get(),
                                                                         gamma_Entry.get(),nNeighbors_Entry.get(),assignVar.get(),
                                                                         degree_Entry.get(),coef0_Entry.get(),affinity_Entry.get()).run())

        submit.grid(column=1,row=6)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=6)

        self.root.mainloop()

if __name__ == '__main__':
    wardGUI().Main()