# rasterMiner

   This open-source software empowers the users with the set of tools to discover knowledge hidden in raster datasets.  
   This software is distributed under GNU-V3 liscense.
   
   rasterMiner currently supports the following knowledge discovery tasks:
   1. Data preprocessing and Nan value handling
   2. Pattern mining
   3. Clustering
   4. Classification
   5. Prediction (yet to be developed)
   
   The user manual for rasterMiner is available at  https://udayrage.github.io/rasterMiner/
## Ways to execute rasterMiner

   rasterMiner can be executed in any one of the following ways:
   
   1. Terminal-based execution
   2. GUI-based execution
   3. As a Python-library in QGIS, ARCGIS, ENVI, and in conventional python programs. (Under development) 
    
    
## Installation 

### Installation using Anaconda (Any operating system)
1. Install and set up Anaconda. URL:   https://linuxize.com/post/how-to-install-anaconda-on-centos-7
2. Create a virtual environment using conda.

       conda create --name rasterMiner
     
3. Enter into virtual environment. 

       conda activate rasterMiner
     
4. Install python using Conda.  

       conda install python
 
5. Install GDAL using Conda

       conda install gdal
         
6. Install the following libraries using PIP 

       pip install mplcursors matplotlib sklearn pandas pami
         
7. Clone the rasterMiner repository using git clone command

       git clone https://github.com/udayRage/rasterMiner.git

8. Execute the rasterMiner code by typing the following command

       python rasterMiner/rasterMiner/GUI/rasterMiner.py
         
### Installation in MacOS

1. Install Homebrew in Mac
2. Install GDAL using brew
  
       sudo brew install gdal
       
3. Install Git clone

       brew install git

4. Install the following libraries using PIP 

       pip install mplcursors matplotlib sklearn pandas pami
       
       
5. Clone the rasterMiner

       git clone https://github.com/udayRage/rasterMiner.git

6. Execute the rasterMiner code by typing the following command

       python rasterMiner/rasterMiner/GUI/rasterMiner.py
       
### Installation in Ubuntu

1. Execute the following four steps in the presented order:

       sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
       sudo apt-get update
       sudo apt-get gdal-bin
       sudo apt-get install git
    
2. Install any Python 3 version

       sudo apt-get install python

3. Install the following libraries using PIP 

       pip install mplcursors matplotlib sklearn pandas pami
       
       
4. Clone the rasterMiner

       git clone https://github.com/udayRage/rasterMiner.git

5. Execute the rasterMiner code by typing the following command

       python rasterMiner/rasterMiner/GUI/rasterMiner.py
       
       
### Execution of rasterMiner
       
1. Execute the following command to open the GUI:

       python rasterMiner/rasterMiner/GUI/rasterMiner.py
