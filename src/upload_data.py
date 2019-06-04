"""
Created on 5/12/19
@author: Yucheng Zhu
"""


import boto3
import yaml
import argparse
import logging

logger = logging.getLogger(__name__)


s3 = boto3.client("s3")


def upload_data(args):
    """upload data file to a specific S3 path

    :param args: parsed argument input
    :return:
    """

    s3.upload_file(args.input_file_path,args.bucket_name,args.output_file_path)


# def run_upload(arg):
#
#     with open(args.config, "r") as f:
#         config = yaml.load(f)
#
#     run = config['upload_data']–
#
#     upload_data = (**run['upload_data'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload data to S3")
    #
    # parser.add_argument('--config', default='config/model_config.yml',
    #                     help='path to yaml file with configurations')
    # parser.add_argument('--input', default=None, help="Path to input to post process")
    #
    # args = parser.parse_args()
    # run_upload(args)

    # add argument
    parser.add_argument("--input_file_path", help="local path for uploaded file")
    parser.add_argument("--bucket_name", help="s3 bucket name")
    parser.add_argument("--output_file_path", help="output path for uploaded file")

    args = parser.parse_args()
    upload_data(args)



#e.g. python src/upload_data.py --input_file_path "data/red.csv" --bucket_name "yzhu-project" --output_file_path "r2.csv"