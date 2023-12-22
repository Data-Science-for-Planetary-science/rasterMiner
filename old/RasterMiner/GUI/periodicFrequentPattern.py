from tkinter import *
from tkinter import filedialog
from tkinter import ttk

import rasterMiner
from algorithms.patternmining.runSpatialFPGrowth import runSpatialFpGrowth


class periodicFrequentPattern:
    """"""
    def __init__(self):
        """Constructor for periodicFrequentPattern"""
        self.root = Tk()
        self.root.title('periodicFrequentPattern')
        self.mineTargetInputFileVar = StringVar()
        self.mineTargetOutputFileVar = StringVar()
        self.minSupVar = StringVar()
        self.mineinputNeighborFileVar = StringVar()
    def uploadOutputDir(self, event=None):
        # filename = filedialog.askopenfilename()
        outDir = filedialog.askdirectory()
        print('Selected:', outDir)
        outputFolder = outDir
        return outputFolder

    def uploadInputFile(self):
        inputFile = filedialog.askopenfilename()
        print('selected:', inputFile)
        return inputFile


    def back(self):
        self.root.destroy()
        rasterMiner.GUImain().rootGUI()
    def Main(self):
        mineTargetInputFile_label = ttk.Label(self.root, text='select the input file name')
        mineTargetInputFile_label.grid(column=0, row=0, padx=60, pady=30, sticky='W')
        mineTargetInputFile_TB = Entry(self.root, textvariable=self.mineTargetInputFileVar, width=40)
        mineTargetInputFile_TB.grid(row=0, column=1)
        mineTargetInputFile_B = Button(self.root, text='Browse',
                                    command=lambda: self.mineTargetInputFileVar.set(str(self.uploadInputFile())))
        mineTargetInputFile_B.grid(row=0, column=2, padx=60)

        mineTargetOutputFile_label = ttk.Label(self.root, text='select the output folder name')
        mineTargetOutputFile_label.grid(column=0, row=1, padx=60, pady=30, sticky='W')
        mineTargetOutputFile_TB = Entry(self.root, textvariable=self.mineTargetOutputFileVar, width=40)
        mineTargetOutputFile_TB.grid(row=1, column=1)
        mineTargetOutputFile_B = Button(self.root, text='Browse',
                                    command=lambda: self.mineTargetOutputFileVar.set(str(self.uploadOutputDir())))
        mineTargetOutputFile_B.grid(row=1, column=2, padx=60)

        mineInputNeighborFile_label = ttk.Label(self.root, text='Select the Neighborhood file:')
        mineInputNeighborFile_label.grid(row=2, column=0, padx=60, pady=30, sticky='W')
        mineInputNeighborFile_TB = Entry(self.root, textvariable=self.mineinputNeighborFileVar, width=40)
        mineInputNeighborFile_TB.grid(row=2, column=1)

        mineInputNeighborFile_B = Button(self.root, text='Browse',
                            command=lambda: self.mineinputNeighborFileVar.set(str(self.uploadInputFile())))
        mineInputNeighborFile_B.grid(row=2, column=2, padx=60)

        minSup_label = ttk.Label(self.root, text='minSup')
        minSup_label.grid(column=0, row=3, padx=60, pady=30)
        minSup_TB = ttk.Entry(self.root, textvariable=self.minSupVar, width=10)
        minSup_TB.grid(column=1, row=3, padx=60, pady=30)

        submit = Button(self.root, text='submit',
                           command=lambda: runSpatialFpGrowth(self.mineTargetInputFileVar.get(),
                                                                      self.mineinputNeighborFileVar.get(),
                                                                      self.mineTargetOutputFileVar.get(),
                                                                        int(self.minSupVar.get())).run())
        submit.grid(row=4, column=0, pady=30)

        back=Button(self.root, text="Back", command=self.back)
        back.grid(column=2,row=4)