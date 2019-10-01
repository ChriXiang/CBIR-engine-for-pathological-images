# -*- coding: utf-8 -*-
from vgg16_keras import VGG

import numpy as np
import h5py

def execution(query_path, index_file = 'feature.h5', database_path = 'database'):
# read in indexed images' feature vectors and corresponding image names

	h5f = h5py.File(index_file,'r')
	feats = h5f['dataset_1'][:]
	imgNames = h5f['dataset_2'][:]
	h5f.close()
	        
	model = VGG()
	
	queryVec = model.extract_feature(query_path)

	scores = np.array([np.sum(abs(feature - queryVec)) for feature in feats ])
	#scores = np.dot(queryVec, feats.T)

	rank_ID = np.argsort(scores)#[::-1]
	rank_score = scores[rank_ID]

	# number of top retrieved images to show
	maxres = 4
	imlist = [str(imgNames[index],'utf-8') for index in rank_ID[0:maxres]]

	return imlist
