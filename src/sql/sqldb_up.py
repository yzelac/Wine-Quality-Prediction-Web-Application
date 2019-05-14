"""
Created on 5/10/19
@author: Yucheng Zhu
"""

import os
import sys
import logging


from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, MetaData, create_engine, Text, Floa
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

    index  = Column(Integer, primary_key=True, unique=True, nullable=False)
    fixed_acidity = Column(Float, unique=False, nullable=False)
    volatile_acidity = Column(Float, unique=False, nullable=False)
    citric_acid = Column(Float, unique=False, nullable=False)
    residual_sugar= Column(Float, unique=False, nullable=False)
    chlorides   = Column(Float, unique=False, nullable=False)
    free_sulfur = Column(Float, unique=False, nullable=False)
    dioxid = Column(Float, unique=False, nullable=False)
    total_sulfur = Column(Float, unique=False, nullable=False)
    dioxide    = Column(Float, unique=False, nullable=False)
    density = Column(Float, unique=False, nullable=False)
    pH  = Column(Float, unique=False, nullable=False)
    sulphates   = Column(Float, unique=False, nullable=False)
    alcohol = Column(Float, unique=False, nullable=False)
    quality = Column(Integer, unique=False, nullable=False)
    prediction = Column(String(100), unique=False, nullable=True)

    def __repr__(self):
        predict_repr = "<Wine_Predict(index='%d', prediction='%s')>"
        return predict_repr % (self.index, self.prediction)





# set up sqlite connection
engine_string = 'sqlite:////tmp/wine.db'
engine = sql.create_engine(engine_string)
# create the tracks table
Base.metadata.create_all(engine)
# set up looging config
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__file__)


