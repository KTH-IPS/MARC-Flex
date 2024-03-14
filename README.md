# MARC-Flex Dataset
<p align="center">
 <img src="/media/marc-flex_full_logo.png" width="350" height="350">
 </p>

## Introduction
This is the Python scripts repository for MARC-Flex Dataset.

## Pipeline
The whole pipeline 

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