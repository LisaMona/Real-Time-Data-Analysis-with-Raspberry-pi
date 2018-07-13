# Real-Time-Data-Analysis-with-Raspberry-pi

This repository contains the real-time data of an inbuilt temperature sensor in th R-pi 3B.
The data is stored in data_for_process.csv file and is read from that for drawing an interactive real-time plot.
The code for the same is written in the file temp sensor.py
For our convenience, latest 20 data points is plotted in a graph.

This part has been taken as a reference from https://projects.raspberrypi.org/en/projects/temperature-log



As an extension to the project, a Machine Learning model has been trained with the already exsiting data.
The code for training and predicting the results from static csv file is present in Building the model.py



The combination of the above has been carried out next.

This logistic regression model learns from the data and predicts the output/results from the sensor readings in real-time.
The instant data has been stored in the file real_time_data.csv
The code present in Real time Temp monitor.py trains the logistic regression model on the static data from data_for_process.csv and then 
new data is stored into real_time_data.csv

The latest entry into the file is used as an input to the model and results are predicted.

An interactive graph as well as an alert message is also notified on the screen for the users.



Few output images are also given for reference.

Hope it helps!

