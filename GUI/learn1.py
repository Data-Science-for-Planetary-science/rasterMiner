from tkinter import *
from tkinter import ttk

#Make the root widget
root = Tk()

#Make the first notebook
program = ttk.Notebook(root) #Create the program notebook
program.pack()


mainLabels=['Preprocessing', 'Pattern mining', 'Clustering']

for label in mainLabels:
    term = Frame(program, height=800,width=800)
    program.add(term, text=label)
    nbName = label
    nbName = ttk.Notebook(term)
    nbName.pack(expand=True,side='top')

    if label == 'Preprocessing':
        subLabels =['Multi-band images', 'Single-band temporal images']
        for subLabel in subLabels:
            if subLabel == 'Multi-band images':
                subLabelFrame = Frame(nbName, height=800,width=800,)
                nbName.add(subLabelFrame , text=subLabel)

                ttk.Label(subLabelFrame, text='Select the folder containing raster files:').grid(column=0, row=0, padx=30, pady=30, sticky='W')
            elif subLabel == 'Single-band temporal images':
               print('To be written')

    elif label == 'Pattern mining':
        subLabels = ['Convert TSV to Database', 'Pattern mining']
        for subLabel in subLabels:
            subLabelFrame = Frame(nbName, height=800,width=800)
            nbName.add(subLabelFrame, text=subLabel)
    elif label == 'Clustering':
        subLabels = ['Parameter tuning', 'Algorithms']
        for subLabel in subLabels:
            subLabelFrame = Frame(nbName, height=800,width=800)
            nbName.add(subLabelFrame, text=subLabel)

    else:
        for a in range(1, 4):
            courseName = "Course" + str(a)  # concatenate coursename(will come from dict)
            course = Frame(nbName)  # Create a course frame for the newly created term frame for each iter
            nbName.add(course, text=courseName)  # add the course frame to the new notebook



root.mainloop()