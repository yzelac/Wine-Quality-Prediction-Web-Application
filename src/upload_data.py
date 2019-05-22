"""
Created on 5/12/19
@author: Yucheng Zhu
"""


import argparse
import boto3
import logging

logger = logging.getLogger(__name__)


s3 = boto3.client("s3")


def upload_data(args):
	"""upload data file to a specific S3 path
	Args:
		args (src): parsed argument input
	"""
    s3.upload_file(args.input_file_path,args.bucket_name,args.output_file_path)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload data to S3")

    # add argument
    parser.add_argument("--input_file_path", help="local path for uploaded file")
    parser.add_argument("--bucket_name", help="s3 bucket name")
    parser.add_argument("--output_file_path", help="output path for uploaded file")

    args = parser.parse_args()
    upload_data(args)


#e.g. python upload_data.py --input_file_path "data/red.csv" --bucket_name "yzhu-project" --output_file_path "r2.csv"