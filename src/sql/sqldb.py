"""
Created on 5/10/19
@author: Yucheng Zhu
"""

import os
import sys
import logging


from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, MetaData, create_engine, Text, Float
import sqlalchemy as sql
import pandas as pd

import argparse


logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger('wine-db')

Base = declarative_base()



class Wine_Predict(Base):
    """ Defines the data model for the table `wine`. """

    __tablename__ = 'Wine_Predict'

    fixed_acidity = Column(Float, primary_key=True, unique=False, nullable=False)
    volatile_acidity = Column(Float, primary_key=True, unique=False, nullable=False)
    citric_acid = Column(Float, primary_key=True, unique=False, nullable=False)
    residual_sugar= Column(Float, primary_key=True, unique=False, nullable=False)
    chlorides = Column(Float, primary_key=True, unique=False, nullable=False)
    free_sulfur_dioxide = Column(Float, primary_key=True, unique=False, nullable=False)
    total_sulfur_dioxide = Column(Float, primary_key=True, unique=False, nullable=False)
    density = Column(Float, primary_key=True, unique=False, nullable=False)
    pH = Column(Float, primary_key=True, unique=False, nullable=False)
    sulphates = Column(Float, primary_key=True, unique=False, nullable=False)
    alcohol = Column(Float, primary_key=True,unique=False, nullable=False)
    # quality = Column(Integer, unique=False, nullable=False)
    quality = Column(Integer, unique=False, nullable=True)

    def __repr__(self):
        predict_repr = "<Wine_Predict(fixed_acidity='%f', quality='%d')>"
        return predict_repr % (self.index, self.quality)




# the engine_string format
#engine_string = "{conn_type}://{user}:{password}@{host}:{port}/DATABASE_NAME"
conn_type = "mysql+pymysql"
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
host = os.environ.get("MYSQL_HOST")
port = os.environ.get("MYSQL_PORT")
DATABASE_NAME = 'msia423'
engine_string = "{}://{}:{}@{}:{}/{}".\
format(conn_type, user, password, host, port, DATABASE_NAME)
#print(engine_string)
engine = sql.create_engine(engine_string)
Base.metadata.create_all(engine)


# set up looging config
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)




