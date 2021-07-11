from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import startApp
from algorithms.clustering.kmeans import kMeans


class DBScanGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('DBScan')
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

        eps_label=Label(self.root,text='Number of cluster')
        eps_label.grid(column=0,row=2)
        eps_Entry = Entry(self.root,textvariable='')
        eps_Entry.grid(column=1,row=2)

        minSample_label = Label(self.root, text='Number of cluster')
        minSample_label.grid(column=0, row=3)
        minSample_Entry = Entry(self.root, textvariable='')
        minSample_Entry.grid(column=1, row=3)

        leafSize_label=Label(self.root,text='k-means alg run with the different centroid')
        leafSize_label.grid(column=0, row=4)
        leafSize_Entry=Entry(self.root,textvariable='')
        leafSize_Entry.grid(column=1,row=4)

        p_label = Label(self.root, text='centroid initialization:')
        p_label.grid(column=0, row=5)
        p_Entry = Entry(self.root, textvariable='')
        p_Entry.grid(column=1, row=5)

        nJobs_label = Label(self.root, text='The number of OpenMP threads:')
        nJobs_label.grid(column=0, row=6)
        nJobs_Entry = Entry(self.root, textvariable='')
        nJobs_Entry.grid(column=1, row=6)

        alg_label = Label(self.root, text='Enter Max iterations value:')
        alg_label.grid(column=0, row=7)
        algOpt=['auto','ball_tree','kol_tree','brute']
        algVar=StringVar()
        alg_CB=ttk.Combobox(self.root,textvariable=algVar,values=algOpt,state='readonly')
        algVar.set(algOpt[0])
        alg_CB.grid(column=1, row=7)

        submit=Button(self.root,text="submit",command=kMeans.run)
        submit.grid(column=1,row=8)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=8)

        self.root.mainloop()

if __name__ == '__main__':
    DBScanGUI().Main()

