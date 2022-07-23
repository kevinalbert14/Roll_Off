from sklearn.metrics import confusion_matrix
import tensorflow as tf
import matplotlib.pyplot as plt 
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.image import load_img, img_to_array, smart_resize
from tensorflow.keras import datasets, layers, models
from pathlib import Path
import numpy as np
from imageload import image_load, test_loader, timestamps
from splitting import splitting_train_test
from mod import mod
from accuracy_graph import accuracy_graph, rep_1, individual_events, graphreport, finalreport_1
from conf_matrix import conf_matrix
from classifier_state import classifier_state
from tsreport import events, tsreport
from continuous_data import continuous, evelogs, samp_pred
from single_events import single_events
from keras.models import load_model
from emailhandler import emailer
import os

def clear():      # This function will create the terminal screen
      os.system('cls')

clear()

def choice():     # This function will allow the user to select the choice between 1 & 2
    sel = 0       #Initally providing the selection value as 0
    while sel not in [1,2]:   #Checking if the value is 1 or 2
        sel = int(input("Press 1 to train the model and 2 to run the prediction:  ")) # Getting the input from the user
        if sel != 2:    # If the variable sel is not equal to 2 then this code will be executed
            print("The model is getting trained")     
    return sel    #The variable sel is being returned

selection = choice()    # Have called the function choice to get the user input

while selection == 1:   # If the user has provided the input as 1 the this code will be executed if not the else part will be executed


      if selection == 1: # If the user has provided his choice as 1 then this part of the code will be executed


            target_dict = dict([("Dump", 0),("Loaded",1),("Unloaded",2),("Inter",3)]) # We have assigned the var target_dict with dict key value pairs

            images, labels = image_load() # The file which is used for training is loaded using the image_load() function and it will return images and lables in the form of array

            labels_int = [] # use the target_dict to convert the string labels to an array of integers
            for i in labels:
                  n_key = target_dict[i]
                  labels_int.append(n_key)
            labels_int = np.array(labels_int)

            X_train, Y_train, X_test, Y_test, X_val, Y_val = splitting_train_test(images, labels_int) # The training data has been split and the correspondings values are returned.
            clear()
            model = mod()     # By calling the mod() funtion the model is being created and returned in the variable model
            print(model.summary())  # We will be able to see the summary of the model in our console
            model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy']) # We are now modifying the created model using the compile function.


            history = model.fit(X_train, Y_train, epochs=8, validation_data=(X_val, Y_val)) # The model is now being fit providing it with the epoch od 8

            test_loss, test_acc = model.evaluate(X_test,  Y_test, verbose=2) # The perfromance of the model is being evaluvated and test_loss and test_acc are calculated

            accuracy = history.history["accuracy"]
            val_accuracy = history.history["val_accuracy"]  # Validation accuracy and the test accuracy have been calculated

            accuracy_graph(accuracy, val_accuracy)    # Graph is being plotted be on the accuracy recieved

            test_prend = model.predict(X_test)  # The test data is being sent and the predictions are being returned in test_pred

            print(conf_matrix(Y_test, test_prend)) # Confusion matrix is being calculated for the better understanding of how the data has been trained

            model.save('model_weight_cnn_86.h5')      # The trained model is now saved of the later usage

            print(" Model has be trained and saved ")

            selection = 2     # Selection has been changed into 2 so that the next set of the code will be executed

else:
      

      model = load_model('model_weight_cnn_86.h5')    # The saved model is now being loaded again for predecting purpose

      clear()

      print("The weigths of the model have been restored from the saved file")


      testing_file = input("Enter the name of the folder which needs to be predicted:  ") # Destination path for the testing file is being provided

      test_img, ip_im_name, speed_data = test_loader(testing_file)    # The path is being given to test_loader function and it is being intergrated with the speed present in the .json file

      ip_pred = model.predict(test_img)   # The saved model will now predict the new data

      Y = timestamps(ip_pred, ip_im_name, speed_data)  # Based on the predictions we will now be creating timestamps


      ### This part of the code needs to be reviewed
      #Converting the predicted Numbers into their corresponding states "Loaded" , "Unloading" , "Inter" and "Dump"
      ip_pred_2 = [] # use the target_dict to convert the string labels to an array of integers\n",
      target_dict2 = dict([(0,'Dump'),(1,'Loaded'),(2,'Unloaded'),(3,'Inter')])
      for i in Y['Pred']:
            need = target_dict2[i]
            ip_pred_2.append(need)



      ip_pred_2, number, target_dict2 = classifier_state(ip_pred_2, Y)  # The states are being classified 

      #print( target_dict2)


      #report_1 = rep_1(ip_pred_2,Y['TS']) ## This chart needs to be shown in the report.

      start_time, end_time, time_elapsed = tsreport(Y["Pred"], Y["TS"], target_dict2) # tsreport will now generate start, end time

      Lding, Uding, Lded, Ulded, Ding = events(ip_pred_2, Y["TS"])      

      Uding_log, Lding_log, Ding_log = continuous(ip_pred_2,Y['TS'],Lding, Uding, Ding)

      events_log = evelogs(Uding_log, Lding_log, Ding_log)

      event_predictions = samp_pred(events_log, ip_pred_2, Y)

      #individual_events (events_log, Y, ip_pred_2, event_predictions)

      single_events(Lding, Uding, Lded, Ulded, Ding)  

      graphreport(Y['TS'],ip_pred_2, event_predictions, events_log, ip_pred_2, Y)

      finalreport_1(Y['TS'],ip_pred_2, event_predictions, events_log, ip_pred_2, Y)

      
      def option():
            selection = 0
            while selection not in [1,2]:
                  selection = int(input("Press 1 to send the report as email and 2 for ignore: "))
                  if selection == 1:
                        sender_address = input("Enter the email address to which the report has to be sent :")
                        emailer(sender_address)
                        print("The report has been sent as an email successfully")
                  elif selection == 2:
                        print("The process is completed")

      clear()
      
      option()







                              
                                   




                                    






      

