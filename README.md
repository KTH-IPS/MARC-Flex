# MARC-Flex Dataset
 ![MARC-Flex Dataset](/media/marc-flex_full_logo.png)

## Introduction
This is the Python scripts repository for MARC-Flex Dataset.

## Folders
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

    - **dict.py**

        This script is 
    - **merge.py**

        This script is 
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