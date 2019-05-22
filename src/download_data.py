"""
Created on 5/12/19
@author: Yucheng Zhu
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def download_data(read_path,save_path):
	"""Download data from a public S3 to certain path
	Args:
		read_path (str): path to data source
		save_path (str): save path
	"""
    df = pd.read_csv(url,sep=';')
    df.to_csv(save_path)



if __name__ == "__main__":
    url = 'http://s3.us-east-2.amazonaws.com/wine-source/winequality-red.csv'
    download_data(url,'data/red.csv')