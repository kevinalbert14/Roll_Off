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
from accuracy_graph import accuracy_graph, rep_1, individual_events
from conf_matrix import conf_matrix
from classifier_state import classifier_state
from tsreport import events, tsreport
from continuous_data import continuous, evelogs, samp_pred


target_dict = dict([("Dump", 0),("Loaded",1),("Unloaded",2),("Inter",3)])

images, labels = image_load()

labels_int = [] # use the target_dict to convert the string labels to an array of integers
for i in labels:
      n_key = target_dict[i]
      labels_int.append(n_key)
labels_int = np.array(labels_int)

X_train, Y_train, X_test, Y_test, X_val, Y_val = splitting_train_test(images, labels_int)

model = mod()
print(model.summary())
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


history = model.fit(X_train, Y_train, epochs=12,
                    validation_data=(X_val, Y_val))

test_loss, test_acc = model.evaluate(X_test,  Y_test, verbose=2)

accuracy = history.history["accuracy"]
val_accuracy = history.history["val_accuracy"]

accuracy_graph(accuracy, val_accuracy)

test_prend = model.predict(X_test)

print(conf_matrix(Y_test, test_prend))

testing_file = input("Enter the destiation of the testing file")

test_img, ip_im_name, speed_data = test_loader(testing_file)

ip_pred = model.predict(test_img)

Y = timestamps(ip_pred, ip_im_name, speed_data)

### This part of the code needs to be reviewed
ip_pred_2 = []
target_dict2 = dict([("Dump", 0),("Loaded",1),("Unloaded",2),("Inter",3)])
for i in Y['Pred']:
      need = target_dict2[i]
      ip_pred_2.append(need)


ip_pred_2, number, target_dict2 = classifier_state(ip_pred_2, Y)


report_1 = rep_1(ip_pred_2,Y['TS']) ## This chart needs to be shown in the report.

start_time, end_time, time_elapsed = tsreport(ip_pred_2, Y["TS"], target_dict2)

Lding, Uding, Lded, Ulded, Ding = events(ip_pred_2, Y["TS"])

Uding_log, Lding_log, Ding_log = continuous(ip_pred_2,Y['TS'],Lding, Uding, Ding)

events_log = evelogs(Uding_log, Lding_log, Ding_log)

event_predictions = samp_pred(events_log, ip_pred_2, Y)

individual_events (events_log, Y, ip_pred_2, event_predictions)







                              
                                   




                                    






      

