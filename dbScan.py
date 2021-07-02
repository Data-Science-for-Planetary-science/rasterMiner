from tkinter import *
from tkinter import filedialog
# import re
# import ast 
from tkinter import messagebox
# import final_code
import mplcursors
import startapp
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
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
        epsi=textBox2.get()
        minpts=textBox3.get()
        outputfile=textBox1.get()+'/result_DBScan_'+str(epsi)+'_'+str(minpts)+'.csv'
        if(inputfile=='' or outputfile=='' or epsi=='' or minpts==''):
            messagebox.showerror("Error", "Please fill the fields properly")
        else:
            of=open(outputfile, 'w')
            f=open(inputfile,'r')
            data=[]
            # data1=[]
            pts=[]
            for i in f:
                j=i.strip('\n').split(',')
                for r in range(1,len(j)):
                    j[r]=float(j[r])
                pts.append(j[0])
                data.append(j[1:])
            # X = np.array(data)
            z=np.array(data)
            # print(z)
            q=z.copy()
            X = StandardScaler().fit_transform(z)
            # print(z)

            dbs = DBSCAN(eps=float(epsi), min_samples=int(minpts)).fit(X)
            labels = dbs.labels_
            n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
            n_noise_ = list(labels).count(-1)
            for p in range(len(z)):
                stri=pts[p]+','+str(labels[p])+'\n'
                of.write(stri)
            of.close()
        # print("output generated")
        my_label4=Label(root,text='Estimated number of clusters:')
        my_label4.grid(column=0, row=10)
        my_label5=Label(root,text=str(n_clusters_))
        my_label5.grid(column=1, row=10)
        my_label6=Label(root,text='Estimated number of noise points:')
        my_label6.grid(column=0, row=11)
        my_label7=Label(root,text=str(n_noise_))
        my_label7.grid(column=1, row=11)
        if n_clusters_>1:
            my_label8=Label(root,text='Silhouette Coefficient:')
            my_label8.grid(column=0, row=12)
            my_label9=Label(root,text=str(metrics.silhouette_score(X, labels)))
            my_label9.grid(column=1, row=12)
    root=Tk()
    root.title('DB-Scan')
    v = IntVar(root, 1) 
    root.minsize(600,400)
    my_label1=Label(root,text='Select the input file:')
    my_label1.grid(column=0, row=0) 
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
    my_label3=Label(root,text='Enter Epsilon value(ε):')
    my_label3.grid(column=0, row=2)
    textBox2=Entry(root,textvariable='')
    textBox2.grid(column=1,row=2)
    my_label3=Label(root,text='Enter Min pts:')
    my_label3.grid(column=0, row=3)
    textBox3=Entry(root,textvariable='')
    textBox3.grid(column=1,row=3)
    submit=Button(root,text="submit",command=submit1)
    submit.grid(column=1,row=7)
    back=Button(root,text="Back",command=back)
    back.grid(column=2,row=7)
    root.mainloop()
