"""
Created on 5/12/19
@author: Yucheng Zhu
"""

import sys
import os
import json
import warnings
import os.path

import argparse
import boto3
import logging
import yaml

import pandas as pd
# import numpy as np

logger = logging.getLogger(__name__)

s3 = boto3.client("s3")


def load_data(path):
    """Load data to a dataframe
    Args:
        path (str): file name.
        
    Returns:
        df (:py:class:`pandas.DataFrame`): Concacted DataFrame
    """
    df = pd.read_csv(path, sep=',', index_col=0)

    return df


def loading(arg):
    """Run defined functions

    :param arg: parsed argument input
    :return:
    """
    with open(args.config, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    run = config['load_data']

    df = load_data(**run['load_data'])
    print(df.head())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load data")

    parser.add_argument('--config', default='config/model_config.yml',
                        help='path to yaml file with configurations')
    parser.add_argument('--input', default=None, help="Path to input to post process")
    args = parser.parse_args()

    loading(args)

    # add argument
    # parser.add_argument("--csv_path", default='data/red.csv', type=str, help="local path of data csv file")
    #
    # args = parser.parse_args()
    # load_data(args.csv_path)
