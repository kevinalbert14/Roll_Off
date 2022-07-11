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
    fig.add_trace(go.Scatter(x=month, y=high_2000, name='states',line=dict(color='black', width=4)))                 

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
    fig.write_html("all.html")
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
    #print(ses)
    file = open("all.html","w")

    fig.write_html(file)
    file.write("""<h2> Summary </h2>""")
    file.write("<h4>"+Summary+"</h4>")

    now_text = """
    <style>
    table, th, td {
        border:1px solid black;
    }
    </style>

    <table style="width:100%">
        <tr>
            <td>Start Time Stamp</td>
            <td>Start State</td>
            <td>Start Speed</td>
            <td>End Time Stamp</td>
            <td>End State</td>
            <td>End Speed</td>
            <td>Predicted Activity</td>
        </tr>
    """
    file.write(now_text)
    for i,j,sp in zip(ses,events_log,speed_log):
        flag_now = 0
        if(ss == ''):
            ss =i
            st=j
            sp1=sp
        else:
            if(sp1>10 or sp>10):
            #now_text = ('Start time is '+str(st)+' state is '+str(ss)+' and the speed is '+str(sp1)+' End time is '+str(j)+' State is '+str(i)+' Speed of truck is '+str(sp)+' No event as truck is moving ')
                now_text = """  <tr>
                <td>"""+st+"""</td>
                <td>"""+ss+"""</td>
                <td>"""+str(sp1)+"""</td>
                <td>"""+j+"""</td>
                <td>"""+i+"""</td>
                <td>"""+str(sp)+"""</td>
                <td>No event as truck is moving </td>
                </tr>"""
                file.write(now_text)
                event_predictions.append('Truck is Moving')
            elif(ss == 'Loaded' and i == 'Unloaded'):
                flag_now = 0
                for j_now,k_now,sp_now in zip(ip_pred_2,Y['TS'],Y['Speed']):
                    if(k_now>=st and k_now <=j):
                        if(j_now=='Unloading'):
                            flag_now = 1
                            break
                if(flag_now==1):
                    #now_text=('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'The activity performed in the sample is predicted to be UNLOADING')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> Unloading </td>
                    </tr>"""
                    file.write(now_text)
                    event_predictions.append('Unloading')
                else:
                    #now_text=str('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+' No productive Event')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> No Productive Event </td>
                    </tr>"""
                    file.write(now_text)
                    event_predictions.append('No productive Event')
            elif(ss == 'Unloaded' and i == 'Loaded'):
                flag_now = 0
                for j_now,k_now,sp_now in zip(ip_pred_2,Y['TS'],Y['Speed']):
                    if(k_now>=st and k_now <=j):
                        if(j_now=='Loading'):
                            flag_now = 1
                            break
                if(flag_now==1):
                    #now_text = str('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'The activity performed in the sample is predicted to be LOADING')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> Loading </td>
                    </tr>"""
                    file.write(now_text)
                    event_predictions.append('Loading')
                else:
                    #now_text = str('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+' No productive Event')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> No Productive Event </td>
                    </tr>"""
                    file.write(now_text)
                    event_predictions.append('No productive Event')
            elif(ss == 'Loaded' and i == 'Loaded'):
                flag_now = 0
                for j_now,k_now,sp_now in zip(ip_pred_2,Y['TS'],Y['Speed']):
                    if(k_now>=st and k_now <=j):
                        if(j_now=='Dump'):
                            flag_now = 1
                            break
                if(flag_now==1):
                    event_predictions.append('Dumping')
                    #now_text = ('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'The activity performed in the sample is predicted to be DUMPING')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> Dumping </td>
                    </tr>"""
                    file.write(now_text)
                else:
                    event_predictions.append('No productive Event')
            else:
                #file.write('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'No productive action was identified here')
                now_text = """  <tr>
                <td>"""+st+"""</td>
                <td>"""+ss+"""</td>
                <td>"""+str(sp1)+"""</td>
                <td>"""+j+"""</td>
                <td>"""+i+"""</td>
                <td>"""+str(sp)+"""</td>
                <td> No Productive Event </td>
                </tr>"""
                file.write(now_text)
                event_predictions.append('No productive Event')
            ss=''
            now = ''

    file.write("</table>")
    file.close()
                
                

    

def finalreport_1(TimeStamp,Predicted_state, event_predictions, events_log, ip_pred_2, Y):

    need_predictions = []
    new_predictions = []
    new_timelog = []
    new_activity = []
    for i in event_predictions:
        need_predictions.append(i)
        need_predictions.append(i)
    for j,k in zip(events_log,need_predictions):
        if(k in ('Unloading','Dumping','Loading')):
            for h,i in zip(Predicted_state,TimeStamp):
                if(j==i):
                    new_predictions.append(h)
                    new_timelog.append(j)
                    new_activity.append(k)
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
    for i in events_log:
        counter=counter+1
    start_timelog = []
    start_new_predictions = []
    end_timelog = []
    end_new_predictions = []
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=month, y=high_2000, name='states',
                         line=dict(color='black', width=4)))
    n_cnt = 0
    for i,j in zip(new_timelog,new_predictions):
        if(n_cnt%2==0):
            start_timelog.append(i)
            start_new_predictions.append(j)
        else:
            end_timelog.append(i)
            end_new_predictions.append(j)
        n_cnt=n_cnt+1


    fig.add_trace(go.Scatter(x=start_timelog, y= start_new_predictions ,
                    mode='markers',
                    name='start of event'))


    fig.add_trace(go.Scatter(x=end_timelog, y= end_new_predictions ,
                    mode='markers',
                    name='end of event'))
    
    ulding_count = 0
    ding_count = 0
    ling_count = 0
    miss_count = 0

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
    Summary = Dc+str(ulding_count/2) +DUc +str(ding_count/2) + Pc+str(ling_count/2)

    fig.update_layout(title='State diagram of the continuous dataset With Filtered Predicted Events after post-processing ||  ',
                   xaxis_title='Timestamp',
                   yaxis_title='States')

    fig.show()
    fig.write_html("valid.html")
    print("Summary || ",Summary)

    # applicable for continuous datasets

    # Identifying the speed during the start and end timestamp (this will later be used to find and rejects misclassifications)

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
#print(events_log)


    # predict each event using the basic prediction flow
    ss = ''
    #print(ses)
    file = open("valid.html","w")

    fig.write_html(file)
    file.write("""<h2> Summary </h2>""")
    file.write("<h4>"+Summary+"</h4>")

    now_text = """
    <style>
    table, th, td {
        border:1px solid black;
    }
    </style>

    <table style="width:100%">
        <tr>
            <td>Start Time Stamp</td>
            <td>Start State</td>
            <td>Start Speed</td>
            <td>End Time Stamp</td>
            <td>End State</td>
            <td>End Speed</td>
            <td>Predicted Activity</td>
        </tr>
    """
    file.write(now_text)
    for i,j,sp in zip(ses,events_log,speed_log):
        flag_now = 0
        if(ss == ''):
            ss =i
            st=j
            sp1=sp
        else:
            if(sp1>10 or sp>10):
            #now_text = ('Start time is '+str(st)+' state is '+str(ss)+' and the speed is '+str(sp1)+' End time is '+str(j)+' State is '+str(i)+' Speed of truck is '+str(sp)+' No event as truck is moving ')
                now_text = """  <tr>
                <td>"""+st+"""</td>
                <td>"""+ss+"""</td>
                <td>"""+str(sp1)+"""</td>
                <td>"""+j+"""</td>
                <td>"""+i+"""</td>
                <td>"""+str(sp)+"""</td>
                <td>No event as truck is moving </td>
                </tr>"""
                #file.write(now_text)
                event_predictions.append('Truck is Moving')
            elif(ss == 'Loaded' and i == 'Unloaded'):
                flag_now = 0
                for j_now,k_now,sp_now in zip(ip_pred_2,Y['TS'],Y['Speed']):
                    if(k_now>=st and k_now <=j):
                        if(j_now=='Unloading'):
                            flag_now = 1
                            break
                if(flag_now==1):
                    #now_text=('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'The activity performed in the sample is predicted to be UNLOADING')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> Unloading </td>
                    </tr>"""
                    file.write(now_text)
                    event_predictions.append('Unloading')
                else:
                    #now_text=str('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+' No productive Event')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> No Productive Event </td>
                    </tr>"""
                    #file.write(now_text)
                    event_predictions.append('No productive Event')
            elif(ss == 'Unloaded' and i == 'Loaded'):
                flag_now = 0
                for j_now,k_now,sp_now in zip(ip_pred_2,Y['TS'],Y['Speed']):
                    if(k_now>=st and k_now <=j):
                        if(j_now=='Loading'):
                            flag_now = 1
                            break
                if(flag_now==1):
                    #now_text = str('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'The activity performed in the sample is predicted to be LOADING')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> Loading </td>
                    </tr>"""
                    file.write(now_text)
                    event_predictions.append('Loading')
                else:
                    #now_text = str('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+' No productive Event')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> No Productive Event </td>
                    </tr>"""
                    #file.write(now_text)
                    event_predictions.append('No productive Event')
            elif(ss == 'Loaded' and i == 'Loaded'):
                flag_now = 0
                for j_now,k_now,sp_now in zip(ip_pred_2,Y['TS'],Y['Speed']):
                    if(k_now>=st and k_now <=j):
                        if(j_now=='Dump'):
                            flag_now = 1
                            break
                if(flag_now==1):
                    event_predictions.append('Dumping')
                    #now_text = ('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'The activity performed in the sample is predicted to be DUMPING')
                    now_text = """  <tr>
                    <td>"""+st+"""</td>
                    <td>"""+ss+"""</td>
                    <td>"""+str(sp1)+"""</td>
                    <td>"""+j+"""</td>
                    <td>"""+i+"""</td>
                    <td>"""+str(sp)+"""</td>
                    <td> Dumping </td>
                    </tr>"""
                    file.write(now_text)
                else:
                    event_predictions.append('No productive Event')
            else:
                #file.write('Start time is'+str(st)+'state is'+str(ss)+' and the speed is'+str(sp1)+'End time is'+str(j)+'State is'+str(i)+'Speed of truck is'+str(sp)+'No productive action was identified here')
                now_text = """  <tr>
                <td>"""+st+"""</td>
                <td>"""+ss+"""</td>
                <td>"""+str(sp1)+"""</td>
                <td>"""+j+"""</td>
                <td>"""+i+"""</td>
                <td>"""+str(sp)+"""</td>
                <td> No Productive Event </td>
                </tr>"""
                file.write(now_text)
                event_predictions.append('No productive Event')
            ss=''
            now = ''

    file.write("</table>")
    file.close()
    