import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import plotly.graph_objects as go
import plotly.express as px


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

def graphreport(TimeStamp,Predicted_state, event_predictions, events_log, ip_pred_2, Y):
    need_predictions = []
    new_predictions = []
    new_timelog = []
    for i in event_predictions:
        need_predictions.append(i)
        need_predictions.append(i)

    for j,k in zip(events_log,need_predictions):
        if(k in ('Unloading','Dumping','Loading')):
            for h,i in zip(Predicted_state,TimeStamp):
                if(j==i):
                    new_predictions.append(h)
                    new_timelog.append(j)
                    break

    now_all_preds = []
    time_all_preds = []
    for j,k in zip(events_log,need_predictions):
        for h,i in zip(Predicted_state,TimeStamp):
            if(j==i):
                now_all_preds.append(h)
                time_all_preds.append(j)
                break

    Start_end_indicator = []
    counter = -1
    month = TimeStamp
    high_2000 = Predicted_state
    j = -1
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=month, y=high_2000, name='states',
                         line=dict(color='black', width=4)))                 

    fig.update_layout(title='State diagram of the continuous dataset With Filtered Predicted Events after post-processing',
                   xaxis_title='Timestamp',
                   yaxis_title='States')

    start_timelog = []
    end_timelog = []
    start_new_predictions = []
    end_new_predictions = []
    n_cnt = 0
    for i,j in zip(time_all_preds,now_all_preds):
        if(n_cnt%2==0):
            start_timelog.append(i)
            start_new_predictions.append(j)
    #print(i,j)
        else:
            #print('else',i,j)
            end_timelog.append(i)
            end_new_predictions.append(j)
        n_cnt=n_cnt+1

    print(end_new_predictions)

    ulding_count = 0
    ding_count = 0
    ling_count = 0
    miss_count = 0
    #print(len(start_new_predictions))
    #print(start_new_predictions)

    for k in need_predictions:
        if(k == 'Unloading'):
            ulding_count = ulding_count+1
        elif(k == 'Dumping'):
            ding_count = ding_count+1 
        elif(k == 'Loading'):
            ling_count = ling_count+1
        else:
            miss_count = miss_count+1

    Dc = "  Drop Off Count  :  "
    Pc = "  Pickup Count :  "
    DUc = "  Dumping Count :  "
    Oc = "  Other Events Count :  "
    Summary = Dc+str(ulding_count/2) +DUc +str(ding_count/2) + Pc+str(ling_count/2)+ Oc+ str(miss_count/2)
    print(Summary)

    fig.add_trace(go.Scatter(x=start_timelog, y= start_new_predictions ,
                    mode='markers',
                    name='start of event'))


    fig.add_trace(go.Scatter(x=end_timelog, y= end_new_predictions ,
                    mode='markers',
                    name='end of event'))


    fig.update_layout(title='State diagram of the continuous dataset With All Predicted Events before post-processing',
                   xaxis_title='Timestamp',
                   yaxis_title='States')

    fig.show()
    print("Summary ||  ",Summary)

    count = 0
    ses = []
    speed_log = []
    event_predictions = []
    now = ''
    for i in events_log:
        for j,k,sp in zip(ip_pred_2,Y['TS'],Y['Speed']):
            if(i==k and j in ('Loaded','Unloaded')):
                ses.append(j)
                speed_log.append(sp)
                break

    ss = ''
    for i,j,sp in zip(ses,events_log,speed_log):
        if(ss == ''):
            ss =i
            st=j
            sp1=sp
        else:
            if(sp1>10 or sp>10):
                print('Start time is',st,'state is',ss,' and the speed is',sp1,'End time is',j,'State is',i,'Speed of truck is',sp,'No event as truck is moving')
                event_predictions.append('Truck is Moving')
            elif(ss == 'Loaded' and i == 'Unloaded'):
                print('Start time is',st,'state is',ss,' and the speed is',sp1,'End time is',j,'State is',i,'Speed of truck is',sp,'The activity performed in the sample is predicted to be UNLOADING')
                event_predictions.append('Unloading')
            elif(ss == 'Unloaded' and i == 'Loaded'):
                print('Start time is',st,'state is',ss,' and the speed is',sp1,'End time is',j,'State is',i,'Speed of truck is',sp,'The activity performed in the sample is predicted to be LOADING')
                event_predictions.append('Loading')
            elif(ss == 'Loaded' and i == 'Loaded'):
                flag_now = 0
                for j_now,k_now,sp_now in zip(ip_pred_2,Y['TS'],Y['Speed']):
                    if(k_now>=st and k_now <=j):
                        if(j_now=='Dump'):
                            flag_now = 1
                            break
                if(flag_now==1):
                    event_predictions.append('Dumping')
                    print('Start time is',st,'state is',ss,' and the speed is',sp1,'End time is',j,'State is',i,'Speed of truck is',sp,'The activity performed in the sample is predicted to be DUMPING')
                else:
                    event_predictions.append('No productive Event')

            else:
                event_predictions.append('No productive Event')

            ss=''
            now = ''
    
    