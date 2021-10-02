from tkinter import *
from tkinter import filedialog, Label
import webbrowser
from tkinter import ttk
from algorithms.clustering.meanShift import meanShift
import rasterMiner
import GUImain

class meanShiftGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('meanShift')
        self.root.minsize(600, 400)
        self.bandWidthVar = StringVar()
        self.bandWidthVar.set('None')
        self.maxIterVar = StringVar()
        self.maxIterVar.set(300)
        self.clusterAllVar = StringVar()
        self.clusterAllVar.set('True')
        self.minBinFreqVar = StringVar()
        self.minBinFreqVar.set(1)
        self.binSeedingVar = StringVar()
        self.binSeedingVar.set('False')
        self.seedsVar = StringVar()
        self.seedsVar.set('None')





    def enter_fg(self,event):
        event.widget['fg'] = 'blue'
    def leave_fg(self,event):
        event.widget['fg'] = 'black'
    def callBack(self,url):
        webbrowser.open_new(url)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("txt","*.txt"),('tsv','*tsv')))
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
                clusterAll_label.grid(column=0, row=4)
                clusterAll_Entry.grid(column=1, row=4)

                minBinFreq_Entry.grid(column=1, row=5)
                minBinFreq_label.grid(column=0, row=5)

                binSeeding_label.grid(column=0, row=6)
                binSeeding_Entry.grid(column=1, row=6)

                seeds_label.grid(column=0, row=7)
                seeds_Entry.grid(column=1, row=7)


            else:
                clusterAll_label.grid_remove()
                clusterAll_Entry.grid_remove()

                minBinFreq_Entry.grid_remove()
                minBinFreq_label.grid_remove()

                binSeeding_Entry.grid_remove()
                binSeeding_label.grid_remove()

                seeds_label.grid_remove()
                seeds_Entry.grid_remove()


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
        bandwidth_Entry = Entry(self.root,textvariable=self.bandWidthVar)
        bandwidth_Entry.grid(column=1,row=2)

        maxIter_label = Label(self.root, text='Enter Max iterations value:')
        maxIter_label.grid(column=0, row=3)
        maxIter_Entry = Entry(self.root, textvariable=self.maxIterVar)
        maxIter_Entry.grid(column=1, row=3)

        clusterAll_label = Label(self.root, text='Cluster All')
        clusterAll_Entry = Entry(self.root, textvariable=self.clusterAllVar)

        minBinFreq_label = Label(self.root, text='To speed up algorithm')
        minBinFreq_Entry = Entry(self.root, textvariable=self.minBinFreqVar)

        binSeeding_label = Label(self.root, text='binSeeding')
        binSeeding_Entry = Entry(self.root, textvariable=self.binSeedingVar)

        seeds_label = Label(self.root, text='Seeds')
        seeds_Entry = Entry(self.root, textvariable=self.seedsVar)

        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')
        # nJobs_label.grid(column=0, row=8)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=8)

        submit=Button(self.root,text="submit",command=lambda :meanShift(iFilename.get(),oFilename.get(),self.bandWidthVar.get()
                                                                        ,self.seedsVar.get(),self.binSeedingVar.get()
                                                                        ,self.minBinFreqVar.get(),self.clusterAllVar.get()
                                                                        ,self.maxIterVar.get()).run())

        helpLink = Label(self.root, text="help", fg="black",font=("Arial", 20))
        helpLink.place(relx=0.01,rely=0.9)
        helpLink.bind('<Button-1>',
                        lambda e: self.callBack('https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html'))
        helpLink.bind('<Enter>',self.enter_fg)
        helpLink.bind('<Leave>',self.leave_fg)

        bin = BooleanVar()
        bin.set(False)
        detailOptions_CHB = ttk.Checkbutton(self.root, text='add options',variable=bin,command=lambda :makeAddOptions(bin))
        detailOptions_CHB.grid(column=0,row=14)

        submit.grid(column=1,row=8)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=8)
        self.root.mainloop()

if __name__ == '__main__':
    meanShiftGUI().Main()

