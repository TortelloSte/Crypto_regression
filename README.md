# Analysis of Bitcoin Historical Data:
Bitcoin is a decentralized digital currency that has gained popularity over the last ten years. As the price of Bitcoin has fluctuated dramatically, there is a growing interest in using machine learning techniques to analyze and predict the price of Bitcoin. In this project, I have analyzed historical Bitcoin data using various regression methods and models. The ultimate purpose of this project is to demonstrate how this data can be studied through machine learning.

All the data used for this project can be found directly at the following link: https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory, from which you can extract the dataset coin_Bitcoin.csv since the folder contains different datasets for different digital coins. The study focuses on Bitcoin precisely because of its popularity.

This study is conducted using Python3 as the programming language for implementing machine learning models, and the project will explain the theoretical aspects behind these models to enable them to be used to study and understand the different regression models used in Version_1 of the project, which was an assignment during my course of study.

Subsequently, I decided to revisit this project and create a Version_2 where I apply different techniques to show how to analyze this data in a different way.


## Requirements:
To run the program, several libraries are required in our Python workspace. My recommendation is to use a new environment for the development of this study, which I make public to allow anyone to modify and improve the code.

The libraries required for this study are as follows:

- pandas
- sklearn
- numpy
- datetime
- matplotlib
- keras

These can be installed via the terminal with the following commands:

pip install 'library name'
conda install 'library name' (if using Anaconda as the environment)



## How to Use the Project:

The project is divided into two main folders:

1. The folder named 'Version_1' refers to all the code that was developed during the course of studies and subsequently modified to make the code more readable and interpretable once the exam project was delivered.
      Within this folder, there are two other subfolders as follows:
      - LSTM_machine_learning: Inside this folder is the code that applies the LSTM model, which was a test of applying a particular model that will be explained later in the section dedicated to different models.
      - regression_model: This is the main folder where all the code for the models applied to the dataset is located. Additionally, by personal choice, I decided to write a code called "main" and improved it to evaluate the different models to understand which one was the best.
2. The folder named 'Version_2' refers to the new codes that were tested after the course of studies and are therefore improved or are a proof of implementation of different models in different ways.
      - Inside, there are only two codes. The first is main.py, which allows us to run the code inside the utils.py file, which will be explained in detail in the following paragraphs.


To use the project, I recommend cloning the entire repository from GitHub and then reading the readme.md file in detail to understand, given the project's objectives, the section below that explains how the different regression models work. 

Afterward, add the DATA folder to the repository where you intend to use the project and download the datasets with all the data from Kaggle.



 ## Regression Model

 # 1.





   ### Author:
   Stefano Perdicchia
