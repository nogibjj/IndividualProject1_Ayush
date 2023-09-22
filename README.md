# IDS-706-Mini_Proj3

Link to my Youtube Video describing this project : https://www.youtube.com/watch?v=_thUsMoECbo

The repository contains the files utilized for Mini-Project 3 which includes:
1. Makefile
2. Requirements.txt
3. Python Files
4. Github Actions
5. CSV file for data analysis
6. Summary_statistics.md 

## Purpose of the Project: 
The aim of the project is to utilize Polars in Python for descriptive statistics. This library was used to read the dataset in CSV file. I used the 'forbes_2022_billionaires.csv' to analyze the average, median 'FinalWorth' of billionaires and its standard deviation in various countries. Bar Chart was used from the Plotly library to visualize the output from this analysis. 

## Code Description: 
1. stats_descriptive.py - A python file that uses 3 functions to calculate mean, median and standard deviation
2. test_stats.py - A python file that reads the forbes_2022_billionaires.csv file and tests the three functions in stats_descriptive.py.  
3. visualization.py - This contains the code to analyze and visualize the output.
4. Summary_statistics.md gives a summary of the output obtained after running the code. 


The output of the visualization is:


![Visualization using Bar Chart](https://github.com/nogibjj/IDS_706_ag758_proj2/blob/main/Visualization.png)

## CI/CD Automation Files :
requirements.txt - Holds all the necessary Python packages.

Makfefile - Automates different parts of developing a Python Project that includes : 
1. Running Tests
2. Cleaning Builds
3. Installing Dependencies

.github/workflows - 
Used for creating and storing GitHub Actions workflows. GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform. The workflow is triggered on pushes to the main branch as the following representation: 

![Visualization using Bar Chart](https://github.com/nogibjj/IDS_706_ag758_proj2/blob/main/GitHub.png)










[![Stats CI](https://github.com/nogibjj/IDS_706_ag758_proj2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS_706_ag758_proj2/actions/workflows/cicd.yml)
