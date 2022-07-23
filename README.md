# Capstone project (Roll-Off Trucks)

 The waste management system is a technique used by a company to dispose of waste. This waste typically consists of 4 different types follows, municipal solid waste, industrial waste, agricultural waste, and hazardous waste, these types of waste are usually carried out from one point to another point, i.e., source (where the waste is collected) to the destination (where the waste must be dumped), these wastes are majorly carried out from one place to another place using a large roll-off truck. Various key activities take place during the process of loading and unloading waste in the truck, including loading/unloading and carrying portable and removable containers from one area to another. These events must be monitored and evaluated to ensure that the task has taken place as intended.
Detect and report incidents of interest recorded by cameras placed on trash management trucks using Machine Learning and Machine Vision techniques. The objective is to identify in real-time key events and generate alerts for a vehicle operation monitoring system. 
External elements such as light and precipitation can influence outcomes because the vehicles operate outdoor in all weather conditions. The aim is to use powerful machine learning and machine vision algorithms to handle real-world problems in the waste management sector.

# Problem identification

The company has a camera fixed to the back of their Roll Off Trucks, using the images from this camera they would like to accurately map the activities performed by the truck and also to reduce the manual effort by building a scalable solution which would convert the video input into a report summarising all the activities performed within the given timeframe.


# Business Need for implementing ML in this project

The pre-existing technology used by the company is RFID.  The main issue faced by the company while using RFID is that they were susceptible to several field-related conditions.
By implementing a Machine Learning model into this, we will be able to help the customers make more accurate calculations that are related to productivity and will be able to improve real-time diagnostic capabilities for the system.

# Dataset and its source

The dataset has been provided by the company “Metric Masters Ltd”.
Input/Training Data:
The data provided is comprised of 3 scenarios.
 	a)Dumping
	b)Loaded
	c)Unloaded
The Resolution of the given images is in between 180*320 to 720*1080.
Testing Continuous Data:
The images that were captured by the camera every 3 seconds in 4.5 Hours, which is comprised of around 3000 images.
All images were recorded with their respective timestamps. 


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

# Preprocessing

Every image which we received was in a different dimension, As part of pre-processing, we downsized all images to 320*180 before we start using the images. 

Also, we have converted the images into grayscale, so that the CNN model will be able to provide better accuracy regardless of diminishing image resolution and quality.

### Short summary about the list of other steps involved in preprocessing

Data Preparation and Processing
1)Data Labelling
2)Image resizing
3)RGB Image to greyscale 
4)Normalizing pixel values
5)Removing similar images

# Data Pipeline

