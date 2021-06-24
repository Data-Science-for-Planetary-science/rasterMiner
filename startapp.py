from tkinter import *
from tkinter import filedialog
# import re
# import ast 
from tkinter import messagebox
import kmeans
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
import dbScan
import elbowKmeans
import elbowKmeansPl
import kmeanspl
import fuzzc
def  main():
	def gotoalgo(master):
		master.destroy()
		entered_algo = variable.get()
		if entered_algo=='k-Means':
			kmeans.main()
		else:
			if entered_algo=='k-Means++':
				kmeanspl.main()
			else:
				if entered_algo=='DB-scan':
					dbScan.main()
				else:
					if entered_algo=='elbow k-Means':
						elbowKmeans.main()
					else:
						if entered_algo=='elbow k-Means++':
							elbowKmeansPl.main()
						else:
							if entered_algo=='Fuzzy C-Means':
								fuzzc.main()


	OPTIONS=['elbow k-Means','elbow k-Means++','k-Means','k-Means++','Fuzzy C-Means','DB-scan']
	master = Tk()
	master.title('Clustering App')
	master.geometry("400x200") #
	variable = StringVar(master)
	variable.set(OPTIONS[0]) # default value
	label1=Label(master,text='Select the Algoritham:')
	label1.grid(column=1, row=1)
	w = OptionMenu(master, variable, *OPTIONS)
	w.grid(column=3, row=1)
	submit=Button(master,text="submit",command=lambda master=master:gotoalgo(master))
	submit.grid(column=2,row=3)
	master.mainloop()
if __name__ == "__main__": 
    main()