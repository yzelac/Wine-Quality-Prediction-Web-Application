"""
Created on 5/10/19
@author: Yucheng Zhu
"""

import os
import sys
import logging
import logging.config

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql

import config
from helpers import create_connection, get_session
import argparse

logging.config.fileConfig(config.LOGGING_CONFIG)
logger = logging.getLogger('wine-models')

Base = declarative_base()


class Wine_Predict(Base):
    """ Defines the data model for the table `wine`. """

    __tablename__ = 'Wine_Predict'

    index  = Column(Integer, primary_key=True, unique=True, nullable=False)
    fixed_acidity = Column(float, unique=False, nullable=False)
    volatile_acidity = Column(float, unique=False, nullable=False)
    citric_acid = Column(float, unique=False, nullable=False)
    residual_sugar= Column(float, unique=False, nullable=False)
    chlorides   = Column(float, unique=False, nullable=False)
    free_sulfur = Column(float, unique=False, nullable=False)
    dioxid = Column(float, unique=False, nullable=False)
    total_sulfur = Column(float, unique=False, nullable=False)
    dioxide    = Column(float, unique=False, nullable=False)
    density = Column(float, unique=False, nullable=False)
    pH  = Column(float, unique=False, nullable=False)
    sulphates   = Column(float, unique=False, nullable=False)
    alcohol = Column(float, unique=False, nullable=False)
    quality = Column(int, unique=False, nullable=False)
    prediction = Column(String(100), unique=False, nullable=True)

    def __repr__(self):
        predict_repr = "<Wine_Predict(index='%d', prediction='%s')>"
        return predict_repr % (self.index, self.prediction)





def get_engine_string(RDS = False):
    if RDS:
        conn_type = "mysql+pymysql"
        user = os.environ.get("MYSQL_USER")
        password = os.environ.get("MYSQL_PASSWORD")
        host = os.environ.get("MYSQL_HOST")
        port = os.environ.get("MYSQL_PORT")
        DATABASE_NAME = 'mysql-yuchengzhu'
        engine_string = "{}://{}:{}@{}:{}/{}". \
            format(conn_type, user, password, host, port, DATABASE_NAME)
        # print(engine_string)
        logging.debug("engine string: %s"%engine_string)
        return  engine_string
    else:
        return 'sqlite:///Wine_Predict.db'






def create_db(args,engine=None):
    """Creates a database with the data models inherited from `Base` (Tweet and TweetScore).
    Args:
        engine (:py:class:`sqlalchemy.engine.Engine`, default None): SQLAlchemy connection engine.
            If None, `engine_string` must be provided.
        engine_string (`str`, default None): String defining SQLAlchemy connection URI in the form of
            `dialect+driver://username:password@host:port/database`. If None, `engine` must be provided.
    Returns:
        None
    """
    if engine is None:
        RDS = eval(args.RDS)
        logger.info("RDS:%s"%RDS)
        engine = sql.create_engine(get_engine_string(RDS = RDS))

    Base.metadata.create_all(engine)
    logging.info("database created")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create defined tables in database")
    parser.add_argument("--RDS", default="False",help="True if want to create in RDS else None")
    args = parser.parse_args()
    create_db(args)

    