## Developer: Yucheng Zhu
QA: Yi Feng


# MSiA 423 - Wine Quality Prediction Project


<!-- toc -->
- [Project Charter](#project-charter)
- [Backlog](#backlog)
- [Repo structure](#repo-structure)
- [Documentation](#documentation)
- [Running the application](#running-the-application)
- [Testing](#testing)
- [Works Cited](#cited)


<!-- tocstop -->

## Project Charter 

**Vision**: Conventional methods of evaluating wine quality are primarily based on the subjective experience of tasters. This project not only explores the relationship between physiochemical properties of wines and their taste, but also intends to utilize machine learning methods to figure out which physiochemical properties make a wine taste "good."

**Mission**: Enable users to predict quality of a wine based on physiochemical properties of the wine.

**Success criteria**: 
- (Machine Learning) The prediction accuracy ((TP+TN)/total) of the selected model on the test dataset should be at least 80%. 
- (Business) User retention rate should be at least 60%.
- (Business) Those users who have tasted the wine they try to predict via the web app will be asked whether they think the prediction is accurate. The project is considered successful if the satisfaction rate is greater than 70%. 

## Backlog 

**Develop Themes**: 

Wine lovers always hope to spend their money on wines they will actually enjoy. However, without actually tasting the wine, it is often challenging for people to predict wine quality ahead of time. Even though a few famous wine critics do provide ratings on wine, those scores are still based on their subjective experience. 

The aim of this project is to investigate how the taste of wines are related to their measurable physiochemical properties (e.g. pH, volatile acidity, residual sugar, sulfur dioxide, etc.). Through various machine learning methods, the project will help to identify the most physiochemical properties that make a wine taste good as well as allow users to predict the quality of wines based on their physiochemical properties. In this way, users will be able to assess wine quality from a more objective perspective and make better buying decisions.

The final web app would allow user to input values of the most important physiochemical properties of wine (either white or red) and return the predicted wine quality.


**Epic 1: Data Preparation** 
- Story #1: Downloading the data files (red wine & white wine) from UCI Machine Learning Repository (1 pt) **(Planned for the next 2 weeks)**
    - **Backlog**
    - Link to data source:[https://archive.ics.uci.edu/ml/datasets/wine+quality]
- Story #2: EDA and Data Cleaning (2 pts) **(Planned for the next 2 weeks)**
    - **Backlog**
    - Conducting exploratory data analysis (variable structures, distribution of variables, etc.)
    - Performing data cleaning (null values, outliers, etc.)
    
**Epic 2: Modeling and Model Selection** 
- Story #1: Building classification models on randomly selected training data using Random Forest, XGBoost, and Neural Networks (4 pts) **(Planned for the next 2 weeks)**
    - **Backlog**
- Story #2: Comparing models based on performance metrics (Accuracy) on testing data (2 pts) **(Planned for the next 2 weeks)**
    - **Backlog**
- Story #3: Exploring additional models (e.g. CNN, SVM)
    -   **Icebox**
- Story #4: Reviewing models with QA partner (4 pts)
    - **Backlog**
    
**Epic 3: Online Deployment and Testing** 
- Story #1: Web app UI design (8 pts)
    - **Backlog**
- Story #2: Deploying web app (Flask) on AWS (8 pts)
    - **Backlog**
- Story #3: Creating an RDS instance (4 pts)
    - **Backlog**
- Story #4: Testing (Unit tests and Configured reproducibility tests) (8 pts)
    - **Backlog**
    
**Epic 4: Final Presentation**  
- Story #1: Presentation slides (4 pts)
    - **Backlog**

    
## Repo structure

```
├── README.md                         <- You are here
│
├── requirements.txt                  <- Python package dependencies.
│
├── Makefile                          <- Make file for reproduction
│
├── config.py                         <- Flask and Database config file
│
├── .gitignore                        <- Specifies intentionally untracked files to ignore
│
├── app
│   ├── app.py                        <- Script for deploy the Flask app (main script)
│   │  
│   ├── static                        <- Folder contains images for the web pages
│   │  
│   ├── templates                     <- Folder contains html files
│
├── config
│   ├── model_config.yml              <- YAML configuration
│   │  
│   ├── logging                       <- Folder holding logging configuratins
│   
├── data                              <- Folder that contains primary data set
│   ├── red.csv                       <- Primary dataset downloaded from S3
│   │
│   ├── y_predicted.csv               <- Prediction result
│   │
│   ├── train                         <- Folder holding training data
│   │    ├── X_train.csv              <- training data
│   │    │   
│   │    ├── y_train.csv              <- training label
│   │
│   ├── test                          <- Folder holding testing data
│        ├── X_test.csv               <- testing data  
│        │   
│        ├── y_test.csv               <- testing label  
│  
├── deliverables                      <- Folder that contains deliverables
│
├── docs                              <- Folder that contains documents
│
├── models                            <- Folder that contains trained model
│
├── notebooks                         <- Folder that contains notebooks
│
├── src                               <- Source data for the project.
│   ├── add.py                        <- Script for adding entry to db. 
│   │  
│   ├── download_data.py              <- Script for downloading data from a public S3 bucket.
│   │ 
|   ├── upload_data.py                <- Script for uploading data to a specific busket (can be private).  
│   │
│   ├── load_data.py                  <- Script for loading data.   
│   │ 
│   ├── generate_feature.py           <- Script for generating features.  
│   │ 
│   ├── train_model.py                <- Script for model training. 
│   │ 
│   ├── score_model.py                <- Script for scoring data using trained model.     
│   │ 
│   ├── evaluate_model.py             <- Script for model performance evaluation. 
│   │    
│   ├── helper                        <- Folder holding script for helper functions
│   │    
│   ├── sql
│        │  
│        ├── config.py                <- config file  
│        │   
│        ├── helpers.py               <- helper functions
│        │ 
│        ├── local.py                 <- Script for creating local .db  
│        │   
│        ├── sqldb.py                 <- Script for adding tables to 'msia' database in RDS.
│
```


## Documentation
- See `ocs/README.md`s for mid-project info.

## Running the application (To be added)

### 1. Change directory to MSiA423-Project/


### 2. Create virtual environment

The `requirements.txt` file contains the packages required to run the model code. An environment can be set up in two ways.

#### With `conda` (Recommended)

```bash
conda create -n wine python=3.7
conda activate wine
conda install pip
pip install -r requirements.txt

```

#### With `virtualenv`

```bash
pip install virtualenv

virtualenv wine

source wine/bin/activate

pip install -r requirements.txt

```

#### If using EC2, please run:
```bash
source ~/.bashrc
```


### 3. Reproduce model using pipeline (optional)

- Reproduce with default setting (setting can be configured manually in `config/model_config.yml`):
```bash
make all
```

- To create a database in the local location, run:
```bash
python src/add.py

# "--local_URI", default='sqlite:///data/Wine_Predict.db'
# If want to save it into non-existing sub-directories, please make sure to create the folders first

```

- (Optional) To upload dataset to your personal S3, please change the following line in `Makefile` accordingly
```bash
data_uploading:
	python src/upload_data.py --input_file_path "data/red.csv" --bucket_name "yzhu-project" --output_file_path "red3.csv"
```
- (Optional) And run
```bash
make data_uploading
```

### 4. Configure Flask app

`config.py` holds the configurations for the Flask app:

```python
DEBUG = True  # Keep True for debugging, change to False when moving to production 
LOGGING_CONFIG = "config/logging/local.conf"  # Path to file that configures Python logger
PORT = 3000
APP_NAME = "wine-predictor"
HOST = "127.0.0.1"
MAX_ROWS_SHOW = 30
PATH_TO_MODEL = "models/rf_model.pkl"
```

### 5.Run the Flask app
- To set up environment variable SQLALCHEMY_DATABASE_URI from command line in the main project repository, please run:
```bash
# If using default argument when running src/add.py, run:
local: export SQLALCHEMY_DATABASE_URI='sqlite:///data/Wine_Predict.db'

rds: export SQLALCHEMY_DATABASE_URI="{conn_type}://{user}:{password}@{host}:{port}/{DATABASE_NAME}"
```
- then
```bash
python app.py
```

### 5 Interact with the application


Navigate to http://127.0.0.1:3000/ (If using RDS: the combination of your EC2's public/elastic IP + port) to interact with the current version of the app.

The app is also available at: http://3.13.243.252:3000/ 


## Testing

- Run `make test` from the root directory to run all unit tests
- Test file is located at `test/test.py` 


## Works Cited

- Images from 'Sour Grapes' and Sothebys.com
- Template from W3Schools: https://www.w3schools.com/w3css/tryw3css_templates_parallax.htm