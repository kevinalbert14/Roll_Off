import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def accuracy_graph(accuracy, val_accuracy):
    plt.plot(accuracy, label='accuracy')
    plt.plot(val_accuracy, label = 'val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legend(loc='lower right')
    return plt.show()



def rep_1(prediction_state, tsp):
    plt.plot(tsp, prediction_state)
    plt.title('Time Vs RO State')
    plt.xlabel('Time', fontsize = 14)
    plt.ylabel('State', fontsize = 14)
    return plt.show()