import sys
import os.path
import argparse
import boto3
import logging
import pandas as pd
import numpy as np
import yaml
import pickle
import pytest



import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.score_model import *
from src.load_data import *
from src.train_model import *
from src.generate_feature import *
from src.evaluate_model import *
from src.helpers import Timer


logger = logging.getLogger(__name__)

def test_load_data():
    """

    :return:
    """
    print("test_load_data")

    path = "data/red.csv"
    df = pd.read_csv(path, sep=',', index_col=0)

    assert df.equals(load_data(path))

def test_transform_y():
    """

    :return:
    """
    print("test_transform_y")

    # load sample test data
    path = "data/red.csv"
    data = pd.read_csv(path, sep=',', index_col=0)

    bins = (2, 6.5, 8)
    data['quality'] = pd.cut(data['quality'], bins = bins, labels = ['bad', 'good'])
    label_quality = LabelEncoder()
    data['quality'] = label_quality.fit_transform(data['quality'])

    # raise AssertionError if output values do not match element-wise
    assert data.equals(transform_y(red=data, left=2, mid=6.5, right=8))

def test_choose_features():
    print("test_choose_features")

    path = "data/red.csv"
    data = pd.read_csv(path, sep=',', index_col=0)

    bins = (2, 6.5, 8)
    data['quality'] = pd.cut(data['quality'], bins = bins, labels = ['bad', 'good'])
    label_quality = LabelEncoder()
    data['quality'] = label_quality.fit_transform(data['quality'])

    X = data.drop('quality', axis=1)
    assert X.equals(choose_features(data))


def test_get_target():
    print("test_get_target")

    path = "data/red.csv"
    data = pd.read_csv(path, sep=',', index_col=0)

    bins = (2, 6.5, 8)
    data['quality'] = pd.cut(data['quality'], bins = bins, labels = ['bad', 'good'])
    label_quality = LabelEncoder()
    data['quality'] = label_quality.fit_transform(data['quality'])

    y = data['quality']

    assert y.equals(get_target(data))

def test_split_data():

    print("test_split_data")

    path = "data/red.csv"
    data = pd.read_csv(path, sep=',', index_col=0)

    bins = (2, 6.5, 8)
    data['quality'] = pd.cut(data['quality'], bins = bins, labels = ['bad', 'good'])
    label_quality = LabelEncoder()
    data['quality'] = label_quality.fit_transform(data['quality'])

    X = data.drop('quality', axis=1)
    y = data['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state =111)

    X_train1, X_test1, y_train1, y_test1 = split_data(X, y, test_size = 0.2 , seed =111)


    assert X_train.equals(X_train1)
    assert X_test.equals(X_test1)
    assert y_train.equals(y_train1)
    assert y_test.equals(y_test1)


def test_random_forest_type ():

    print("test_random_forest_type")

    path = "data/red.csv"
    data = pd.read_csv(path, sep=',', index_col=0)

    bins = (2, 6.5, 8)
    data['quality'] = pd.cut(data['quality'], bins = bins, labels = ['bad', 'good'])
    label_quality = LabelEncoder()
    data['quality'] = label_quality.fit_transform(data['quality'])
    X = data.drop('quality', axis=1)
    y = data['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state =111)

    model = random_forest(X_train, X_test, y_train, y_test, estimators = 200, path_to_model = None)
    model.fit(X_train, y_train)

    assert str(type(model)) == "<class 'sklearn.ensemble.forest.RandomForestClassifier'>"


def test_score_model():

    print("test_score_model")

    path = "data/red.csv"
    data = pd.read_csv(path, sep=',', index_col=0)

    bins = (2, 6.5, 8)
    data['quality'] = pd.cut(data['quality'], bins = bins, labels = ['bad', 'good'])
    label_quality = LabelEncoder()
    data['quality'] = label_quality.fit_transform(data['quality'])
    X = data.drop('quality', axis=1)
    y = data['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state =111)

    model = RandomForestClassifier(n_estimators=200, random_state= 111, verbose=0)
    model.fit(X_train, y_train)
    pred_rfc = model.predict(X_test)

    y_predicted = pd.DataFrame(pred_rfc)
    y_predicted.columns = ['y_pred']

    assert y_predicted.equals(score_model(X_test,
                                          y_test,
                                          path_to_model = "models/rf_model.pkl",
                                          path_to_predicted=None))

def test_evaluate_model():

    print("test_evaluate_model")
    path = "data/red.csv"
    data = pd.read_csv(path, sep=',', index_col=0)

    bins = (2, 6.5, 8)
    data['quality'] = pd.cut(data['quality'], bins=bins, labels=['bad', 'good'])
    label_quality = LabelEncoder()
    data['quality'] = label_quality.fit_transform(data['quality'])
    X = data.drop('quality', axis=1)
    y = data['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=111)

    model = RandomForestClassifier(n_estimators=200, random_state=111, verbose=0)
    model.fit(X_train, y_train)
    pred_rfc = model.predict(X_test)

    y_predicted = pd.DataFrame(pred_rfc)
    y_predicted.columns = ['y_pred']
    pred_rfc = y_predicted['y_pred'].values


    assert (pred_rfc == evaluate_model(y_test, path_to_model="models/rf_model.pkl", path_to_predicted="data/y_predicted.csv")).all()


if __name__ == "__main__":
    test_load_data()
    test_transform_y()
    test_choose_features()
    test_get_target()
    test_split_data()
    test_random_forest_type()
    test_score_model()
    test_evaluate_model()
    print("All unit tests passed!!!")