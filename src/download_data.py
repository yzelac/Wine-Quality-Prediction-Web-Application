"""
Created on 5/12/19
@author: Yucheng Zhu
"""
import argparse
import pandas as pd
import logging
import yaml

logger = logging.getLogger(__name__)


def download_data(url,save_path):
    """Download data from a public S3 to certain path

    :param read_path: path to data source
    :param save_path: save path
    :return: None
    """

    df = pd.read_csv(url, sep=';')
    df.to_csv(save_path)


def downloading (arg):
    """Run functions defined

    :param arg: parsed argument input
    :return: None
    """
    with open(args.config, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    run = config['download_data']

    download_data(**run['download_data'])


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="Download Data from S3 to Local")

    parser.add_argument('--config', default='config/model_config.yml',
                        help='path to yaml file with configurations')
    parser.add_argument('--input', default=None, help="Path to input to post process")
    args = parser.parse_args()

    downloading(args)

    # url = 'http://s3.us-east-2.amazonaws.com/wine-source/winequality-red.csv'
    # download_data(url,'data/red.csv')