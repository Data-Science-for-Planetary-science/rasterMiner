from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
import webbrowser

# import re
# import ast
# import final_code
from GUI import GUImain
from algorithms.clustering.affinitypropagation import affinityPropagation

class affinityPropagationGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('affinity propagation')
        self.root.minsize(600, 400)
        self.dampingVar = StringVar()
        self.dampingVar.set(0.5)
        self.convergenceIterVar = StringVar()
        self.convergenceIterVar.set(3)
        self.maxIterVar = StringVar()
        self.maxIterVar.set(200)
        self.affinityVar = StringVar()
        self.randomStateVar = StringVar()
        self.randomStateVar.set(0)
        self.preferenceVar = StringVar()
        self.preferenceVar.set(50)
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
                preference_label.grid(column=0, row=4)
                preference_Entry.grid(column=1, row=4)

                affinity_label.grid(column=0, row=5)
                affinity_CB.grid(column=1, row=5)

                randomState_label.grid(column=0, row=6)
                randomState_Entry.grid(column=1, row=6)

            else:
                affinity_label.grid_remove()
                affinity_CB.grid_remove()

                preference_label.grid_remove()
                preference_Entry.grid_remove()

                randomState_label.grid_remove()
                randomState_Entry.grid_remove()

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

        damping_label=Label(self.root,text='damping')
        damping_label.grid(column=0, row=2)
        damping_Entry = Entry(self.root, textvariable=self.dampingVar)
        damping_Entry.grid(column=1, row=2)
        
        
        maxIter_label = Label(self.root,text='maxIter')
        maxIter_Entry = Entry(self.root,textvariable=self.maxIterVar)
        maxIter_label.grid(column=0, row=3)
        maxIter_Entry.grid(column=1,row=3)
        
        preference_label = Label(self.root, text='preference')
        preference_Entry = Entry(self.root, textvariable=self.preferenceVar)

        affinity_label = Label(self.root, text='affinity:')
        affinityOpt = ['euclidean','precomputed']
        affinity_CB = ttk.Combobox(self.root,textvariable=self.affinityVar,values=affinityOpt,state='readonly')
        self.affinityVar.set(affinityOpt[0])

        randomState_label=Label(self.root,text='random state')
        randomState_Entry=Entry(self.root, textvariable=self.randomStateVar)

        helpLink = Label(self.root, text="help", fg="black",font=("Arial", 20))
        helpLink.place(relx=0.01,rely=0.9)
        helpLink.bind('<Button-1>',
                        lambda e: self.callBack('https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html'))
        helpLink.bind('<Enter>',self.enter_fg)
        helpLink.bind('<Leave>',self.leave_fg)

        bin = BooleanVar()
        bin.set(False)
        detailOptions_CHB = ttk.Checkbutton(self.root, text='add options',variable=bin,command=lambda :makeAddOptions(bin))
        detailOptions_CHB.grid(column=6,row=7)



        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')


        # nJobs_label.grid(column=0, row=10)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=10)

        submit=Button(self.root, text="submit", command=lambda :affinityPropagation(iFilename.get(), oFilename.get(), self.dampingVar.get()
                                                                      , self.maxIterVar.get(), self.convergenceIterVar.get(),
                                                                      self.preferenceVar.get(), self.affinityVar.get(),self.randomStateVar.get()).run())

        submit.grid(column=1,row=7)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=7)

        self.root.mainloop()

if __name__ == '__main__':
    affinityPropagationGUI().Main()