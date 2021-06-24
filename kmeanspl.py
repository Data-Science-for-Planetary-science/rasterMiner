from tkinter import *
from tkinter import filedialog
# import re
# import ast 
from tkinter import messagebox
# import final_code
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
        k=textBox3.get()
        outputfile=textBox1.get()+'/result_K-means++_'+str(k)+'_'+str(maxiterations)+'.csv'
        otc=textBox1.get()+'/centers_K-means++_'+str(k)+'_'+str(maxiterations)+'.csv'
        if(inputfile=='' or outputfile=='' or maxiterations=='' or k==''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            of=open(outputfile, 'w')
            f=open(inputfile,'r')
            oc=open(otc,'w')
            data=[]
            pts=[]
            for i in f:
                j=i.strip('\n').split(',')
                for r in range(1,len(j)):
                    j[r]=float(j[r])
                pts.append(j[0])
                data.append(j[1:])
            X = np.array(data)
            kmeans = KMeans(n_clusters=int(k),init='k-means++',max_iter=int(maxiterations)).fit(X)
            WSSE=kmeans.inertia_
            wr = kmeans.labels_
            for p in range(len(X)):
                # print(p)
                # wr=kmeans.predict(p)
                stri= pts[p]+','+str(wr[p])+'\n'
                of.write(stri)
            of.close()
            co=1
            for j in kmeans.cluster_centers_:
                text='Center-'+str(co)
                for d in j:
                    text+=','+str(d)
                # print(text)
                text+='\n'
                oc.write(text)
                co+=1
            oc.close()
        my_label4=Label(root,text='WSSE:')
        my_label4.grid(column=0, row=10)
        my_label5=Label(root,text=str(WSSE))
        my_label5.grid(column=1, row=10)
    root=Tk()
    root.title('k-means++')
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
    my_label3=Label(root,text='Enter k value:')
    my_label3.grid(column=0, row=3)
    textBox3=Entry(root,textvariable='')
    textBox3.grid(column=1,row=3)
    submit=Button(root,text="submit",command=submit1)
    submit.grid(column=1,row=7)
    back=Button(root,text="Back",command=back)
    back.grid(column=2,row=7)
    root.mainloop()
