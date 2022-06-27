import datetime
from tkinter import Y

def tsreport(pred, tsp, target_dict2):
    Start_state = []
    End_state = []
    Dump_flag = 0
    date = datetime.date(1,1,1)
    for i,j in zip(pred, tsp):
        if(i == 1 or i == 2):
            need_now = i
            need_now2 = j
            break
    strt = ("Start state is", target_dict2[i], "and the timestamp is", j)
    Start_state = target_dict2[i]
    #print(int(str(j[6:])))
    start_time = int(j[j.find('T')+1:j.find('T')+3]),int(j[j.find('T')+3:j.find('T')+5]),int(j[j.find('T')+5:j.find('T')+7])
    #print(int(str(j[9:11])),int(str(j[11:13])))#,int(str(j[13:])))
    StartTime= datetime.time(int(j[j.find('T')+1:j.find('T')+3]),int(j[j.find('T')+3:j.find('T')+5]),int(j[j.find('T')+5:j.find('T')+7]))
    datetime1 = datetime.datetime.combine(date, StartTime)
    #print(datetime1)


    for i,j in zip(pred, tsp):
        if( i == 1 or i == 2):
            need_now = i
            need_now2 = j
        if(i == 0):
            Dump_flag = 1
    end = ("End State is '", target_dict2[i],"' and the time stamp is ",j)
    End_state = target_dict2[i]
    End_time = int(j[j.find('T')+1:j.find('T')+3]),int(j[j.find('T')+3:j.find('T')+5]),int(j[j.find('T')+5:j.find('T')+7])
    EndTime= datetime.time(int(j[j.find('T')+1:j.find('T')+3]),int(j[j.find('T')+3:j.find('T')+5]),int(j[j.find('T')+5:j.find('T')+7]))
    datetime2 = datetime.datetime.combine(date, EndTime)

    time_elapsed = datetime2 - datetime1
    elspd = ('Time enlapsed between Start and End state',time_elapsed)
    return strt, end, elspd









