# TimeSeriesClassification
While using Datasets folder you must have to cite UCR Time Series Repository
@misc{UCRArchive2018,
        title = {The UCR Time Series Classification Archive},
        author = {Dau, Hoang Anh and Keogh, Eamonn and Kamgar, Kaveh and Yeh, Chin-Chia Michael and Zhu, Yan 
                  and Gharghabi, Shaghayegh and Ratanamahatana, Chotirat Ann and Yanping and Hu, Bing 
                  and Begum, Nurjahan and Bagnall, Anthony and Mueen, Abdullah and Batista, Gustavo, and Hexagon-ML},
        year = {2018},
        month = {October},
        note = {\url{https://www.cs.ucr.edu/~eamonn/time_series_data_2018/}}
    }

How to run the programs

python3.7 filename.py locationofTraindataset locationofTestDataset

input: Dataset TrainData and TestData
output: ClassificatioAccuracy of the dataset

For Instance:

python3.7 fuzzyTSC.py Datasets/BeetleFly_TRAIN.tsv Datasets/BeetleFly_TEST.tsv


output:
Total Accuracy of proposedAlgo is: 75.0
Total Execution time of proposedAlgo is: 0.10213017463684082
Memory of proposedAlgo in MB: 21368.0
