import pickle
import traceback
import os
import sys
import pandas as pd
from flask import render_template, request, redirect, url_for
import logging.config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.score_model import *
from src.add import *
from src.load_data import *
from src.train_model import *
from src.generate_feature import *
from app import *

# Initialize the Flask application
app = Flask(__name__)

# Configure flask app from config.py
app.config.from_object('config')


# Define LOGGING_CONFIG in config.py - path to config file for setting
# up the logger (e.g. config/logging/local.conf)
logging.config.fileConfig(app.config["LOGGING_CONFIG"])
logger = logging.getLogger("wine-pred")
logger.debug('Test log')

# Initialize the database
db = SQLAlchemy(app)


@app.route('/')
def index():
    """Homepage of this prediction system.

    Returns: rendered html template
    """

    try:
        return render_template('homepage.html')
    except:
        logger.warning("Unable to display homepage")
        return render_template('error.html')




@app.route('/add', methods=['POST', 'GET'])
def add_entry():
    """View that process a POST with new wine input

    Returns: rendered html template with evaluation results.
    """

    fixed_acidity = request.form['fixed_acidity']
    volatile_acidity = request.form['volatile_acidity']
    citric_acid = request.form['citric_acid']
    residual_sugar = request.form['residual_sugar']
    chlorides = request.form['chlorides']
    free_sulfur_dioxide = request.form['free_sulfur_dioxide']
    total_sulfur_dioxide = request.form['total_sulfur_dioxide']
    density = request.form['density']
    pH = request.form['pH']
    sulphates = request.form['sulphates']
    alcohol = request.form['alcohol']


    try:
        # retrieve features
        fixed_acidity = request.form['fixed_acidity']
        volatile_acidity = request.form['volatile_acidity']
        citric_acid = request.form['citric_acid']
        residual_sugar = request.form['residual_sugar']
        chlorides = request.form['chlorides']
        free_sulfur_dioxide = request.form['free_sulfur_dioxide']
        total_sulfur_dioxide = request.form['total_sulfur_dioxide']
        density = request.form['density']
        pH = request.form['pH']
        sulphates = request.form['sulphates']
        alcohol = request.form['alcohol']
        logger.info("all inputs retrieved!")


        # load trained model
        path_to_model = app.config["PATH_TO_MODEL"]
        with open(path_to_model, "rb") as f:
            model = pickle.load(f)
        logger.info("model loaded!")

        # create a dataframe to store inputs for prediction
        wine_df = pd.DataFrame(columns=["fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
                                        "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide",
                                        "density", "pH", "sulphates", "alcohol"])

        wine_df.loc[0] = [fixed_acidity,
                          volatile_acidity,
                          citric_acid,
                          residual_sugar,
                          chlorides,
                          free_sulfur_dioxide,
                          total_sulfur_dioxide,
                          density,
                          pH,
                          sulphates,
                          alcohol]


        # change datatype from object to float
        wine_df = wine_df.astype("float")

        pred_quality = model.predict(wine_df)
        pred_quality_num = pred_quality[0]


        logger.info("prediction made: {:0.3f}".format(pred_quality_num))

        if pred_quality_num == 1:
            evaluation = "Nice wine to buy!"
        elif pred_quality_num == 0:
            evaluation = "Poor wine to avoid!"

        wine1 = Wine_Predict (fixed_acidity=float(fixed_acidity),
                              volatile_acidity=float(volatile_acidity),
                              citric_acid=float(citric_acid),
                              residual_sugar=float(residual_sugar),
                              chlorides=float(chlorides),
                              free_sulfur_dioxide=float(free_sulfur_dioxide),
                              total_sulfur_dioxide=float(total_sulfur_dioxide),
                              density=float(density),
                              pH=float(pH),
                              sulphates=float(sulphates),
                              alcohol=float(alcohol),
                              quality=float(pred_quality)
                              )
        instance = db.session.query(Wine_Predict).filter_by(fixed_acidity=float(fixed_acidity),
                                    volatile_acidity=float(volatile_acidity),
                                    citric_acid=float(citric_acid),
                                    residual_sugar=float(residual_sugar),
                                    chlorides=float(chlorides),
                                    free_sulfur_dioxide=float(free_sulfur_dioxide),
                                    total_sulfur_dioxide=float(total_sulfur_dioxide),
                                    density=float(density),
                                    pH=float(pH),
                                    sulphates=float(sulphates),
                                    alcohol=float(alcohol)
                                    ).first()
        if not instance:
            db.session.add(wine1)
            db.session.commit()
            logger.info("New wine evaluated as: %s", evaluation)

        result = "This wine is classified as a {}".format(evaluation)
        # return redirect(url_for('index'))
        return render_template('homepage.html', result=result)
    except:
        traceback.print_exc()
        logger.warning("Not able to display evaluations, error page returned")
        return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], port=app.config["PORT"], host=app.config["HOST"])
