# -*- coding: utf-8 -*-
from datetime import timedelta
from datetime import date as timedate

def textProcess(OCRfile):
    convictionList=[]
    OCRfile=OCRfile.splitlines()
    date=False
    dispo=False
    cnt=0
    offense=False
    for i in OCRfile:
        cnt+=1
        
        if 'court.' in i.lower() or 'court:' in i.lower():
            date=OCRfile[cnt][0:9]
            print (date)
        if "dispo:convicted" in i.lower():
            dispo=True
            offense=OCRfile[cnt-2]
            
        if dispo==True:
            if "sen:" in i.lower():
               
                convictionList.append({'sentenceLength' : senToNum(i), 'date' : [int(date[0:5]),int(date[5:7]),int(date[7:])], 'penalCode' : offense})
    print(convictionList)
    return convictionList
def senToNum(sentence):
    length=0
    punishments=sentence.split(",")
    for part in punishments:
        part=part.split()
        for s in part:
            if s.isdigit(): #assuming all sentances are the same, fulfilled sequentially, and all numbers are sentance lengths
                if part[part.index(s)+1]=="WEEK" or part[part.index(s)+1]=="WEEKS":
                    length+=(int(s)*7)
                elif part[part.index(s)+1]=="MONTHS" or part[part.index(s)+1]=="MONTH":
                        length+=(int(s)*30.5) #assuming months are on average 30.5 days
                elif part[part.index(s)+1]=="YEAR" or part[part.index(s)+1]=="YEARS":
                        length+=(int(s)*365)
                elif part[part.index(s)+1]=="DAY" or part[part.index(s)+1]=="DAYS":
                        length+=int(s)
                
    return timedelta(days=length)
                    
                
                    
                
def main():
    textProcess("COURT: NAM: 2 \n 20011102 CASC SANTA ANA \n CNTIOI \n11364 HS-POSSESS CONTROL SUBSTANCE PARAPHERNA \n DISPO:CONVICTED \n CONV STATU51MISDEMEANOR \n SEN: 3 YEARS PROBATION,30 DAYS JAIL \n COM: DCN-T1139453580130‘J1172")

main()
             
