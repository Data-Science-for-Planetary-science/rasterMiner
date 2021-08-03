from runSpatialEclat import *
import sys

"""rSE = runSpatialEclat("/Users/masuyudai/runDataTranspose/Data/spatialData_100.tsv","output1.txt","neighbour1.txt",0.2,">=",4500,50)
rSE.run()"""


rSE = runSpatialEclat(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
rSE.run()
