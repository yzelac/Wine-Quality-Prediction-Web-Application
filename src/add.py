"""
Created on 5/12/19

@author: Yucheng Zhu

"""
import os
import sys
import logging
import pandas as pd

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sql

import argparse

logging.basicConfig(level=logging.DEBUG, filename="logfile_db.log", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger(__file__)

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




def get_engine_string(conn_type="mysql+pymysql", DATABASE_NAME='msia423'):
    """Get database engine path.

    Args:
        conn_tyep (str): Name of sql connection.
        DATABASE_NAME (str): Name of the database to be used.

    Returns:
        engine_string (str): String defining SQLAlchemy connection URI.

    """

    user = os.environ.get("MYSQL_USER")
    password = os.environ.get("MYSQL_PASSWORD")
    host = os.environ.get("MYSQL_HOST")
    port = os.environ.get("MYSQL_PORT")

    engine_string = "{}://{}:{}@{}:{}/{}".format(conn_type, user, password, host, port, DATABASE_NAME)

    logging.debug("engine string: %s" % engine_string)
    return engine_string


def create_db(args, engine=None):
    """Creates a database with the data models inherited from `Base`.

    Args:
        engine (`str`, default None): String defining SQLAlchemy connection URI in the form of
            `dialect+driver://username:password@host:port/database`. If None, `engine` must be provided.
        args: Parser arguments.

    Returns:
        engine (:py:class:`sqlalchemy.engine.Engine`, default None): SQLAlchemy connection engine.

    """
    if engine is None:
        if args.RDS:
            engine_string = get_engine_string()
        else:
            engine_string = args.local_URI
        logger.info("RDS:%s" % args.RDS)
        engine = sql.create_engine(engine_string)

    Base.metadata.create_all(engine)
    logging.info("database created")

    return engine


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create defined tables in database")
    args = parser.parse_args()

    engine = create_db(args)
