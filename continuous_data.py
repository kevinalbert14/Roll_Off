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

    return Uding_log, Lding_log, Ding_log
















