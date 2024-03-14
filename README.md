# MARC-Flex Dataset
<p align="center">
 <img src="/media/marc-flex_full_logo.png" width="350" height="350">
 </p>

## Introduction
This is the Python scripts repository for MARC-Flex Dataset.

## Pipeline
The whole pipeline is described as follow. If you want to build a new dataset, or enrich this dataset, it is easy to follow this pipeline.
1. Record raw videos with single or multiple camers using scripts in **video recorder**. Raw video frames will be generated at the same time.
2. Clip the raw videos into procedural ones using the anchors. Scripts to clip the video are in **video clipper**.
3. Generate skeleton frames using any skeleton estimator (OpenPose in this dataset), for instance the codes in **skeleton generator**.
4. Merge the skeleton frames into procedural skeketon data using scripts from **skeleton generator**.
5. Build the training and testing subdataset using scripts in **subdataset generator**. X-Sample, X-Subject, and X-Sensor can be used for different research target.

## Folders
 - **video recorder**

    This folder contains scripts
 - **video clipper**

    This folder contains scripts
 - **skeleton generator**
    
    This folder contains scripts generating skeleton from video and merging the individual skeleton frames into procedural ones.
 - **subdataset generator**
    
    This folder contains scripts dividing the training and testing subsets, and the .npy, .pkl files for network training.

## How to use
 - **skeleton generator**
    - **batch_openpose.py**

        This script is used for generating skeleton data from video, no matter raw video or clipped video.
        To use OpenPose as the skeleton estimator, you need to install OpenPose on the computer you are going to use with this script. In this project, we used Openpose 1.6.0 and 1.7.0. There is no specific requirement for the Openpose version.
        In MARC-Flex, we use clipped videos in "procedural video" as the input. The output of this script is saved into "skeleton frames" folder.
    - **dict.py**

        This file contains dictionaries of the procedure names. They will be used in merge_customdata_asbly.py and merge_customdata_dsbly.py.
    - **merge.py**

        This script is the template script for merge_customdata_asbly.py and merge_customdata_dsbly.py. Please refer to them for more details.
    - **merge_customdata_asbly.py**

        This script is 
    - **merge_customdata_dsbly.py**

        This script is 
 - **subdataset generator**
    - **divider.py**

        This script is 
    - **label_gen.py**

        This script is 
    - **npy_gen.py**

        This script is 