![Screenshot 2022-07-20 184833](https://user-images.githubusercontent.com/105304976/180095626-7591c4dd-894c-420c-b61f-a0f4f6f2383e.png)

# Methods

The method used to arrive at the desired result can be divided into 3 major sections

### Modeling Objective
Identify a machine learning model that accurately identifies the state of any given image.
### Post Processing
Design a pattern recognition logic that would be able to identify the activity that takes place.
### Modeling Steps
The focus here is to create a classification model that can accurately classify given images into the defined states. Furthermore, the model must be lightweight so that it can handle high volumes of data but robust enough to be applicable in all 4 vivid seasons that Canada experiences. 

# Models Implemented and their perfromace based on accuracy and coverage

We have implemented three different classification models to see which one is best suited for our use case. We need a model that gives high accuracy but also is lightweight and the best model in terms of prediction speed.
1.	Logistic Regression
2.	Random Forrest
3.	CNN

### Accuracy of each model on our data

![acc](https://user-images.githubusercontent.com/105304976/180098047-c5f0081a-ad1d-4ecf-84e8-5545beec9d1f.png)


The plots represents the accuracy and coverage for 3 models
* We can see that CNN model has the highest accuracy and coverage with 93.3%

### Event prediction aka coverage of the model based on our data

![qq](https://user-images.githubusercontent.com/105304976/180098332-9f3a50a2-838e-4261-b4bc-620822ff37fb.png)

The graph represents the prediction of events using 3 models.
* CNN Model has performed better than the other 2 models in predicting events.
* Out of 15 Events, the CNN model predicted 14 events correctly.

( We will be discussing how we have been able to evaluate the event prediction, this will be covered in the post-processing steps with the help of the flowchart for a better understanding. )

# Post Processing
### Input: Sequence of States 
### Output: Operational report with a list of activities 
Get the predicted states of all images, this would contain 4 distinct values Loaded, Unloaded, Inter and Dumping. 
1.	Decoding Inter into Loading and Unloading
![Screenshot 2022-07-20 193031](https://user-images.githubusercontent.com/105304976/180099794-301926aa-0277-4d98-a881-ba6bc25a982b.png)

2.	Classification of activities
![Screenshot 2022-07-20 193202](https://user-images.githubusercontent.com/105304976/180099930-9ff9cf52-d9c4-4d6a-9003-c0e0520af8d7.png)

# Results

After performing all the actions which were discussed in the section on post-processing we will be able to arrive at our desired result.
A graph will be generated based on the activity of the truck along with the summary table which reports the list of activities.
This file will be generated in form of .html

![Screenshot 2022-07-20 194035](https://user-images.githubusercontent.com/105304976/180100693-3bc2ed79-8b35-49d2-9d33-6460dcfab054.png)


# Operating instruction

* Clone the repo
* Execute the .requirements file so that it will install all the dependencies 
* Execute the main.py file

### Note:
*To execute the file you will need access to the dataset since we have signed the NDA agreement we are unable to publish the dataset here. In case you have the dataset, please follow the next process.
* The dataset will be divided into two folders. 1) waste folder ( which will have all the training images for the model ) 2) Test folder ( The file which needs to be predicted )
* All these folders have to be in the same folder in order to successfully run the code.

# Troubleshooting instruction
 
In case you find any error while running the main.py file, it should probably be because ceratin libraries may not have been installed in the .requirements file.
 So, kindly install those libraries which u get to see in the error.
 
 # Working instructions:
  
After the setup of the code is completed, Kindly follow the below-mentioned steps:
  
  * Once the code is executed, it will show a prompt saying "Press 1 to train the model and 2 to run the prediction"
  * In case if you have new data to train the model, press option 1 but before doing this, you will have to store all the new data in the waste folder after that you will also have to delete the already existing trained model which is being present in the same directory. 
  * Once this is done, you will also be seeing a prompt which says that the model is getting trained the model will be trained and will be stored in .h5 format under the same folder.
  * In case you are providing option 2, the newly saved model will be loaded for prediction, once it is successfully loaded you will be able to see a prompt saying "The weight of the model has been restored from the saved file"
  * You will now be asked to provide the name of the folder in which the continuous data is present aka, the data which needs to be predicted.
  * You will now see the processing of the test data getting predicted by the model in a pictorial representation. 
  * Once the above step is completed, there will be two .html data being generated and stored in the project folder. One HTML will be having the information about all the events which have taken place, and the other one will have the consolidated pieces of information.
  * In the next step, you will now see a prompt saying press 1 to send the consolidated file as an email and 2 to exit.
  * If option 1 is given, the prompt will now ask the user to provide an email address, to send the report.
  * If a valid email address is provided, the .html report will be sent in the email.
  * Once the email is sent successfully, you will see a message stating that the email has been sent successfully.
  * Note: In case you don't see the email in the inbox, please check your spam folder.
  
(Optional)
  If you want your email address to send the report to the recipient please follow the instructions provided below.
   
   * Create a new gmail account ( highly recommended ) or use an existing email address.
   * Navigate to " Manage your account " as shown in the below mentioned screenshot.
   ![Screenshot 2022-07-20 232119](https://user-images.githubusercontent.com/105304976/180122968-d8da207c-1e8d-490c-9171-40fd8a009512.png)
   * Click on security and the click on 2SV
  ![Screenshot 2022-07-20 232407](https://user-images.githubusercontent.com/105304976/180123284-3ff37d53-4400-4ca9-a442-8ab81ff8fac2.png)
  * Activate the 2 SV, to activate please follow the instructions shown by gmail on your screen.
  * Once the above step is successfully performed, you will have to now click the app password.
  * ![Screenshot 2022-07-20 232703](https://user-images.githubusercontent.com/105304976/180123756-acbc4eb0-79e0-4b96-b73a-9cc84b590d66.png)
  * Create a custom name of your own choice and hit on generate.
  * Once it is generated you will see a 16 digit verification code. Kindly save it on a notepad.
  ![Screenshot 2022-07-20 233117](https://user-images.githubusercontent.com/105304976/180124049-c93a71ca-299d-4479-9235-4be5b89e4869.png)
  * Now open the emailhandler.py from our project file and provide the newly created email address in the sender and past the 16 digit password to the password variable.
  
  # Demo
  https://user-images.githubusercontent.com/105304976/180585582-c0ad7cf1-e338-42ed-843b-ec6ea322dc66.mp4
  
 























