from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import GUImain
from algorithms.clustering.birch import BIRCH
import webbrowser

class birchGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('birch')
        self.root.minsize(600, 400)
        self.threshholdVar = StringVar()
        self.threshholdVar.set(0.5)
        self.computeLabelsVar = StringVar()
        self.nClusterVar = StringVar()
        self.nClusterVar.set(3)
        self.brunchingVar = StringVar()
        self.brunchingVar.set(50)
    def enter_fg(self,event):
        event.widget['fg'] = 'blue'
    def leave_fg(self,event):
        event.widget['fg'] = 'black'
    def callBack(self,url):
        webbrowser.open_new(url)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("txt","*.txt"),("tsv","*.tsv")))
        return filename1
    def pathtooutfile(self):
        dirName=filedialog.askdirectory(initialdir="~/Desktop")
        return dirName
    def back(self):
        self.root.destroy()
        GUImain.GUImain()
    def Main(self):
        def makeAddOptions(bin):
            if bin.get():
                brunchingFactor_label.grid(column=0, row=3)
                brunchingFactor_Entry.grid(column=1, row=3)

                computeLabels_label.grid(column=0, row=4)
                computeLabels_CB.grid(column=1, row=4)

                nCluster_label.grid(column=0, row=5)
                nCluster_Entry.grid(column=1, row=5)




            else:
                computeLabels_label.grid_remove()
                computeLabels_CB.grid_remove()

                nCluster_label.grid_remove()
                nCluster_Entry.grid_remove()

                brunchingFactor_Entry.grid_remove()
                brunchingFactor_label.grid_remove()

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
        threshhold_Entry = Entry(self.root,textvariable=self.threshholdVar)
        threshhold_Entry.grid(column=1,row=2)

        brunchingFactor_label = Label(self.root, text='BranchingFactor')
        brunchingFactor_Entry = Entry(self.root, textvariable=self.brunchingVar)

        computeLabels_label = Label(self.root, text='Compute Labels:')
        computeLabelsOpt = ['True','False']
        computeLabels_CB = ttk.Combobox(self.root,textvariable=self.computeLabelsVar,values=computeLabelsOpt,state='readonly')
        self.computeLabelsVar.set(computeLabelsOpt[0])

        nCluster_label=Label(self.root,text='Number of cluster')
        nCluster_Entry=Entry(self.root,textvariable=self.nClusterVar)

        helpLink = Label(self.root, text="help", fg="black",font=("Arial", 20))
        helpLink.place(relx=0.01,rely=0.9)
        helpLink.bind('<Button-1>',
                        lambda e: self.callBack('https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html'))
        helpLink.bind('<Enter>',self.enter_fg)
        helpLink.bind('<Leave>',self.leave_fg)

        bin = BooleanVar()
        bin.set(False)
        detailOptions_CHB = ttk.Checkbutton(self.root, text='add options',variable=bin,command=lambda :makeAddOptions(bin))
        detailOptions_CHB.grid(column=3,row=5)



        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')


        # nJobs_label.grid(column=0, row=10)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=10)

        submit=Button(self.root,text="submit",command=lambda :BIRCH(iFilename.get(),oFilename.get(),self.threshholdVar.get()
                                                                        ,self.brunchingVar.get(),self.computeLabelsVar.get(),
                                                                        self.nClusterVar.get()).run())

        submit.grid(column=1,row=5)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=5)

        self.root.mainloop()

if __name__ == '__main__':
    birchGUI.Main(j)
