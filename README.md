# MARC-Flex Dataset
 ![MARC-Flex Dataset](/media/marc-flex_full_logo.png)

## Introduction
This is the Python scripts repository for MARC-Flex Dataset.

## Folders
 - skeleton generator
    
    This folder contains scripts generating skeleton from video and merging the individual skeleton frames into procedural ones.
 - subdataset generator
    
    This folder contains scripts dividing the training and testing subsets, and the .npy, .pkl files for network training.

## How to use
 - skeleton generator
    - batch_openpose.py
    - dict.py
    - merge.py
    - merge_customdata_asbly.py
    - merge_customdata_dsbly.py
 - subdataset generator
    - divider.py
    - label_gen.py
    - npy_gen.py