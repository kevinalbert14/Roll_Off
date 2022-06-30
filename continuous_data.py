# only applicable for continuous daatasets
# identify individual events from loading, Unloading and Dumping

import datetime 


def continuous(pred, tsps, Lding, Uding, Ding):
    date = datetime.date(1, 1, 1)
    now_1 = 0
    old_v = 0
    time_taken = 0
    ocnt = 0
    Lding_log = []
    Uding_log = []
    Ding_log = []
    events_log = []
    # identify individual events from loading
    for i in Lding:
        if(now_1 == 0):
            old_v = datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
            datetime1 = datetime.datetime.combine(date, old_v)
            now_1=1
            for j,k in zip(pred,tsps):
                if(k<=i and j in ('Loaded','Unloaded')):    #need to be reviewed
                    ocnt = k
                    #print(ocnt)
                elif(k>i):
                    break
                else:
                    ocnt = ocnt
            Lding_log.append(ocnt)

        else:
            time_taken = datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))  
            datetime2 = datetime.datetime.combine(date, time_taken)
            for j,k in zip(pred,tsps):
                if(k>=i and j in ('Loaded','Unloaded')):
                    ocnt = k
                    break
                elif(k<i):
                    ocnt = ocnt
                else:
                    ocnt = ocnt
            Lding_log.append(ocnt)
            time_elapsed =  datetime2 - datetime1
            now_1=0

# identify individual events from Unloading
    for i in Uding:
        if(now_1 == 0):
            old_v = datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
            datetime1 = datetime.datetime.combine(date, old_v)
            now_1=1
            for j,k in zip(pred,tsps):
                if(k<=i and j in ('Loaded','Unloaded')):
                    ocnt = k
                    #print(ocnt)
                elif(k>i):
                    break
                else:
                    ocnt = ocnt
            Uding_log.append(ocnt)   

        else:
            time_taken = datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))  
            datetime2 = datetime.datetime.combine(date, time_taken)
            for j,k in zip(pred,tsps):
                if(k>=i and j in ('Loaded','Unloaded')):
                    ocnt = k
                    break
                elif(k<i):
                    ocnt = ocnt
            Uding_log.append(ocnt)
            time_elapsed =  datetime2 - datetime1
            now_1=0

# identify individual events from Dumping

    for i in Ding:
        if(now_1 == 0):
            old_v = datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
            datetime1 = datetime.datetime.combine(date, old_v)
            now_1=1
            for j,k in zip(pred,tsps):
                if(k<=i and j in ('Loaded','Unloaded')):
                    ocnt = k
                    #print(ocnt)
                elif(k>i):
                    break
                else:
                    ocnt = ocnt
            Ding_log.append(ocnt)

        else:
            time_taken = datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))  
            datetime2 = datetime.datetime.combine(date, time_taken)
            for j,k in zip(pred,tsps):
                if(k>=i and j in ('Loaded','Unloaded')):
                    ocnt = k
                    break
                elif(k<i):
                    ocnt = ocnt
                else:
                    ocnt = ocnt
            Ding_log.append(ocnt)
            time_elapsed =  datetime2 - datetime1
            now_1=0

    return Uding_log, Lding_log, Ding_log, events_log


def evelogs(Uding_log, Lding_log, Ding_log):
    # only applicable for continuous datasets
    flag = 0
    # combining individual logs into one deduped list
    events_log = []
    count = 0
    aler = 0
    for i in Uding_log:
        if(count%2==0):
            if(i in events_log):
                indices = [Z for Z, Y in enumerate(events_log) if Y == i]
                for this in indices:
                    if(this%2==0):
                        aler = 1
                        break
                if(aler == 0):
                    events_log.append(i)
            else:
                events_log.append(i)
        else:
            if(aler==0):
                events_log.append(i)
            else:
                aler=0
        count=count+1
        #print(events_log)
        #print(i)

    count = 0
    aler = 0
    for i in Lding_log:
        if(count%2==0):
            if(i in events_log):
                indices = [Z for Z, Y in enumerate(events_log) if Y == i]
                for this in indices:
                    if(this%2==0):
                        aler = 1
                        break
                if(aler == 0):
                    events_log.append(i)
            else:
                events_log.append(i)
        else:
            if(aler==0):
                events_log.append(i)
            else:
                aler=0
        count=count+1
        #print(events_log)
        #print(i)

    count = 0
    aler = 0
    for i in Ding_log:
        if(count%2==0):
            if(i in events_log):
                indices = [Z for Z, Y in enumerate(events_log) if Y == i]
                for this in indices:
                    if(this%2==0):
                        aler = 1
                        break
                if(aler == 0):
                    events_log.append(i)
            else:
                events_log.append(i)
        else:
            if(aler==0):
                events_log.append(i)
            else:
                aler=0
        count=count+1
        #print(events_log)
        #print(i)
    return events_log


def samp_pred(events_log, ip_pred_2, Y):
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
    print(events_log)
    
    # predict each event using the basic prediction
    ss = ''
    print(ses)
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
                print('Start time is',st,'state is',ss,' and the speed is',sp1,'End time is',j,'State is',i,'Speed of truck is',sp,'The activity performed in the sample is predicted to be DUMPING')
                event_predictions.append('Dumping')
            else:
                print('Start time is',st,'state is',ss,' and the speed is',sp1,'End time is',j,'State is',i,'Speed of truck is',sp,'No productive action was identified here')
                event_predictions.append('No productive Event')
            ss=''
            now = ''

    return event_predictions




















