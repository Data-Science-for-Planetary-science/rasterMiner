**[CLICK HERE](index.html)** to access the manual.

## Installation in Ubuntu

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

       python rasterMiner/rasterMiner/GUI/main.py