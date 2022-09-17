import argparse
import os
import cv2
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
from tensorflow.keras.models import load_model
import keras.backend as K

from sklearn.metrics import roc_auc_score

import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()
parser.add_argument('--testimg', type=str, default='test/')
parser.add_argument('--model', type=str, default='model.h5')
parser.add_argument('--resize', type=int, default=256)  
parser.add_argument('--greyscale', action='store_true')  
parser.add_argument('--rescale', action='store_true')
parser.add_argument('--classes', type=str, nargs='+')
parser.add_argument('--binary', action='store_true')
opt = parser.parse_args()


os.environ["CUDA_VISIBLE_DEVICES"]="-1"    
model = load_model(opt.model)

img = cv2.imread(opt.testimg)

length = opt.resize
img.resize((length,length,3))

img = np.array(img).reshape(1,128,128,3)

if opt.rescale == True:
    img = img /255
    
if opt.greyscale == True:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


results = model.predict(img,verbose=0)

res = []
if opt.binary:
    res.append(results[0][0])
    res.append(1-results[0][0])
else:
    res = results
res = np.array(res)
print(opt.classes[res.argmax()])