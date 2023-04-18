#Question: Given a list of json string, json string will have two field, severviceName and errorType . Write a python script to find out service name which has the highest warning errorType.

 


inputData = [{"severviceName":"gprs","errorType":"warning"},
             {"severviceName":"gprs","errorType":"critical"},
             {"severviceName":"gprs","errorType":"warning"},
             {"severviceName":"gprs","errorType":"warning"},
             {"severviceName":"text","errorType":"warning"},
             {"severviceName":"voice","errorType":"warning"},
             {"severviceName":"voice","errorType":"critical"}]

 


highest={}

for x in inputData:
    #print(x)
    if x['errorType']=='warning':
        if x['severviceName'] in highest:
            highest[x['severviceName']]+=1
        else:
            highest[x['severviceName']]=1
highest_service=max(highest,key=highest.get)
print(highest_service)
        

#print(highest) 
    


