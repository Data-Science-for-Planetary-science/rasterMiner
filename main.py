import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

inputRasterFolder=''
outputFolder = ''
def UploadAction1(event=None):
    # filename = filedialog.askopenfilename()
    filename = filedialog.askdirectory()
    print('Selected:', filename)
    inputRasterFolder = filename

def UploadAction2(event=None):
    # filename = filedialog.askopenfilename()
    filename = filedialog.askdirectory()
    print('Selected:', filename)
    outputFolder = filename

root = tk.Tk()
root.title("rasterMiner: Discovering Knowledge Hidden in Raster Images")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Convert Raster Files to CSV File')
tabControl.add(tab2, text='Pattern Mining')
tabControl.add(tab3, text='Clustering')
tabControl.add(tab4, text='Classification')
tabControl.add(tab5, text='Prediction')
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1, text='Select the folder containing raster files:').grid(column=0, row=0, padx=30, pady=30,sticky = 'W')
ttk.Label(tab1, text='Enter the file extension of the raster files:').grid(column=0, row=1, padx=30, pady=30,sticky = 'W')
ttk.Label(tab1, text='Select output folder:').grid(column=0, row=2, padx=30, pady=30,sticky = 'W')

e1 = tk.Entry(tab1)
e2 = tk.Entry(tab1)
e3 = tk.Entry(tab1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e2.grid(row=2, column=1)


button1 = tk.Button(tab1, text='Open', command=UploadAction1)
button1.grid(row=0,column=2)
e1 = tk.Entry(tab1,textvariable=inputRasterFolder);

button2 = tk.Button(tab1, text='Open', command=UploadAction2)
button2.grid(row=2,column=2)
e3 = tk.Entry(tab1,textvariable=outputFolder);

ttk.Label(tab2, text='Input csv file:').grid(column=0, row=0, padx=30, pady=30)


root.mainloop()