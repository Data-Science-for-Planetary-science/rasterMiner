from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
from GUI import GUImain
from algorithms.clustering.optics import optics
import webbrowser

class opticsGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('OPTICS')
        self.root.minsize(600, 400)
        self.minSamplesVar = StringVar()
        self.minSamplesVar.set(5)
        self.maxEpsVar = StringVar()
        self.maxEpsVar.set('inf')
        self.metricVar = StringVar()
        self.metricVar.set('minkowski')
        self.pVar = StringVar()
        self.pVar.set(2)
        self.metricParamsVar = StringVar()
        self.metricParamsVar.set('None')
        self.clusterMethodVar = StringVar()
        self.clusterMethodVar.set('xi')
        self.epsVar = StringVar()
        self.epsVar.set('None')
        self.xiVar = StringVar()
        self.xiVar.set(0.05)
        self.minClusterSizeVar = StringVar()
        self.minClusterSizeVar.set('None')
        self.leafSizeVar = StringVar()
        self.leafSizeVar.set(30)
        self.preCorrectionVar = StringVar()
        self.algVar=StringVar()

    def enter_fg(self,event):
        event.widget['fg'] = 'blue'
    def leave_fg(self,event):
        event.widget['fg'] = 'black'
    def callBack(self,url):
        webbrowser.open_new(url)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("tsv","*.tsv")))
        return filename1
    def pathtooutfile(self):
        dirName=filedialog.askdirectory(initialdir="~/Desktop")
        return dirName
    def back(self):
        self.root.destroy()
        GUImain.GUImain().rootGUI()
    def Main(self):
        def makeAddOptions(bin):
            if bin.get():
                p_Entry.grid(column=1, row=5)
                p_label.grid(column=0, row=5)

                metric_label.grid(column=0, row=6)
                metric_Entry.grid(column=1, row=6)

                xi_label.grid(column=0, row=7)
                xi_Entry.grid(column=1, row=7)

                clusterMethod_label.grid(column=0, row=8)
                clusterMethod_Entry.grid(column=1, row=8)

                metricParams_label.grid(column=0, row=9)
                metricParams_Entry.grid(column=1, row=9)

                minClusterSize_label.grid(column=0, row=10)
                minClusterSize_Entry.grid(column=1, row=10)

                leafSize_label.grid(column=0, row=11)
                leafSize_Entry.grid(column=1, row=11)

                preCorrection_label.grid(column=0, row=12)
                preCorrection_CB.grid(column=1, row=12)

                alg_label.grid(column=0, row=13)
                alg_CB.grid(column=1, row=13)

            else:
                p_Entry.grid_remove()
                p_label.grid_remove()

                metric_label.grid_remove()
                metric_Entry.grid_remove()

                xi_label.grid_remove()
                xi_Entry.grid_remove()

                clusterMethod_label.grid_remove()
                clusterMethod_Entry.grid_remove()

                metricParams_label.grid_remove()
                metricParams_Entry.grid_remove()

                minClusterSize_label.grid_remove()
                minClusterSize_Entry.grid_remove()

                leafSize_label.grid_remove()
                leafSize_Entry.grid_remove()

                preCorrection_label.grid_remove()
                preCorrection_CB.grid_remove()

                alg_label.grid_remove()
                alg_CB.grid_remove()

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

        minSamples_label=Label(self.root,text='minSamples')
        minSamples_label.grid(column=0,row=2)
        minSamples_Entry = Entry(self.root,textvariable=self.minSamplesVar)
        minSamples_Entry.grid(column=1,row=2)

        maxEps_label=Label(self.root,text='max_eps')
        maxEps_label.grid(column=0, row=3)
        maxEps_Entry=Entry(self.root,textvariable=self.maxEpsVar)
        maxEps_Entry.grid(column=1,row=3)

        eps_label = Label(self.root,text='eps')
        eps_label.grid(column=0,row=4)
        eps_Entry=Entry(self.root,textvariable=self.epsVar)
        eps_Entry.grid(column=1,row=4)
        p_label = Label(self.root, text='Parameter for the Minkowski metric from pairwise_distances')
        p_Entry = Entry(self.root, textvariable=self.pVar)

        metric_label = Label(self.root, text='metric')
        metric_Entry = Entry(self.root, textvariable=self.metricVar)

        xi_label = Label(self.root, text='xi')
        xi_Entry = Entry(self.root, textvariable=self.xiVar)

        clusterMethod_label = Label(self.root, text='clusterMethod')
        clusterMethod_Entry = Entry(self.root, textvariable=self.clusterMethodVar)

        metricParams_label = Label(self.root, text='metric params')
        metricParams_Entry = Entry(self.root, textvariable=self.metricParamsVar)


        minClusterSize_label = Label(self.root, text='min cluster size:')
        minClusterSize_Entry = Entry(self.root, textvariable=self.minClusterSizeVar)

        leafSize_label = Label(self.root, text='leaf size:')
        leafSize_Entry = Entry(self.root, textvariable=self.leafSizeVar)

        preCorrection_label = Label(self.root, text='predecessor_correction:')
        preCorrectionOpt = ['True','False']
        preCorrection_CB = ttk.Combobox(self.root,textvariable=self.preCorrectionVar,values=preCorrectionOpt,state='readonly')
        self.preCorrectionVar.set(preCorrectionOpt[0])


        alg_label = Label(self.root, text='Algorithm:')
        algOpt=['auto', 'ball_tree', 'kd_tree', 'brute']
        alg_CB = ttk.Combobox(self.root,textvariable=self.algVar,values=algOpt,state='readonly')
        self.algVar.set(algOpt[0])

        helpLink = Label(self.root, text="help", fg="black",font=("Arial", 20))
        helpLink.place(relx=0.01,rely=0.9)
        helpLink.bind('<Button-1>',
                        lambda e: self.callBack('https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html'))
        helpLink.bind('<Enter>',self.enter_fg)
        helpLink.bind('<Leave>',self.leave_fg)

        bin = BooleanVar()
        bin.set(False)
        detailOptions_CHB = ttk.Checkbutton(self.root, text='add options',variable=bin,command=lambda :makeAddOptions(bin))
        detailOptions_CHB.grid(column=3,row=14)

        # nJobs_label = Label(self.root, text='The number of OpenMP threads:')
        # nJobs_label.grid(column=0, row=10)
        # nJobs_Entry = Entry(self.root, textvariable='')
        # nJobs_Entry.grid(column=1, row=10)

        submit=Button(self.root,text="submit",command=lambda :optics(iFilename.get(),oFilename.get(),int(self.minSamplesVar.get())
                                                                     ,self.maxEpsVar.get(),self.metricVar.get(),int(self.pVar.get())
                                                                     ,self.metricParamsVar.get(),self.clusterMethodVar.get(),self.epsVar.get()
                                                                     ,float(self.xiVar.get()),bool(self.preCorrectionVar.get()),int(self.leafSizeVar.get())
                                                                     ,self.minClusterSizeVar.get(),self.algVar.get()).run())

        submit.grid(column=1,row=14)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=14)

        self.root.mainloop()

if __name__ == '__main__':
    opticsGUI().Main()