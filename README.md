# rasterMiner

   Our software provides a set of tools to discover knowledge hidden in raster datasets.  
   It is an open source software distributed under GNU-V3 liscense.
   rasterMiner currently supports the following knowledge discovery tasks:
   
   1. Data preprocessing and Nan value handling
   2. Pattern mining
   3. Clustering
   4. Classification
   5. Prediction (yet to be developed)
   
## Ways to execute rasterMiner

   rasterMiner can be executed in any one of the following ways:
   
   1. Terminal-based execution
   2. GUI-based execution
   3. As a Python-library in QGIS, ARCGIS, ENVI, and in conventional python programs. 
   
## Installation using Anaconda.

1. Install and set up Anaconda. URL:   https://linuxize.com/post/how-to-install-anaconda-on-centos-7
2. Create a virtual environment using conda.

       conda create --name rasterMiner
     
3. Enter into virtual environment. 

       conda activate rasterMiner
     
4. Install python using Conda.  

       conda install python
 
5. Install GDAL using Conda

       conda install gdal
         
6. Open the terminal in pycharm, and execute the following command

       pip install mplcursors matplotlib sklearn pandas pami
         
7. Clone the rasterMiner repository using git clone command

       git clone https://github.com/udayRage/rasterMiner.git

8. Execute the rasterMiner code by typing the following command

       python rasterMiner/rasterMiner/GUI/main.py
          

## Usage of Anaconda

1. Open terminal and enter into rasterMiner virtual environment. 

       conda activate rasterMiner
       
2. Execute the rasterMiner code by typing the following command

       python rasterMiner/rasterMiner/GUI/main.py

          
