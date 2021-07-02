from raster2xyz.raster2xyz import Raster2xyz

input_raster = "/Users/udaykiranrage/Dropbox/Family Room/ohtakeCluster/testFolder/avg_cube_1000s-7000s_slct_smtcont110303.img"
out_csv = "/Users/udaykiranrage/Dropbox/Family Room/ohtakeCluster/testFolder/out_xyz.csv"

#cmd ='gdal2xyz.py -allbands ' + input_raster + ' ' +out_csv

#print(cmd)
#os.system(cmd)
rtxyz = Raster2xyz()
rtxyz.translate(input_raster, out_csv)
