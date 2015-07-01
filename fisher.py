# -*- coding: utf-8 -*-
"""
Citation: N. Ahmad, S. Derrible, T. Eason, and H. Cabezas, “USING FISHER INFORMATION IN BIG DATA.” 
(URL will be updated when finalized)
"""

import csv
import math
import matplotlib.pyplot as plt


def FI(f_name,step,step_1):
    
    out=open(f_name+'.csv','rb')
    data=csv.reader(out)
    Data=[]
        
    for row in data:
        Data.append(row)
            
    out.close()
    
    Data_num=[]
    Time=[]
    
    for row in Data:
        Time.append(row[0])
        temp=[]
        for i in range(1,len(row)):
            if row[i]=='':
                temp.append(0)
            else:
                temp.append(float(row[i]))
        Data_num.append(temp)
    
    
    out=open('sost.csv','rb')
    data=csv.reader(out)
    Data=[]
        
    for row in data:
        Data.append(row)
            
    out.close()
    
    sost=[]
    
    for i in Data[0]:
        sost.append(eval(i))
        

    
    FI_final=[]
    k_init=[]
    for i in range(0,len(Data_num),step_1):
        
        Data_win=Data_num[i:i+step]
       
        if len(Data_win)==step:
            Bin=[]
            for i in Data_win:
                Bin_temp=[]
                
                for j in Data_win:
                    if i==j:
                        Bin_temp.append('I')
                    else:
                        Bin_temp_1=[]
                        for k in range(len(j)):
                            if (abs(i[k]-j[k]))<=sost[k]:
                                Bin_temp_1.append(1)
                            else:
                                Bin_temp_1.append(0)
                                
                        Bin_temp.append(sum(Bin_temp_1))
                        
                Bin.append(Bin_temp)
                
            
            FI=[]
            for tl in range(1,101):
                tl1=len(sost)*float(tl)/100
                Bin_1=[]
                Bin_2=[]
                
                for j in range(len(Bin)):
                    if j not in Bin_2:
                       
                        Bin_1_temp=[j]
                        for i in range(len(Bin[j])):
                            if Bin[j][i]!='I' and Bin[j][i]>=tl1 and i not in Bin_2:
                                Bin_1_temp.append(i)
                                
                        Bin_1.append(Bin_1_temp)
                        Bin_2.extend(Bin_1_temp)
                    
               
                
                prob=[0]
                for i in Bin_1:
                    prob.append(float(len(i))/len(Bin_2))
                    
                prob.append(0)
                
               
                prob_q=[]
                for i in prob:
                    prob_q.append(math.sqrt(i))
                    
               
                
                FI_temp=0
                for i in range(len(prob_q)-1):
                    FI_temp+=(prob_q[i]-prob_q[i+1])**2
                FI_temp=4*FI_temp    
                
                FI.append(FI_temp)
                
          
            for i in range(len(FI)):
                if FI[i]!=8.0:
                    k_init.append(FI.index(FI[i]))
                    break
            
                
            FI_final.append(FI)
  
        
    for i in range(0,len(FI_final)):
        FI_final[i].append(float(sum(FI_final[i][min(k_init):len(FI_final[i])]))/len(FI_final[i][min(k_init):len(FI_final[i])]))
        FI_final[i].append(Time[(i*step_1+step)-1])
    
    out=open("FI.csv","wb")
    new=csv.writer(out)
    for i in FI_final:
        new.writerow(i)
        
    out.close()
    
    plt.plot(range(step,len(FI_final)+step),[i[-2] for i in FI_final ],
    'b',label='FI')
    plt.ylim(0,8)
    plt.ylabel('Fisher Information')
    plt.xlabel('Time')
    plt.tight_layout()
  


            
            
    