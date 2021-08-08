import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import kmeans
import spectralClustering
import meanShift
import dbscan
import optics
import affinityPropagation
import pandas as pd
import elbowKmeans
from algorithms.patternmining.createDB import createDB
from algorithms.patternmining.euclidDistance import EuclidDistance
from dataProcessing.VerticalExpansion import verticalExpansion
from dataProcessing.HorizontalExpansion import HorizontalExpansion


class GUImain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("rasterMiner: Discovering Knowledge Hidden in Raster Images")

    def uploadInputDir(self, event=None):
        # filename = filedialog.askopenfilename()
        inputDir = filedialog.askdirectory()
        print('Selected:', inputDir)
        inputRasterFolder = inputDir
        return inputRasterFolder

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

    def rasterToHorizontal(self,inputRasterFolderName,fileExtension,outputFolderName,startBandVar,endBandVar):
        print("Calling HorizontalExpansion.py")
        a = HorizontalExpansion(inputRasterFolderName, fileExtension, outputFolderName,
                            startBandVar, endBandVar)
        a.convert()
            #     print(f'-bounds{i}',end=' ')
            # print(inputRasterFolderName.get())
            # print(outputFolderName.get())
    def rasterToVertical(self,inputRasterFolderName,fileExtension,outputFolderName):
        print("Calling VertificalExpansion.py")
        a = verticalExpansion(inputRasterFolderName, fileExtension, outputFolderName)
        a.convert()


    def judgeAlg(self,target):
        self.root.destroy()
        if target == 'k-Means/k-Means++':
            kmeans.kmeansGUI().Main()
        elif target == 'DBScan':
            dbscan.DBScanGUI().Main()
        elif target == 'MeanShift':
            meanShift.meanShiftGUI().Main()
        elif target == 'SpectralClustering':
            spectralClustering.spectralGUI().Main()
        elif target == 'OPTICS':
            optics.opticsGUI().Main()
        elif target == 'AffinityPropagation':
            affinityPropagation.affinityPropagationGUI().Main()
        elif target == 'Elbow-kmeans':
            elbowKmeans.elbowKmeansGUI().Main()
        # elif target == 'Elbow-kmeans++':
        #     elbowKmeansPl.elbowKmeansPlGUI().Main()


    def rootGUI(self):
        def addOpt():
            if wranglingVar.get() == 'fill':
                dropValue_CB.grid_remove()
                convertValue_TB.grid(column=2, row=2, padx=30, pady=30)
            else:
                convertValue_TB.grid_remove()
                dropValue_CB.grid(column=2, row=2, padx=30, pady=30)

        def dataWrangling():
            df = pd.read_csv(iFileNameHandlingNan.get(), encoding="shift-jis")

            if wranglingVar.get() == 'fill':
                df = df.fillna(convertVal.get())
            elif wranglingVar.get() == 'drop':
                if dropVar.get() == 'all':
                    df = df.dropna(how='all').dropna(how='all', axis=1)
                elif dropVar.get() == 'all column':
                    df = df.dropna(how='all', axis=1)
                elif dropVar.get() == 'all row':
                    df = df.dropna(how='all')
                elif dropVar.get() == 'any':
                    df = df.dropna(how='any').dropna(how='any', axis=1)
                elif dropVar.get() == 'any column':
                    df = df.dropna(how='any')
                elif dropVar.get() == 'any row':
                    df = df.dropna(how='any', axis=1)
            print(df)
            df.to_csv(oFileNameHandlingNan.get() + '/result.csv')

        clusteringAlgorithms = {'Parameter tuning': ["Elbow-kmeans", "Elbow-kmeans++"],
                          'individual algorithm': ["k-Means/k-Means++", "DBScan", "SpectralClustering", "MeanShift",
                                                   "OPTICS","BIRCH","AffinityPropagation"]}
        pamiAlgorithms = ['SpatialEclat','spatialFPGrowth']
        options = ['multi-band images', 'single-band temporal images',"handling Nan value"]
        mineOptions = ['Temporal File', 'Mining', 'Neighborhood File']
        condition = ['<=', '>=','<','>']
        nanOpt = ['drop', 'fill']
        dropOpt = ['all', 'all column', 'all row', 'any', 'any column', 'any row']


        tabControl = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        tab5 = ttk.Frame(tabControl)

        subTab1 = ttk.Notebook(tab1)
        subTab1.pack(expand=True,side='top')
        subTab1.pack(fill='both')
        subTab2 = ttk.Notebook(tab2)
        subTab2.pack(expand=True,side='top')
        subTab2.pack(fill='both')
        subTab3 = ttk.Notebook(tab3)
        subTab3.pack(expand=True,side='top')
        subTab3.pack(fill='both')

        tabControl.add(tab1, text='Convert Raster Files to TSV Files')
        tabControl.add(tab2, text='Pattern Mining')
        tabControl.add(tab3, text='Clustering')
        tabControl.add(tab4, text='Classification')
        tabControl.add(tab5, text='Prediction')
        tabControl.pack(expand=1, fill="both")

        v2 = tk.StringVar()
        inputRasterFolderName = tk.StringVar()
        iFileNameHandlingNan = tk.StringVar()
        oFileNameHandlingNan = tk.StringVar()
        fileExtension = tk.StringVar()
        start_band_var = tk.StringVar()
        end_band_var = tk.StringVar()
        wranglingVar = tk.StringVar()
        convertVal = tk.StringVar()
        dropVar = tk.StringVar()
        inputTempFileName = tk.StringVar()
        conditionVar = tk.StringVar()
        thresholdVar = tk.StringVar()
        inputNeighborFileVar = tk.StringVar()
        outputNeighborFolderVar = tk.StringVar()
        pamiAlgVar = tk.StringVar()
        outputFolderNameTab1 = tk.StringVar()
        oTempFolderVar = tk.StringVar()





        for algorithm in clusteringAlgorithms.keys():
            subFrame3 = ttk.Frame(subTab3, height=600, width=800)
            subTab3.add(subFrame3,text=algorithm)
            cb2 = ttk.Combobox(subFrame3, textvariable=v2, state='readonly')
            cb2.place(relx=0.25, rely=0.5, relwidth=0.5)
            submit = ttk.Button(subFrame3, text='submit', command=lambda :self.judgeAlg(v2.get()))
            submit.place(relx=0.378, rely=0.7, relwidth=0.25, relheight=0.125)
            if algorithm == 'Parameter tuning':
                cb2.config(values=clusteringAlgorithms['Parameter tuning'])
            elif algorithm == 'individual algorithm':
                cb2.config(values=clusteringAlgorithms['individual algorithm'])

        for mineOption in mineOptions:
            subFrame2 = ttk.Frame(subTab2, height=600, width=800)
            subTab2.add(subFrame2, text=mineOption)
            if mineOption == 'Temporal File':
                iTempFile_label = ttk.Label(subFrame2, text='input file')
                iTempFile_label.grid(column=0, row=0, padx=60, pady=30, sticky='W')
                iTempFile_TB = ttk.Entry(subFrame2, textvariable=inputTempFileName, width=40)
                iTempFile_TB.grid(column=1, row=0, padx=60, pady=30)
                iTempFile_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda :inputTempFileName.set(str(self.uploadInputFile())))
                iTempFile_B.grid(row=0, column=2, padx=60, pady=30)

                oTempFolder_label = ttk.Label(subFrame2, text='output folder')
                oTempFolder_label.grid(column=0, row=1, padx=60, pady=30, sticky='W')
                oTempFolder_TB = ttk.Entry(subFrame2, textvariable=oTempFolderVar, width=40)
                oTempFolder_TB.grid(column=1, row=1, padx=60, pady=30)
                oTempFolder_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda :oTempFolderVar.set(str(self.uploadOutputDir())))
                oTempFolder_B.grid(row=1, column=2, padx=60, pady=30)

                condition_label = ttk.Label(subFrame2, text='condition')
                condition_label.grid(column=0,row=2, padx=60, pady=30, sticky='W')
                condition_CB = ttk.Combobox(subFrame2, textvariable=conditionVar, values=condition, state='readonly')
                condition_CB.grid(column=1, row=2, padx=60, pady=30)

                threshold_label = ttk.Label(subFrame2, text='threshold')
                threshold_label.grid(column=0, row=3, padx=60, pady=30)
                threshold_TB = ttk.Entry(subFrame2, textvariable=thresholdVar)
                threshold_TB.grid(column=1, row=3, padx=60, pady=30)

                submit = tk.Button(subFrame2, text='submit', command=lambda :createDB(inputTempFileName.get(), oTempFolderVar.get()
                                                                                      ,conditionVar.get(), int(thresholdVar.get())).run())
                submit.grid(row=4, column=0, pady=30)

            elif mineOption == 'Mining':
                patternMiningAlg_label = ttk.Label(subFrame2, text='select the algorithm')
                patternMiningAlg_label.grid(column=0, row=0, padx=60, pady=30, sticky='W')

                condition_CB = ttk.Combobox(subFrame2, textvariable=pamiAlgVar, values=pamiAlgorithms, state='readonly')
                condition_CB.grid(column=1, row=0, padx=60, pady=30)

                submit = tk.Button(subFrame2, text='submit')
                submit.grid(row=1, column=0, pady=30)

            elif mineOption == 'Neighborhood File':
                iNeighborFile_label = ttk.Label(subFrame2, text='Select the file:')
                iNeighborFile_label.grid(row=0, column=0, padx=60, pady=30, sticky='W')
                iNeighborFile_TB = tk.Entry(subFrame2, textvariable=inputNeighborFileVar, width=40)
                iNeighborFile_TB.grid(row=0, column=1)

                iNeighborFile_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda: inputNeighborFileVar.set(str(self.uploadInputFile())))
                iNeighborFile_B.grid(row=0, column=2, padx=60)

                outputNeighborFolder_label = ttk.Label(subFrame2, text='Select output folder:')
                outputNeighborFolder_label.grid(column=0, row=1, padx=60, pady=30, sticky='W')
                outputNeighborFolder_TB = tk.Entry(subFrame2, textvariable=outputNeighborFolderVar, width=40)
                outputNeighborFolder_TB.grid(row=1, column=1)

                outputNeighborFolder_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda: outputNeighborFolderVar.set(str(self.uploadOutputDir())))
                outputNeighborFolder_B.grid(row=1, column=2, padx=60)

                threshold_label = ttk.Label(subFrame2, text='threshold')
                threshold_label.grid(column=0, row=2, padx=60, pady=30)
                threshold_TB = ttk.Entry(subFrame2, textvariable=thresholdVar)
                threshold_TB.grid(column=1, row=2, padx=60, pady=30)

                submit = tk.Button(subFrame2, text='submit', command=lambda :EuclidDistance(inputNeighborFileVar.get(), outputNeighborFolderVar.get(),
                                                                                            int(thresholdVar.get())).run())
                submit.grid(row=3, column=0, pady=30)


        for option in options:
            subFrame1=ttk.Frame(subTab1, height=600, width=800)
            subTab1.add(subFrame1,text=option)
            label1 = ttk.Label(subFrame1, text='Select the folder containing raster files:')
            label2 = ttk.Label(subFrame1, text='Enter the file extension of the raster files:')
            label3 = ttk.Label(subFrame1, text='Select output folder:')
            label4 = ttk.Label(subFrame1, text='Initial band number')
            label5 = ttk.Label(subFrame1, text='Final band number')
            label1.grid(column=0, row=0, padx=30, pady=30, sticky='W')
            label2.grid(column=0, row=1, padx=30, pady=30, sticky='W')
            label3.grid(column=0, row=2, padx=30, pady=30, sticky='W')
            label4.grid(column=0, row=3, padx=30, pady=30, sticky='W')
            label5.grid(column=0, row=4, padx=30, pady=30, sticky='W')

            e1 = tk.Entry(subFrame1, textvariable=inputRasterFolderName,width=40)
            e2 = tk.Entry(subFrame1, textvariable=fileExtension,width=40)
            e3 = tk.Entry(subFrame1, textvariable=outputFolderNameTab1,width=40)

            e1.grid(row=0, column=1)
            e2.grid(row=1, column=1)
            e3.grid(row=2, column=1)

            button1 = tk.Button(subFrame1, text='Browse', command=lambda: inputRasterFolderName.set(str(self.uploadInputDir())))
            button1.grid(row=0, column=2,padx=30)
            button2 = tk.Button(subFrame1, text='Browse', command=lambda: outputFolderNameTab1.set(str(self.uploadOutputDir())))
            button2.grid(row=2, column=2,padx=30)

            start_band_TB = tk.Entry(subFrame1, textvariable=start_band_var, width=5)
            start_band_TB.grid(row=3, column=1)
            end_band_TB = tk.Entry(subFrame1, textvariable=end_band_var, width=5)
            end_band_TB.grid(row=4, column=1)

            if option == 'multi-band images':
                label4.grid()
                label5.grid()
                start_band_TB.grid()
                end_band_TB.grid()
                submit = tk.Button(subFrame1, text='submit',
                                   command=lambda: self.rasterToHorizontal(str(inputRasterFolderName.get()),
                                                                           str(fileExtension.get()),
                                                                           str(outputFolderNameTab1.get()),
                                                                           int(start_band_var.get()),
                                                                           int(end_band_var.get())))

                submit.bind('<1>', lambda e: print('running'))
                submit.grid(row=6, column=0)
            elif option == 'single-band temporal images':
                label4.grid_remove()
                label5.grid_remove()
                start_band_TB.grid_remove()
                end_band_TB.grid_remove()
                submit = tk.Button(subFrame1, text='submit',
                                   command=lambda: self.rasterToVertical(str(inputRasterFolderName.get()),
                                                                         str(fileExtension.get()),
                                                                         str(outputFolderNameTab1.get())))
                submit.bind('<1>', lambda e: print('running'))
                submit.grid(row=6, column=0)
            elif option == 'handling Nan value':
                convertValue_TB = ttk.Entry(subFrame1, textvariable=convertVal, width=10)
                dropValue_CB = ttk.Combobox(subFrame1, textvariable=dropVar, values=dropOpt, state='readonly')
                e1.grid_remove()
                e2.grid_remove()
                e3.grid_remove()
                button1.grid_remove()
                button2.grid_remove()
                label1.grid_remove()
                label2.grid_remove()
                label3.grid_remove()
                label4.grid_remove()
                label5.grid_remove()
                start_band_TB.grid_remove()
                end_band_TB.grid_remove()
                label6 = ttk.Label(subFrame1,text='Select the inputFile')
                label6.grid(row=0, column=0, padx=30, pady=30)
                label7 = ttk.Label(subFrame1,text='Select the outputFolder')
                label7.grid(row=1, column=0, padx=30, pady=30)
                label7 = ttk.Label(subFrame1,text='Select the handling type')
                label7.grid(row=2, column=0, padx=30, pady=30)


                iFileName_TB = tk.Entry(subFrame1, textvariable=iFileNameHandlingNan, width=40)
                iFileName_TB.grid(row=0, column=1, padx=30, pady=30)
                iFileName_B = tk.Button(subFrame1, text='Browse',
                                    command=lambda :iFileNameHandlingNan.set(str(self.uploadInputFile())))
                oFileName_TB = tk.Entry(subFrame1, textvariable=oFileNameHandlingNan, width=40)
                oFileName_TB.grid(row=1, column=1, padx=30, pady=30)
                oFIleName_B = tk.Button(subFrame1, text='Browse',
                                    command=lambda :oFileNameHandlingNan.set(str(self.uploadOutputDir())))
                nanValueTreat_CB = ttk.Combobox(subFrame1, textvariable=wranglingVar, value=nanOpt, state='readonly')
                nanValueTreat_CB.grid(row=2, column=1, padx=30, pady=30)
                # nanValueTreat_CB.set(nanOpt[0])
                nanValueTreat_CB.bind('<<ComboboxSelected>>',
                                      lambda e: addOpt())

                # valueConvert_CHB = ttk.Checkbutton(subFrame1,text='convertNanValue',variable=wranglingFlag,command=lambda :makeOptions(wranglingFlag))
                # valueConvert_CHB.grid(row=1, column=0, padx=30, pady=30)

                iFileName_B.grid(row=0, column=2, padx=30)
                oFIleName_B.grid(row=1, column=2, padx=30)

                submit = tk.Button(subFrame1, text='submit')
                submit.grid(row=3, column=1)
                submit.bind('<1>',
                            lambda e:dataWrangling())

        # ttk.Label(tab2, text='Input csv file:').grid(column=0, row=0, padx=30, pady=30)
        # v1 = tk.StringVar()
        # cb = ttk.Combobox(subFrame1, textvariable=v1, values=Type, state='readonly')
        # cb.grid(column=1, row=3, padx=30, pady=30, sticky='W')
        # cb.set(Type[0])
        # cb.bind(
        #     '<<ComboboxSelected>>',
        #     lambda e: updateWidget()
        # )
        self.root.mainloop()

if __name__ == '__main__':
    GUImain().rootGUI()

# def elbowAlgSelected():
#     selectBtn1.state(['pressed'])
#     selectBtn2.state(['!pressed'])
# def simpleAlgSelected():
#     selectBtn1.state(['!pressed'])
#     selectBtn2.state(['pressed'])

# ttk.Label(subFrame3, text='Select algorithm',font=("Arial", 20)).place(relx=0,rely=0,relwidth=1,relheight=0.125)

# make textbox

# button3 = tk.Button(tab3, text='submit', command=)

# v2 = tk.StringVar()

# selectBtn1 = ttk.Button(tab3,text='Parameter tuning',padding=(10),command=elbowAlgSelected)
# selectBtn1.bind('<1>', lambda e: cb2.config(values=Algorithms['elbowAlg']))
# selectBtn2 = ttk.Button(tab3,text='Individual algorithms',padding=(10),command=simpleAlgSelected)
# selectBtn2.bind('<1>', lambda e: ))
# selectBtn1.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.125)
# selectBtn2.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.125)
# selectBtn1.grid(row=1,column=1,sticky='W')
# selectBtn2.grid(row=1,column=2,sticky='W')
# print(str(v2.get))


