#To monitor the real time data and build a logistic regression model.

#importing the required libraries
from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt
import numpy as np

cpu = CPUTemperature()


# Logistic Regression
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/pi/Documents/Sensor_readings/data_for_process.csv')
X = dataset.iloc[:, [1]].values
y = dataset.iloc[:, 2].values
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

plt.ion()
x = np.zeros(20)
y = np.zeros(20)
x = x.tolist()
y = y.tolist()

# saving to a csv file 
def write_temp(temp):
    with open("/home/pi/Documents/Sensor_readings/data.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
    
def graph(temp):
    
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.show()
    plt.pause(0.01)

while True:
    temp = cpu.temperature
    write_temp(temp)
    y.append(temp)
    x.append(time())
    x = x[-20:]
    y = y[-20:]
    
    print(y[-1])
    p = classifier.predict(sc.transform(y[-1]))
    if p == 1:
        print("ALL IS WELL")
    else:
        print("ALERT")
    graph(temp)
 
