import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from GUI import kmeans
from GUI import dbscan
from GUI import spectralClustering
from GUI import meanShift

from dataProcessing.VerticalExpansion import verticalExpansion
from  dataProcessing.HorizontalExpansion import HorizontalExpansion
from algorithms.clustering import *
from GUI import *


class main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("rasterMiner: Discovering Knowledge Hidden in Raster Images")

    def UploadAction1(self, event=None):
        # filename = filedialog.askopenfilename()
        filename = filedialog.askdirectory()
        print('Selected:', filename)
        inputRasterFolder = filename
        return inputRasterFolder

    def UploadAction2(self, event=None):
        # filename = filedialog.askopenfilename()
        filename = filedialog.askdirectory()
        print('Selected:', filename)
        outputFolder = filename
        return outputFolder

    def rasterToHorizontal(self,inputRasterFolderName,fileExtension,outputFolderName,startBandVar,endBandVar):
        print("Calling HorizontalExpansion.py")
        HorizontalExpansion(inputRasterFolderName, fileExtension, outputFolderName,
                            startBandVar, endBandVar)
            #     print(f'-bounds{i}',end=' ')
            # print(inputRasterFolderName.get())
            # print(outputFolderName.get())
    def rasterToVertical(self,inputRasterFolderName,fileExtension,outputFolderName):
        print("Calling VertificalExpansion.py")
        verticalExpansion(inputRasterFolderName, fileExtension, outputFolderName)

    def judgeAlg(self,target):
        self.root.destroy()
        if target == 'k-means/k-means++':
            kmeans.kmeansGUI().Main()
        elif target == 'meanShift':
            meanShift.meanShiftGUI().Main()
        elif target == 'spectral Clustering':
            spectralClustering.spectralGUI().Main()

    def main(self):

        inputRasterFolder = ''
        outputFolder = ''

        Algorithms = {'Parameter tuning': ["elbow-kmeans", "elbow-kmeans++"],
                          'individual algorithm': ["k-means/k-means++", "DBscan", "Spectral Clustering", "MeanShift",
                                                   "optics",
                                                   "birch"]}
        options = ['multi-band images', 'single-band temporal images']
        tabControl = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        tab5 = ttk.Frame(tabControl)

        subTab1 = ttk.Notebook(tab1)
        subTab1.pack(expand=True,side='top')
        subTab1.pack(fill='both')
        subTab3 = ttk.Notebook(tab3)
        subTab3.pack(expand=True,side='top')
        subTab3.pack(fill='both')



        tabControl.add(tab1, text='Convert Raster Files to TSV Files')
        tabControl.add(tab2, text='Pattern Mining')
        tabControl.add(tab3, text='Clustering')
        tabControl.add(tab4, text='Classification')
        tabControl.add(tab5, text='Prediction')
        tabControl.pack(expand=1, fill="both")



        # def elbowAlgSelected():
        #     selectBtn1.state(['pressed'])
        #     selectBtn2.state(['!pressed'])
        # def simpleAlgSelected():
        #     selectBtn1.state(['!pressed'])
        #     selectBtn2.state(['pressed'])



        #ttk.Label(subFrame3, text='Select algorithm',font=("Arial", 20)).place(relx=0,rely=0,relwidth=1,relheight=0.125)

        # make textbox


        #button3 = tk.Button(tab3, text='submit', command=)





        #v2 = tk.StringVar()

        # selectBtn1 = ttk.Button(tab3,text='Parameter tuning',padding=(10),command=elbowAlgSelected)
        # selectBtn1.bind('<1>', lambda e: cb2.config(values=Algorithms['elbowAlg']))
        # selectBtn2 = ttk.Button(tab3,text='Individual algorithms',padding=(10),command=simpleAlgSelected)
        # selectBtn2.bind('<1>', lambda e: ))
        # selectBtn1.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.125)
        # selectBtn2.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.125)
        #selectBtn1.grid(row=1,column=1,sticky='W')
        #selectBtn2.grid(row=1,column=2,sticky='W')
        #print(str(v2.get))


        for algorithm in Algorithms.keys():
            subFrame3 = ttk.Frame(subTab3, height=600, width=800)
            subTab3.add(subFrame3,text=algorithm)
            v2 = tk.StringVar()
            cb2 = ttk.Combobox(subFrame3, textvariable=v2, state='readonly')
            cb2.place(relx=0.25, rely=0.5, relwidth=0.5)
            submit = ttk.Button(subFrame3, text='submit', command=lambda :self.judgeAlg(v2.get()))
            submit.place(relx=0.378, rely=0.7, relwidth=0.25, relheight=0.125)
            if algorithm == 'Parameter tuning':
                cb2.config(values=Algorithms['Parameter tuning'])
            elif algorithm == 'individual algorithm':
                cb2.config(values=Algorithms['individual algorithm'])

        input_raster_folder_name = tk.StringVar()
        output_folder_name = tk.StringVar()
        file_extension = tk.StringVar()
        start_band_var = tk.StringVar()
        end_band_var = tk.StringVar()

        for option in options:
            subFrame1=ttk.Frame(subTab1,height=600,width=800)
            subTab1.add(subFrame1,text=option)
            label1 = ttk.Label(subFrame1, text='Select the folder containing raster files:')
            label2 = ttk.Label(subFrame1, text='Enter the file extension of the raster files:')
            label3 = ttk.Label(subFrame1, text='Select output folder:')
            label4 = ttk.Label(subFrame1, text='Initial band number')
            label5 = ttk.Label(subFrame1, text='Final band number')
            label1.grid(column=0, row=0,padx=30, pady=30,sticky='W')
            label2.grid(column=0, row=1,padx=30, pady=30,sticky='W')
            label3.grid(column=0, row=2, padx=30, pady=30, sticky='W')
            label4.grid(column=0, row=3, padx=30, pady=30, sticky='W')
            label5.grid(column=0, row=4, padx=30, pady=30, sticky='W')

            e1 = tk.Entry(subFrame1, textvariable=input_raster_folder_name)
            e2 = tk.Entry(subFrame1, textvariable=file_extension)
            e3 = tk.Entry(subFrame1, textvariable=output_folder_name)

            e1.grid(row=0, column=1)
            e2.grid(row=1, column=1)
            e3.grid(row=2, column=1)

            button1 = tk.Button(subFrame1, text='Browse', command=lambda: input_raster_folder_name.set(str(self.UploadAction1())))
            button1.grid(row=0, column=2)
            button2 = tk.Button(subFrame1, text='Browse', command=lambda: output_folder_name.set(str(self.UploadAction2())))
            button2.grid(row=2, column=2)


            start_band_tb = tk.Entry(subFrame1, textvariable=start_band_var, width=5)
            start_band_tb.grid(row=3, column=1)
            end_band_tb = tk.Entry(subFrame1, textvariable=end_band_var, width=5)
            end_band_tb.grid(row=4, column=1)

            if option == 'multi-band images':
                label4.grid()
                label5.grid()
                start_band_tb.grid()
                end_band_tb.grid()
                submit = tk.Button(subFrame1, text='submit',
                                   command=lambda: self.rasterToHorizontal(str(input_raster_folder_name.get()),
                                                                           str(file_extension.get()),
                                                                           str(output_folder_name.get()),
                                                                           int(start_band_var.get()),
                                                                           int(end_band_var.get())))

                submit.bind('<1>', lambda e: print('running'))
                submit.grid(row=6, column=0)
            elif option == 'single-band temporal images':
                label4.grid_remove()
                label5.grid_remove()
                start_band_tb.grid_remove()
                end_band_tb.grid_remove()
                submit = tk.Button(subFrame1, text='submit',
                                   command=lambda: self.rasterToVertical(str(input_raster_folder_name.get()),
                                                                         str(file_extension.get()),
                                                                         str(output_folder_name.get())))
                submit.bind('<1>', lambda e: print('running'))
                submit.grid(row=6, column=0)

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
    main().main()


