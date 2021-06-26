```python
from google.colab import drive
drive.mount('/content/gdrive/')
```


```python

```


```python

```


```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array
# load_img 함수: 이미지 불러오기
# img_to_array함수 : 불러온 이미지를 numpy 배열 (ndarray)로 변환
# local에서 사용하려면 Pillow를 설치해야 한다. (pip install Pillow)

# Extract features
import os
import shutil
from os import rename, listdir
from keras.preprocessing.image import ImageDataGenerator
# split data
from sklearn.model_selection import train_test_split
# library import
import re
import random
import xml.etree.ElementTree as et
from PIL import Image
 
import cv2 
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle # 바운딩 박스를 그림

 # import the necessary packages
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from imutils import paths
import matplotlib.pyplot as plt
import argparse

# EfficientNetB0
from tensorflow.keras.applications import EfficientNetB0

# print(tf.__version__)
# print(keras.__version__)
np.random.seed(1)
tf.random.set_seed(1)
```
