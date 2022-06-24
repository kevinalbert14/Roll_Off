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