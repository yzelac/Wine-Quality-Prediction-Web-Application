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


import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.load_data import load_data


logger = logging.getLogger(__name__)

# s3 = boto3.client("s3")


def transform_y(red, left, mid, right):
    """Load data to a dataframe
    Args:
        path (str): file name.
        
    Returns:
        df (:py:class:`pandas.DataFrame`): Concacted DataFrame
    """
    
    bins = (left, mid, right)
    red['quality'] = pd.cut(red['quality'], bins = bins, labels = ['bad', 'good'])
    label_quality = LabelEncoder()
    red['quality'] = label_quality.fit_transform(red['quality'])

    return red


def choose_features(df):
    X = df.drop('quality', axis=1)
    return X


def get_target(df):

    y = df['quality']
    return y


def generating(arg):
    with open(args.config, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    red = load_data(**config['load_data']['load_data'])

    df = transform_y (red, **config['generate_feature']['transform_y'])

    print(df.head(10))

    X = choose_features(df)

    y = get_target(df)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load data")

    parser.add_argument('--config', default='config/model_config.yml',
                        help='path to yaml file with configurations')
    parser.add_argument('--input', default=None, help="Path to input to post process")
    args = parser.parse_args()


    generating(args)


