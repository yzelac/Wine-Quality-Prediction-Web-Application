# Example project repository

```diff
+ QA feedback from Yucheng Zhu is highlighted in green.
```


<!-- toc -->

- [Project Charter](#project-charter)
- [Backlog](#backlog)
- [Repo structure](#repo-structure)
- [Documentation](#documentation)
- [Running the application](#running-the-application)
  * [1. Set up environment](#1-set-up-environment)
    + [With `virtualenv` and `pip`](#with-virtualenv-and-pip)
    + [With `conda`](#with-conda)
  * [2. Configure Flask app](#2-configure-flask-app)
  * [3. Initialize the database](#3-initialize-the-database)
  * [4. Run the application](#4-run-the-application)
- [Testing](#testing)

<!-- tocstop -->

## Project Charter 

**Vision**: Try to figure out the "secret recipe" that make a song popular and to understand the difference in popularity trend between different years/genre.

**Mission**: By inputting information of a song such as lyric, genre and etc., the web app will predict the popularity rank from 1 (the most popular) to 100 (the least popular).

**Success criteria**: 
* ML criteria: The dataset will be separated into training set and testing set. MSE could be used as the machine learning measurement to evaluate models and choose the optimal one.  
* Business criteria: By predicting the popularity of a song, the web app could possibly help song writers to increase exposures of their songs and thus increase their incomes. The success of the app could be measured by the year of year increase in income of active users.

```diff
Is the vision clearly articulated?
+ Yes, the vision is clearly articulated.

Is there an audience who will find it motivating?
+ Yes, both music lovers and producers will be interested in learning more about various factors that makes a song popular.

Is there enough information for the business stakeholder to understand and agree with the motivation for the project so that they fund the project over someone else’s?
+ Yes, the vision provides enough information for the business stakeholder to understand and agree with the motivation. One suggestion is explain "secret recipe" more in detail (e.g. is it about specific lytics, genre, rhythm, etc.)

```

## Backlog
**Develop Themes**: 
* With information about a song, the app will predict its popularity which could possibly help user to increase the songs popularity, which eventually increase song-writers income.
* By predicting the songs' popularities, the app can help user to choose between songs.

**Epic 1**: Data Preparation
There are several datasets available online about songs and their popularity measured by Billboard rankings.

* Story 1: Merge databases (4 point)
  * Backlog
  * Online datasets searching
  * Merge several datasets to include more features of songs that will be needed for modeling

* Story 2: EDA (2 point)
  * Backlog
  * Explore the potential variables that could be used to better predict the songs' popularities
  
**Epic 2**: Modeling
Build the predicting models such as linear regression, neural networks and etc. Choose the optimal model by the ML metrics.

* Story 1: Build initial models (4 points)
  * Backlog
  * Build several predicting models with features from the first epic.
  * Use common ML metrics and test dataset to choose the final model.
  
* Story 3: Model review with QA partner (4 points)
  * Backlog
  * Review the model with QA partner based on the machine learning criteria as well as the user satisfaction
  * Move both datasets and model to AWS server
  
**Epic 3**: Web App Building
Build the web app to enable users access the model through web interface.

* Story 1: UI design of the web app (8 points)
  * Backlog
  * Depends on the functionality of the model, the web app should have reasonable user input and output design
  
* Story 2: Beautify (8 points)
  * Icebox
  * Beautify the web app if time permits
  

## Repo structure 

```
├── README.md                         <- You are here
│
├── app
│   ├── static/                       <- CSS, JS files that remain static 
│   ├── templates/                    <- HTML (or other code) that is templated and changes based on a set of inputs
│   ├── models.py                     <- Creates the data model for the database connected to the Flask app 
│   ├── __init__.py                   <- Initializes the Flask app and database connection
│
├── config                            <- Directory for yaml configuration files for model training, scoring, etc
│   ├── logging/                      <- Configuration files for python loggers
│
├── data                              <- Folder that contains data used or generated. Only the external/ and sample/ subdirectories are tracked by git. 
│   ├── archive/                      <- Place to put archive data is no longer usabled. Not synced with git. 
│   ├── external/                     <- External data sources, will be synced with git
│   ├── sample/                       <- Sample data used for code development and testing, will be synced with git
│
├── docs                              <- A default Sphinx project; see sphinx-doc.org for details.
│
├── figures                           <- Generated graphics and figures to be used in reporting.
│
├── models                            <- Trained model objects (TMOs), model predictions, and/or model summaries
│   ├── archive                       <- No longer current models. This directory is included in the .gitignore and is not tracked by git
│
├── notebooks
│   ├── develop                       <- Current notebooks being used in development.
│   ├── deliver                       <- Notebooks shared with others. 
│   ├── archive                       <- Develop notebooks no longer being used.
│   ├── template.ipynb                <- Template notebook for analysis with useful imports and helper functions. 
│
├── src                               <- Source data for the project 
│   ├── archive/                      <- No longer current scripts.
│   ├── helpers/                      <- Helper scripts used in main src files 
│   ├── sql/                          <- SQL source code
│   ├── add_songs.py                  <- Script for creating a (temporary) MySQL database and adding songs to it 
│   ├── ingest_data.py                <- Script for ingesting data from different sources 
│   ├── generate_features.py          <- Script for cleaning and transforming data and generating features used for use in training and scoring.
│   ├── train_model.py                <- Script for training machine learning model(s)
│   ├── score_model.py                <- Script for scoring new predictions using a trained model.
│   ├── postprocess.py                <- Script for postprocessing predictions and model results
│   ├── evaluate_model.py             <- Script for evaluating model performance 
│
├── test                              <- Files necessary for running model tests (see documentation below) 

├── run.py                            <- Simplifies the execution of one or more of the src scripts 
├── app.py                            <- Flask wrapper for running the model 
├── config.py                         <- Configuration file for Flask app
├── requirements.txt                  <- Python package dependencies 
```
This project structure was partially influenced by the [Cookiecutter Data Science project](https://drivendata.github.io/cookiecutter-data-science/).

## Documentation
 
* Open up `docs/build/html/index.html` to see Sphinx documentation docs. 
* See `docs/README.md` for keeping docs up to date with additions to the repository.

## Running the application 
### 1. Set up environment 

The `requirements.txt` file contains the packages required to run the model code. An environment can be set up in two ways. See bottom of README for exploratory data analysis environment setup. 

#### With `virtualenv`

```bash
pip install virtualenv

virtualenv pennylane

source pennylane/bin/activate

pip install -r requirements.txt

```
#### With `conda`

```bash
conda create -n pennylane python=3.7
conda activate pennylane
pip install -r requirements.txt

```

### 2. Configure Flask app 

`config.py` holds the configurations for the Flask app. It includes the following configurations:

```python
DEBUG = True  # Keep True for debugging, change to False when moving to production 
LOGGING_CONFIG = "config/logging/local.conf"  # Path to file that configures Python logger
PORT = 3002  # What port to expose app on 
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/tracks.db'  # URI for database that contains tracks

```


### 3. Initialize the database 

To create the database in the location configured in `config.py` with one initial song, run: 

`python run.py create --artist=<ARTIST> --title=<TITLE> --album=<ALBUM>`

To add additional songs:

`python run.py ingest --artist=<ARTIST> --title=<TITLE> --album=<ALBUM>`


### 4. Run the application 
 
 ```bash
 python app.py 
 ```

### 5. Interact with the application 

Go to [http://127.0.0.1:3000/]( http://127.0.0.1:3000/) to interact with the current version of hte app. 

## Testing 

Run `pytest` from the command line in the main project repository. 


Tests exist in `test/test_helpers.py`