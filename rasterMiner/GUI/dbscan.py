from tkinter import *
from tkinter import filedialog, Label
from tkinter import ttk
# import re
# import ast
# import final_code
import GUImain
from algorithms.clustering.dbscan import DBScan
import webbrowser

class DBScanGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('DBScan')
        self.root.minsize(600, 400)
        self.epsVar = StringVar()
        self.epsVar.set(0.5)
        self.minSampleVar = StringVar()
        self.minSampleVar.set(5)
        self.leafSizeVar = StringVar()
        self.leafSizeVar.set(30)
        self.powerVar = StringVar()
        self.powerVar.set(None)
        self.algVar = StringVar()
        self.metricVar = StringVar()
        self.metricVar.set('euclidean')
        self.metricParamsVar = StringVar()
        self.metricParamsVar.set(None)



    def callBack(self,url):
        webbrowser.open_new(url)
    def openFile(self):
        filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(('csv','*.csv'),('txt','*.txt'),('tsv','*.tsv')))
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
                leafSize_label.grid(column=0, row=5)
                leafSize_Entry.grid(column=1, row=5)

                p_label.grid(column=0, row=6)
                p_Entry.grid(column=1, row=6)

                metric_label.grid(column=0, row=7)
                metric_Entry.grid(column=1, row=7)

                metricParams_label.grid(column=0, row=8)
                metricParams_Entry.grid(column=1, row=8)

                alg_label.grid(column=0, row=9)
                alg_CB.grid(column=1, row=9)
            else:
                leafSize_Entry.grid_remove()
                leafSize_label.grid_remove()

                p_Entry.grid_remove()
                p_label.grid_remove()

                metric_label.grid_remove()
                metric_Entry.grid_remove()

                metricParams_label.grid_remove()
                metricParams_Entry.grid_remove()

                alg_CB.grid_remove()
                alg_label.grid_remove()

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

        eps_label=Label(self.root,text='eps:')
        eps_label.grid(column=0,row=2)
        eps_Entry = Entry(self.root,textvariable=self.epsVar)
        eps_Entry.grid(column=1,row=2)

        minSample_label = Label(self.root, text='minSample:')
        minSample_label.grid(column=0, row=3)
        minSample_Entry = Entry(self.root, textvariable=self.minSampleVar)
        minSample_Entry.grid(column=1, row=3)

        leafSize_label = Label(self.root, text='leafSize:')
        leafSize_Entry = Entry(self.root, textvariable=self.leafSizeVar)

        p_label = Label(self.root, text='power:')
        p_Entry = Entry(self.root, textvariable=self.powerVar)

        metric_label = Label(self.root, text='metric')
        metric_Entry = Entry(self.root, textvariable=self.metricVar)

        metricParams_label = Label(self.root, text='metric params')
        metricParams_Entry = Entry(self.root, textvariable=self.metricParamsVar)

        algOpt = ['auto', 'ball_tree', 'kol_tree', 'brute']
        alg_CB = ttk.Combobox(self.root, textvariable=self.algVar, values=algOpt, state='readonly')
        self.algVar.set(algOpt[0])
        alg_label = Label(self.root, text='Enter Max iterations value:')

        helpLink = Label(self.root, text="help", fg="blue", cursor="hand2",font=("Arial", 20))
        helpLink.place(relx=0.01,rely=0.9)
        helpLink.bind('<Button-1>',
                        lambda e: self.callBack('https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html'))


        bin = BooleanVar()
        bin.set(False)
        detailOptions_CHB = ttk.Checkbutton(self.root, text='add options',variable=bin,command=lambda :makeAddOptions(bin))
        detailOptions_CHB.grid(column=0,row=10)

        submit=Button(self.root,text="submit",command=lambda :DBScan(iFilename.get(),oFilename.get(),self.epsVar.get(),self.minSampleVar.get()
                                                             ,self.leafSizeVar.get(),self.powerVar.get(),self.metricVar.get()
                                                                    ,self.metricParamsVar.get(),self.algVar.get()).run())
        submit.grid(column=1,row=10)
        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=10)

        self.root.mainloop()

if __name__ == '__main__':
    DBScanGUI().Main()

