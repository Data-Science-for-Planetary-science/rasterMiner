from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import startApp
from algorithms.clustering.meanShift import meanShift


class meanShiftGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('meanShift')
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

        bandwidth_label=Label(self.root,text='band width')
        bandwidth_label.grid(column=0,row=2)
        bandwidth_Entry = Entry(self.root,textvariable='')
        bandwidth_Entry.grid(column=1,row=2)

        maxIter_label = Label(self.root, text='Enter Max iterations value:')
        maxIter_label.grid(column=0, row=3)
        maxIter_Entry = Entry(self.root, textvariable='')
        maxIter_Entry.grid(column=1, row=3)

        clusterAll_label = Label(self.root, text='Cluster All')
        clusterAll_label.grid(column=0, row=4)
        clusterAll_Entry = Entry(self.root, textvariable='')
        clusterAll_Entry.grid(column=1, row=4)

        minBinFreq_label = Label(self.root, text='To speed up algorithm')
        minBinFreq_label.grid(column=0, row=5)
        minBinFreq_Entry = Entry(self.root, textvariable='')
        minBinFreq_Entry.grid(column=1, row=5)

        binSeeding_label = Label(self.root, text='aaaaa')
        binSeeding_label.grid(column=0, row=6)
        binSeeding_Entry = Entry(self.root, textvariable='')
        binSeeding_Entry.grid(column=1, row=6)

        seeds_label = Label(self.root, text='Seeds')
        seeds_label.grid(column=0, row=7)
        seeds_Entry = Entry(self.root, textvariable='')
        seeds_Entry.grid(column=1, row=7)

        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')
        # nJobs_label.grid(column=0, row=8)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=8)

        submit=Button(self.root,text="submit",command=lambda :meanShift(iFilename.get(),oFilename.get(),bandwidth_Entry.get()
                                                                        ,seeds_Entry.get(),binSeeding_Entry.get()
                                                                        ,minBinFreq_Entry.get(),clusterAll_Entry.get()
                                                                        ,maxIter_Entry.get()).run())
        submit.grid(column=1,row=8)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=8)

        self.root.mainloop()

if __name__ == '__main__':
    meanShiftGUI().Main()

