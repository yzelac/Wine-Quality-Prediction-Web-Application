# MSiA423 - Wine Quality Prediction Project (Yucheng Zhu)


<!-- toc -->
- [Project Charter](#project-charter)
- [Backlog](#backlog)
- [Repo structure (To be added)](#repo-structure)
- [Documentation (To be added)](#documentation)
- [Running the application (To be added)](#running-the-application)
- [Testing (To be added)](#testing)


<!-- tocstop -->

## Project Charter 

**Vision**: Conventional methods of evaluating wine quality are primarily based on the subjective experience of tasters. This project not only explores the relationship between physiochemical properties of wines and their taste, but also intends to utilize machine learning methods to figure out which physiochemical properties make a wine taste "good."

**Mission**: Enable users to predict quality of a wine based on physiochemical properties of the wine.

**Success criteria (Machine Learning)**: The accuracy of the selected model on testing dataset should be at least 80%. 

**Success criteria (Business)**: User retention rate should be at least 60%.

## Backlog 

**Develop Themes**: 

Wine lovers always hope to spend their money on wines they will actually enjoy. However, without actually tasting the wine, it is often challenging for people to predict wine quality ahead of time. Even though a few famous wine critics do provide ratings on wine, those scores are still based on their subjective experience. The aim of this project is to investigate how the taste of wines are related to their measurable physiochemical properties. Through various machine learning methods, the project will help to identify the most physiochemical properties that make a wine taste good and allow users to predict the quality of wines based on their physiochemical properties. In this way, users will be able to assess wine quality from a more objective perspective and make better buying decisions.


**Epics 1: Data Preparation** 
- Backlog #1: Download the data files (red wine & white wine) from UCI Machine Learning Repository (1 pt) **(Planned for the next 2 weeks)**
    - Link: [https://archive.ics.uci.edu/ml/datasets/wine+quality]
- Backlog #2: EDA and Data Cleaning (2 pts) **(Planned for the next 2 weeks)**
    - Conducting exploratory data analysis (variable structures, distribution of variables, etc.)
    - Performing data cleaning (null values, outliers, etc.)
    
**Epics 2: Modeling and Model Selection** 
- Backlog #1: Build classification models on randomly selected training data using Random Forest, XGBoost, and Neural Networks (4 pts) **(Planned for the next 2 weeks)**
- Backlog #2: Comparing modelings based on performance metrics (Accuracy) on testing data (2 pts) **(Planned for the next 2 weeks)**
- Icebox: Trying additional models (e.g. CNN, SVM)

**Epics 3: Online Deployment and Testing** 
- Backlog #1: Web app (Flask) deployed on AWS (8 pts)
- Backlog #2: An RDS instance (4 pts)
- Backlog #3: Testing (Unit tests and Configured reproducibility tests) (8 pts)

**Epics 4: Final Presentation**  
- Backlog #1: Presentation slides (4 pts)
    
    
## Repo structure (To be added) 
## Documentation (To be added)
## Running the application (To be added)
## Testing (To be added)





