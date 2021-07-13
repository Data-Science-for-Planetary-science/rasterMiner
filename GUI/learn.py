# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog
#
# root = tk.Tk()
# root.title("rasterMiner: Discovering Knowledge Hidden in Raster Images")
# tabControl = ttk.Notebook(root)
#
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
# tab3 = ttk.Frame(tabControl)
# tab4 = ttk.Frame(tabControl)
# tab5 = ttk.Frame(tabControl)
#
# tabControl.add(tab1, text='Convert Raster Files to TSV Files')
# tabControl.add(tab2, text='Pattern Mining')
# tabControl.add(tab3, text='Clustering')
# tabControl.add(tab4, text='Classification')
# tabControl.add(tab5, text='Prediction')
# tabControl.pack(expand=1, fill="both")
#
#
# tabControl11 = ttk.Notebook()
#
# tabControl11.add(tab1, text='Multi-band images')
# tabControl11.add(tab1, text='Single-band temporal images')
# tabControl11.pack(expand=1, fill="both")
#
# root.mainloop()

from tkinter import *
from tkinter import ttk

#Make the root widget
root = Tk()

#Make the first notebook
program = ttk.Notebook(root) #Create the program notebook
program.pack()

#Make the terms frames for the program notebook
for r in range(1,4):
    termName = 'Term'+str(r) #concatenate term name(will come from dict)
    term = Frame(program)   #create frame widget to go in program nb
    program.add(term, text=termName)# add the newly created frame widget to the program notebook
    nbName=termName+'courses'#concatenate notebook name for each iter
    nbName = ttk.Notebook(term)#Create the notebooks to go in each of the terms frames
    nbName.pack()#pack the notebook

    for a in range (1,6):
        courseName = termName+"Course"+str(a)#concatenate coursename(will come from dict)
        course = Frame(nbName) #Create a course frame for the newly created term frame for each iter
        nbName.add(course, text=courseName)#add the course frame to the new notebook

root.mainloop()
