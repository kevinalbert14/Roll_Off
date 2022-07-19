# Capstone project (Roll-Off Trucks)

 The waste management system is a technique used by a company to dispose of waste. This waste typically consists of 4 different types follows, municipal solid waste, industrial waste, agricultural waste, and hazardous waste, these types of waste are usually carried out from one point to another point, i.e., source (where the waste is collected) to the destination (where the waste must be dumped), these wastes are majorly carried out from one place to another place using a large roll-off truck. Various key activities take place during the process of loading and unloading waste in the truck, including loading/unloading and carrying portable and removable containers from one area to another. These events must be monitored and evaluated to ensure that the task has taken place as intended.
Detect and report incidents of interest recorded by cameras placed on trash management trucks using Machine Learning and Machine Vision techniques. The objective is to identify in real-time key events and generate alerts for a vehicle operation monitoring system. 
External elements such as light and precipitation can influence outcomes because the vehicles operate outdoor in all weather conditions. The aim is to use powerful machine learning and machine vision algorithms to handle real-world problems in the waste management sector.

# Problem identification

The company has a camera fixed to the back of their Roll Off Trucks, using the images from this camera they would like to accurately map the activities performed by the truck.


# Business Need for implementing ML in this project

The pre-existing technology used by the company is RFID.  The main issue faced by the company while using RFID is that they were susceptible to several field-related conditions.
By implementing a Machine Learning model into this, we will be able to help the customers make more accurate calculations that are related to productivity and will be able to improve real-time diagnostic capabilities for the system.

# Dataset and its source

The camera at the back of the truck takes an image every 3 seconds, each image is associated with a timestamp along with the speed embedded in a JSON format.
Given any duration of this data, we would need to identify which among the following activities have taken place.

The dataset has been provided by the company “Metric Masters Ltd”. The data provided is divided into 3 scenarios.

Pick Up
Drop Off
Dumping

# Preprocessing

Every images which we have received was in a different dimension so, As part of pre-processing, we have downsized all images to 320*180 before we start using the images. 

Also, we have converted the images into grayscale, so that the CNN model will able to provide better accuracy regardless of diminising image resolution and quality.


# Data Labeling

We have manually divided and labled the dataset into 4 different types.
Loaded
Unloaded
Dumping
Loading/Unloading (aka Inter)

The states look like the images which are mentioned below.


## Dumping
![20211202T093719](https://user-images.githubusercontent.com/105304976/179648479-0875306a-a2b4-485c-9b16-56ac4afc1aae.jpg)

## Inter
![20211117T103608427](https://user-images.githubusercontent.com/105304976/179649077-1dc57bc9-ae6f-4381-9908-186c52c60fdb.jpg)

## Loaded
![20211117T101005764](https://user-images.githubusercontent.com/105304976/179648803-65a21a24-14d6-42cd-994e-26f078730a50.jpg)

## Unloaded
![20211117T103709227](https://user-images.githubusercontent.com/105304976/179648922-b05e58be-16e0-4caf-b00f-30a6b0e32f72.jpg)











