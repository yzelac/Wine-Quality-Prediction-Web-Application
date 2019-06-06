"""
Created on 5/12/19
@author: Yucheng Zhu
"""

import sys
import os.path
import argparse
import boto3
import logging
import pandas as pd
import numpy as np
import yaml
import pickle


import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.load_data import *
from src.generate_feature import *
from src.helpers import Timer


logger = logging.getLogger(__name__)

s3 = boto3.client("s3")


def split_data(X, y, test_size, seed):
    """
    :param X:
    :param y:
    :param test_size:
    :param seed:
    :return:
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size , random_state =seed)

    path = os.getcwd()
    outdir = path + '/data/train'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    pd.DataFrame(X_train).to_csv('data/train/X_train.csv')
    pd.DataFrame(y_train).to_csv('data/train/y_train.csv')

    outdir = path + '/data/test/'

    if not os.path.exists(outdir):
        os.mkdir(outdir)

    pd.DataFrame(X_test).to_csv('data/test/X_test.csv')
    pd.DataFrame(y_test).to_csv('data/test/y_test.csv')

    return X_train, X_test, y_train, y_test


def random_forest (X_train, X_test, y_train, y_test, estimators, path_to_model):
    """

    :param X_train:
    :param X_test:
    :param y_train:
    :param y_test:
    :param estimators:
    :return:
    """
    # sc = StandardScaler()
    # X_train = sc.fit_transform(X_train)
    # X_test = sc.fit_transform(X_test)

    with Timer("model training", logger) as t:
        rfc = RandomForestClassifier(n_estimators=estimators, random_state= 111)
        rfc.fit(X_train, y_train)
    print(rfc)

    if path_to_model is not None:
        path = os.getcwd()
        outdir = path + '/models/'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        # path_to_model = 'models/rf_model.pkl'
        with open(path_to_model, "wb") as f:
            pickle.dump(rfc, f)
        logger.info("Trained model object saved to %s", path_to_model)

    return rfc


def training(arg):
    with open(args.config, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    red = load_data(**config['load_data']['load_data'])
    df = transform_y (red, **config['generate_feature']['transform_y'])
    X = choose_features(df)
    y = get_target(df)

    X_train, X_test, y_train, y_test = split_data(X, y, **config['train_model']['split_data'])

    random_forest(X_train, X_test, y_train, y_test, **config['train_model']['training'])



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Load data")
    parser.add_argument('--config', default='config/model_config.yml',
                        help='path to yaml file with configurations')
    parser.add_argument('--input', default=None, help="Path to input to post process")
    args = parser.parse_args()
    training(args)
