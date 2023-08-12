# DeepNphos
DeepNphos: A Deep-Learning Architecture for Prediction of N-phosphorylation Sites
## Abstract
Phosphorylation, a common post-translational modification, is essential in regulating cellular activities. It includes O-phosphorylation (e.g., phosphoserine) and N-phosphorylation (e.g., phospho-histidine (pH), phospho-lysine (pK) and phospho-arginine(pR)). Much research has been done on O-phosphorylation, but little has been done on N-phosphorylation. Various algorithms have been developed for predicting O-phosphorylation sites with good performance. However, no model has been constructed to predict the N-phosphorylation sites. In this study, we developed the integrated model, dubbed DeepNphos, to predict N-phosphorylation sites based on thousands of experimentally identified pH, pK and pR sites, respectively. We found that pK was somewhat similar to other lysine modification types. Such similarity could improve the pK prediction performance by integrating the deep-transfer learning strategy into the residual convolutional neural network model. By contrast, pR had little similarity to other arginine modification types, and the deep-transfer learning strategy integration did not affect the pR prediction performance. Since histidine modifications other than pH are limited, we developed the classifier for predicting pH sites directly using the known pH sites. All three classifiers have the Area Under the Curve values around 0.8 for cross-validation and independent test. Overall, DeepNphos is the first classifier for predicting N-phosphorylation sites, accessible at https://github.com/ChangXulinmessi/DeepNPhos. 
## Running environment
DeepNphos is an open-source Python-based toolkit, which operates in the Python environment (Python version 3.6 or above). Prior to installing and running DeepNphos, all the dependencies should be installed in the Python environment, including sys, os, re, PyQt5, qdarkstyle, numpy (1.24.3), pandas (1.5.3), threading, sip, scipy (1.9.3), Bio(1.5.9), tensorflow (2.10.0), random, multiprocessing and time. For convenience, we strongly recommended users to install the Anaconda Python environment in your local computer. The software can be freely downloaded from https://www.anaconda.com/.
## Installation
### Method 
  - Download *DeepNphos* by 
  ```sh
  git clone https://github.com/ChangXulinmessi/DeepNphos
  ```

  - Step 1. Download and install the anaconda platform.
  ```sh  
  Download from: https://www.anaconda.com/products/individual
  ```
  
  - Step 2. Install tensorflow:
  ```sh  
  Please refer to https://www.tensorflow.org/ for tensorflow installation.
  ```
  
  - Step 3. Install python packages:
  ```sh
  pip3 install PyQt5
  pip3 install Bio
  pip3 install ……
 
  ```
  
  - Step 4. Run DeepNphos:
  cd to the *DeepNphos* folder which contains DeepNphos.py and run the ‘ DeepNphos.py’ script as follows:
  ```sh
  python  DeepNphos.py
  ```
