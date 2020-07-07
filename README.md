# Skincancer_Categorization

This is the project to categorize the skin cancer on the basis of deep learning.

## 1. Object
We try to compare the skin cancer images into benign and malignant, in terms of size, textures, perimeter and some other scores.
In skin cancer doctors are mainly interested in these features: asymmetry,  border,  color, diameter. We will also extract regions of different intensity and compute their area relative to the skin lesion area. 

## 2. Skin cancer classification
There are three main types of skin cancer: basal-cell skin cancer (basal-cell carcinoma) (BCC), squamous-cell skin cancer (squamous-cell carcinoma) (SCC) and malignant melanoma.    BCC and SCC is non-melanoma, and the later one is melanoma, which cause the fetal result.

## 3. Project Planning and method flow
### 1. Acquiring the diagnotic datasets (Done)
...dermoscopy images from isic-archive
### 2. Pre-processing (Done)
masking, image resizing, filtering, color space conversions,hair detection and removal, reduction of noise and artifacts
・Converting the RGB channel into suitable color space for analysis(that is CIEL*a*b [50,51], CIEL*u*v [172,273] and HSV [172,200,273] colorspaces.)
・illumination adjustment : adaptive bilateral decomposition and polynomial curve fitting was adopted 
・hair removal: gaussian filter - isotropic filter, empty spots filled with mean of edge pixel values
… Color normalization or  illumination  with  colour  constancy  algorithm(same brightness)
### 3. Typical segmentation methods (Done)
… Watershed, morphological gradients to detect the contours, we use the opencv platform to segment ROIs of skin lesion
### 4. Calculation of ROIs (Done)
… Perimeters, homogeneous, area, color
### 5. Contruction of deep learning algorithm/ Machine learning algorithm (Done)
…. Scikit learn ( library of algorithm for python) for texture description to categolize the skin cancer.
-texture descriptor, statistical descriptor, classifier
### 6. Evaluation of our results (Done)
…. medical score of seriousness the disease (class 0-5),, accuracy, confusion table, grand truth)
https://www.ritchieng.com/machine-learning-evaluate-classification-model/
https://towardsdatascience.com/model-evaluation-techniques-for-classification-models-eac30092c38b
### 7. Writing the reports
... We're supposed to write down the report(4 pages) of mini project up until end of January.
