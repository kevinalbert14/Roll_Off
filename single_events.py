import datetime

def single_events(Lding, Uding, Lded, Ulded, Ding):
    date = datetime.date(1, 1, 1)
    lding_counter = 0
    lding_final=datetime.timedelta(0,0,0)
    for i in Lding:
        Time_n= datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
        print(Time_n)
        if(lding_counter!=0):
            datetime1 = datetime.datetime.combine(date, lding_counter)
            datetime2 = datetime.datetime.combine(date, Time_n)
            time_elapsed =  datetime2 - datetime1
            lding_final = lding_final+time_elapsed
            #print(time_elapsed)
            lding_counter = 0
        elif(lding_counter==0):
            lding_counter = Time_n

    print("Time Spent on Loading is ", lding_final)

    uding_counter=0
    uding_final=datetime.timedelta(0,0,0)
    for i in Uding:
        Time_n= datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
        if(uding_counter!=0):
            datetime1 = datetime.datetime.combine(date, uding_counter)
            datetime2 = datetime.datetime.combine(date, Time_n)
            time_elapsed =  datetime2 - datetime1
            uding_final = uding_final+time_elapsed
            #print(time_elapsed)
            uding_counter = 0
        elif(uding_counter==0):
            uding_counter = Time_n

    print("Time Spent on Un-Loading is ", uding_final)


    lded_counter=0
    lded_final=datetime.timedelta(0,0,0)
    for i in Lded:
        Time_n= datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
        if(lded_counter!=0):
            datetime1 = datetime.datetime.combine(date, lded_counter)
            datetime2 = datetime.datetime.combine(date, Time_n)
            time_elapsed =  datetime2 - datetime1
            lded_final = lded_final+time_elapsed
            #print(time_elapsed)
            lded_counter = 0
        elif(lded_counter==0):
            lded_counter = Time_n

    print("Time Spent in Loaded state ", lded_final)


    ulded_counter=0
    ulded_final = datetime.timedelta(0,0,0)
    for i in Ulded:
        Time_n= datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
        if(ulded_counter!=0):
            datetime1 = datetime.datetime.combine(date, ulded_counter)
            datetime2 = datetime.datetime.combine(date, Time_n)
            time_elapsed =  datetime2 - datetime1
            ulded_final = ulded_final+time_elapsed
            #print(time_elapsed)
            ulded_counter = 0
        elif(ulded_counter==0):
            ulded_counter = Time_n

    print("Time Spent in Un-Loaded state is ", ulded_final)

    ding_counter=0
    ding_final = datetime.timedelta(0,0,0)
    for i in Ding:
        Time_n= datetime.time(int(i[i.find('T')+1:i.find('T')+3]),int(i[i.find('T')+3:i.find('T')+5]),int(i[i.find('T')+5:i.find('T')+7]))
        if(ding_counter!=0):
            datetime1 = datetime.datetime.combine(date, ding_counter)
            datetime2 = datetime.datetime.combine(date, Time_n)
            time_elapsed =  datetime2 - datetime1
            ding_final = ding_final+time_elapsed
            #print(time_elapsed)
            ding_counter = 0
        elif(ding_counter==0):
            ding_counter = Time_n

    print("Time Spent Dumping is ", ding_final)
    #print(Time_n)
    #print(lding_counter)
    tot_time = ding_final+uding_final+lding_final+lded_final+ulded_final
    
    print(tot_time)
        
