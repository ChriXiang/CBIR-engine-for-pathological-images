# -*- coding: utf-8 -*-
import os
import h5py
import numpy as np
import argparse
from vgg16_keras import VGG
import sys

ap = argparse.ArgumentParser()
ap.add_argument("-database", required = True,
	help = "Path to database")
ap.add_argument("-index", required = True,
	help = "Name of index file")
args = vars(ap.parse_args())

def get_imlist(db_path, index_path):
    if os.path.exists(index_path) is False:
        return [os.path.join(db_path,each) for each in os.listdir(db_path) if each.endswith('.jpg')]

    img_list = []
    h5f = h5py.File(index_path,'r')
    imgNames = h5f['dataset_2'][:]
    str_names = str(imgNames, encoding="utf-8")
    for each in os.listdir(db_path):
        if each not in str_names and each.endswith('.jpg'):
            img_list.append(os.path.join(db_path,each))
    h5f.close()

    return img_list


if __name__ == "__main__":

    db = args["database"]
    output = args["index"]

    img_list = get_imlist(db, output)

    if len(img_list) == 0:
        print("No change has been detected in the given database, system terminates.")
        exit()

    print("*** FEATURE EXTRACTION STARTS ***")
    
    feats = []
    names = []
    model = VGG()

    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feature(img_path)
        img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_name)
        sys.stdout.write("\r extracting feature from database %d / %d." %((i+1), len(img_list)))
        #print("extracting feature from database %d / %d." %((i+1), len(img_list)))

    feats = np.array(feats)

    print("*** FEATURE EXTRACTION SUCCEDED ***")
    print("*** FEATURE WRITING STARTS ***")

    if os.path.exists(output):
        h5f = h5py.File(output, 'r')
        sub_feats = h5f['dataset_1'][:]
        sub_names = h5f['dataset_2'][:]
        sub_feats = np.array(sub_feats)
        sub_names = np.array(sub_names)
        feats = np.append(feats, sub_feats)
        names = np.append(names, sub_names)
        h5f.close()

    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_1', data = feats)
    h5f.create_dataset('dataset_2', data = np.string_(names))
    h5f.close()

    print("*** FEATURE WRITING SUCCEDED ***")

