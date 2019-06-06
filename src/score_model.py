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
from src.train_model import *
from src.generate_feature import *
from src.helpers import Timer


logger = logging.getLogger(__name__)

s3 = boto3.client("s3")


def score_model (X_test, y_test, path_to_model , path_to_predicted):
    """

    :param y_train:
    :param y_test:
    :param path_to_saved:
    :return:
    """
    with open(path_to_model, "rb") as f:
        model = pickle.load(f)

    # check model type - has to be randomForest
    if str(type(model)) != "<class 'sklearn.ensemble.forest.RandomForestClassifier'>":
        raise TypeError("model used to score must be an Random Forest Classifier")


    # sc = StandardScaler()
    # X_test = sc.fit_transform(X_test)

    with Timer("Scroing model", logger) as t:
        pred_rfc = model.predict(X_test)

    y_predicted = pd.DataFrame(pred_rfc)
    y_predicted.columns = ['y_pred']

    if path_to_predicted is not None:
        # save predicted as csv
        path = os.getcwd()
        outdir = path + '/data/'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        pd.DataFrame(y_predicted).to_csv(path_to_predicted)

    return y_predicted



def scoring(arg):
    with open(args.config, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    red = load_data(**config['load_data']['load_data'])
    df = transform_y (red, **config['generate_feature']['transform_y'])
    X = choose_features(df)
    y = get_target(df)

    X_train, X_test, y_train, y_test = split_data(X, y, **config['train_model']['split_data'])

    random_forest(X_train, X_test, y_train, y_test, **config['train_model']['training'])

    y_predicted = score_model(X_test, y_test,  **config['score_model']['score_model'])
    print(y_predicted.head())



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Load data")
    parser.add_argument('--config', default='config/model_config.yml',
                        help='path to yaml file with configurations')
    parser.add_argument('--input', default=None, help="Path to input to post process")
    args = parser.parse_args()
    scoring(args)
