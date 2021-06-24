from tkinter import *
from tkinter import filedialog
import re
import ast 
from tkinter import messagebox
# import final_code
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
import mplcursors
import startapp
from sklearn.cluster import KMeans
import numpy as np


def main():
    def openFile():
        root.filename1=filedialog.askopenfilename(initialdir="~/Desktop",title="select a file",filetypes=(("csv","*.csv"),("All Files","*.*")))
        textBox.delete(0,END)
        textBox.insert(0,root.filename1)
    def pathtooutfile():
        root.filename2=filedialog.askdirectory(initialdir="~/Desktop")
        textBox1.delete(0,END)
        textBox1.insert(0,root.filename2)
    def back():
        root.destroy()
        startapp.main()
    def submit1():
        inputfile=textBox.get()
        maxiterations=textBox2.get()
        mink=textBox3.get()
        maxk=textBox4.get()
        inc=textBox5.get()
        outputfile=textBox1.get()+'/result_elbowKmeans++_'+str(mink)+'_to_'+str(maxk)+'_by_'+str(inc)+'.csv'
        if(inputfile=='' or outputfile=='' or maxiterations=='' or mink=='' or maxk=='' or inc==''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            of=open(outputfile, 'w')
            f=open(inputfile,'r')
            data=[]
            pts=[]
            for i in f:
                j=i.strip('\n').split(',')
                for r in range(1,len(j)):
                    j[r]=float(j[r])
                pts.append(j[0])
                data.append(j[1:])
            X = np.array(data)
            gx=[]
            gy=[]
            for i in range(int(mink),int(maxk)+1,int(inc)):
                kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=int(maxiterations)).fit(X)
                gy.append(kmeans.inertia_)
                gx.append(i)
                stri= str(i)+','+str(kmeans.inertia_)+'\n'
                of.write(stri)
            of.close()
            root2=Tk()
            root2.title('elbow k-means++')
            f=Figure(figsize=(5,5),dpi=100)
            a=f.add_subplot(111,facecolor='white')
            a.set_title('Elbow KMeans++')
            a.set_xlabel('k value')
            a.set_ylabel('WSSE')
            a.set_xticks(gx)


            a.plot(gx,gy, marker='o',color='k')
            canvas=FigureCanvasTkAgg(f,root2)
            canvas.draw()
            canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=True)
            toolbar=NavigationToolbar2Tk(canvas,root2)
            mplcursors.cursor(a).connect("add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
            canvas._tkcanvas.pack(side=TOP,fill=BOTH,expand=True)
            root2.mainloop()
    root=Tk()
    root.title('elbow k-means++')
    v = IntVar(root, 1) 
    root.minsize(600,400)
    my_label1=Label(root,text='Select the input file:')
    my_label1.grid(column=0, row=0) 
# v = StringVar(root, value=inputfile)
    textBox=Entry(root,textvariable='')
    textBox.grid(column=1,row=0)
    my_btn=Button(root,text="open a file",command=openFile)
    my_btn.grid(column=2,row=0)
    my_label2=Label(root,text='Select the output directory:')
    my_label2.grid(column=0, row=1) 
    textBox1=Entry(root,textvariable='')
    textBox1.grid(column=1,row=1)
    my_btn1=Button(root,text="open a file",command=pathtooutfile)
    my_btn1.grid(column=2,row=1)
    my_label3=Label(root,text='Enter Max iterations value:')
    my_label3.grid(column=0, row=2)
    textBox2=Entry(root,textvariable='')
    textBox2.grid(column=1,row=2)
    my_label3=Label(root,text='Enter min k value:')
    my_label3.grid(column=0, row=3)
    textBox3=Entry(root,textvariable='')
    textBox3.grid(column=1,row=3)
    my_label4=Label(root,text='Enter max k value:')
    my_label4.grid(column=0, row=4)
    textBox4=Entry(root,textvariable='')
    textBox4.grid(column=1,row=4)
    my_label5=Label(root,text='Enter increment value:')
    my_label5.grid(column=0, row=5)
    textBox5=Entry(root,textvariable='')
    textBox5.grid(column=1,row=5)
    submit=Button(root,text="submit",command=submit1)
    submit.grid(column=1,row=9)
    back=Button(root,text="Back",command=back)
    back.grid(column=2,row=9)
    root.mainloop()
