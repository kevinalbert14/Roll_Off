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

def events(pred, tsp):
    a = 0
    data = datetime.date(1, 1, 1)
    Lding = []
    Uding = []
    Ding = []
    Lded = []
    Ulded = []
    ding_s = 0
    lding_s = 0
    uding_s = 0
    lded_s = 0
    ulded_s = 0
    for i,j in zip(pred, tsp):
        a = j
        if(i =='Unloading' and uding_s == 0):
            Uding.append(j)
            uding_s = 1
            if(lding_s != 0):
                Lding.append(j)
                lding_s = 0
            elif(ding_s!=0):
                Ding.append(j)
                ding_s = 0
            elif(lded_s != 0):
                Lded.append(j)
                lded_s = 0
            elif(ulded_s!=0):
                Ulded.append(j)
                ulded_s = 0
            else:
                print('No Acttion')

        if(i=='Loading' and lding_s ==0):
            print('Loading start',j)
            Lding.append(j)
            lding_s = 1
            if(uding_s !=0):
                print('Unloading end',j)
                Uding.append(j)
                uding_s = 0
            elif(ding_s!=0):
                print('Dumping end',j)
                Ding.append(j)
                ding_s = 0
            elif(lded_s!=0):
                print('Loaded end',j)
                Lded.append(j)
                lded_s = 0
            elif(ulded_s!=0):
                print('Unloaded end',j)
                Ulded.append(j)
                ulded_s = 0
            else:
                print('No Acttion')

        if(i=='Unloaded' and ulded_s ==0):
            print('Unloaded start',j)
            Ulded.append(j)
            ulded_s = 1
            if(uding_s !=0):
                print('Unloading end',j)
                Uding.append(j)
                uding_s = 0
            elif(ding_s!=0):
                print('Dumping end',j)
                Ding.append(j)
                ding_s = 0
            elif(lded_s!=0):
                print('Loaded end',j)
                Lded.append(j)
                lded_s = 0
            elif(lding_s!=0):
                print('Loading end',j)
                Lding.append(j)
                lding_s= 0
            else:
                print('No Action')

        if(i=='Loaded' and lded_s ==0):
            print('loaded start',j)
            Lded.append(j)
            lded_s = 1
            if(uding_s !=0):
                print('Unloading end',j)
                Uding.append(j)
                uding_s = 0
            elif(ding_s!=0):
                print('Dumping end',j)
                Ding.append(j)
                ding_s = 0
            elif(ulded_s!=0):
                print('Unloaded end',j)
                Ulded.append(j)
                ulded_s= 0
            elif(lding_s!=0):
                print('Loading end',j)
                Lding.append(j)
                lding_s= 0
            else:
                print('No Action')

        if(i=='Dump' and ding_s ==0):
            print('Dumping start',j)
            Ding.append(j)
            ding_s = 1
            if(uding_s !=0):
                print('Unloading end',j)
                Uding.append(j)
                uding_s = 0
            elif(lded_s!=0):
                print('Loaded end',j)
                Lded.append(j)
                lded_s= 0
            elif(ulded_s!=0):
                print('Unloaded end',j)
                Ulded.append(j)
                ulded_s= 0
            elif(lding_s!=0):
                print('Loading end',j)
                Lding.append(j)
                lding_s= 0
            else:
                print('No Acttion')

    print("Loaded_start",lded_s)
    print("Unloaded_start",ulded_s)
    print("Loading_start",lding_s)
    print("Unloading_start",uding_s)
    print("Dumping_start",ding_s) 

    if(lded_s ==1):
        print('Loaded End',a)
        Lded.append(j)
    elif(ulded_s ==1):
        print('Unloaded End',a)
        Ulded.append(j)
    elif(lding_s ==1):

        print('Loading End',a)
        Lding.append(j)
    elif(uding_s ==1):
        print('Unloading End',a)
        Uding.append(j)
    elif(ding_s ==1):
        print('Dumping End',a)
        Ding.append(j)
    else:
        print("Complete")

    return Lding, Uding, Lded, Ulded, Ding







