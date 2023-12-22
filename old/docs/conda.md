**[CLICK HERE](index.html)** to access the manual.

## Installation using Anaconda (Any operating system)
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

       python rasterMiner/rasterMiner/GUI/main.py