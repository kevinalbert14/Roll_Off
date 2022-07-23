def classifier_state(ip_pred_2, Y):
      ip_pred_2 = [] #check this
      need_now = []
      target_dict2 = dict([(0,'Dump'),(1,'Loaded'),(2,'Unloaded'),(3,'Inter'),(4,'Loading'),(5,'Unloading'),(6,'Undefined 1'),(7,'Undefined 2'),(8,'Undefined 3')])
      n2 = []
      number = 0
      ss=0
      for i,times in zip(Y['Pred'],Y['TS']):
            need = target_dict2[i]
            if(need == target_dict2[0] or need == target_dict2[1] or need == target_dict2[2]):
                  ip_pred_2.append(need)
                  ss=need
                  n2 = need # n2 represent previous state, used from the second iteration
            elif(need == target_dict2[3]): # If we get Inter, the loop is initiated
                  if(n2 == target_dict2[1]): # if the previous state is "Loaded" we change "Inter" to "Unloading"
                     ip_pred_2.append(target_dict2[5])
                     n2=target_dict2[5]
                  elif(n2 == target_dict2[2]): # if the previous state is "Unloaded" we change "Inter" to "Loading"
                        ip_pred_2.append(target_dict2[4])
                        n2=target_dict2[4]
                  elif(n2==target_dict2[0]): # if previous state is dump
                        #print(Y['Pred']) 
                        per = [0,0,0,0]
                        for i in Y['Pred']:
                              if(i==0):
                                    per[0] = per[0] + 1
                              elif(i==1):
                                    per[1] = per[1] + 1
                              elif(i==2):
                                    per[2] = per[2] + 1
                              else:
                                    per[3] = per[3] + 1
                        #print(per[0]/per[3]) # calculating ratio between dump and inter in the file
                        if(per[0]/per[3]>=1): # we see more dump than inter images (classify as dump)
                              ip_pred_2.append(target_dict2[0])
                              n2=target_dict2[0]
                        elif(per[0]/per[3]<1): # we see more inter images as inter
                              for now,nows in zip(Y['Pred'],Y['TS']): # we loop to find the last stable state before the current timestamp
                                    if(nows<=times and now == 1):
                                          ss=target_dict2[1]
                                    elif(nows<=times and now == 2):
                                          ss=target_dict2[2]
                                    elif(nows>=times):
                                          break
                                    elif(nows<times and now == 3 or now == 0):
                                          nows = nows #continue looping no action needed
                                    else:
                                          print('undefined state')
                              if(ss==target_dict2[1]): #if last stable state is loaded then UNLOADING
                                    ip_pred_2.append(target_dict2[5])
                              elif(ss==target_dict2[2]): #if last stable state is unloaded then LOADING
                                    ip_pred_2.append(target_dict2[4]) 
                              else:
                                    print('no action')
                  #n2=target_dict2[0]
                  elif(n2 ==target_dict2[5] or n2 == target_dict2[4]): # if the previous state is "Loadng" or "Unloading" we retain the same value
                        ip_pred_2.append(n2)  
                  elif(n2 == target_dict2[3]): # If the previous state is "Inter" we raise a error
                        ip_pred_2.append(target_dict2[7])
                  elif(n2==[]): #If a dataset starts with "Inter", we correct it in the for loop using either "Loading" or "Unloading", based on the lowest timestamp of "Loaded" or "Unloaded" available 
                        for i,j in zip(Y['Pred'],Y['TS']):
                              if(i==1 or i==2):
                                    need_now=i
                                    #print('Inside if',i)
                                    break
                        if(need_now==1):
                              ip_pred_2.append(target_dict2[4])
                        elif(need_now==2):
                              ip_pred_2.append(target_dict2[5])
                        else:
                              ip_pred_2.append(target_dict2[8])
                  else:
                       ip_pred_2.append(target_dict2[6])
      return ip_pred_2, number, target_dict2