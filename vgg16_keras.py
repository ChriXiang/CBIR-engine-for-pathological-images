# -*- coding: utf-8 -*-
import numpy as np
import keras
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing import image

import math
#from numpy import linalg as LA
class VGG:
    def __init__(self):
        keras.backend.clear_session()
        self.input_shape = (512, 512, 3)
        self.vgg = VGG16(weights = 'imagenet', input_shape = (self.input_shape[0], self.input_shape[1], self.input_shape[2]), pooling = 'max', include_top = False)

    def extract_feature(self, img_path):
        img = image.load_img(img_path, target_size=(self.input_shape[0], self.input_shape[1]))
        img = image.img_to_array(img)
        
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        feature = self.vgg.predict(img)
        
        #feature shape (1,512)
        norm = math.sqrt(sum(feature[0]**2)) #LA.norm(feature[0], ord=2, axis=None, keepdims=False)
        norm_feat = feature[0]/norm

        return norm_feat
