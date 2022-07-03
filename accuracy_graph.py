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


def individual_events(events_log, Y, ip_pred_2, event_predictions):
    ss = ''
    state = []
    time_s = []
    count = -1
    for el in events_log:
        if(ss == ''):
            ss = el
            state = []
            time_s = []
            count = count +1
            plt.new_figure_manager(1)
        else:
            for i,j in zip(Y['TS'],ip_pred_2):
                if(i>=ss and i<=el):
                    state.append(j)
                    time_s.append(i)
                if(i>el):
                    break
            plt.clf()
            print(event_predictions[count])
            plt.plot(time_s,state)
            plt.title('Time Vs RO State')
            plt.xlabel('Time',fontsize=14)
            plt.ylabel('State',fontsize=14)
            plt.show()
            ss = ''
            print(event_predictions)









