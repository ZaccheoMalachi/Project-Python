# opendata=open('data.csv','r')
# opendata=opendata.readlines()
# print(opendata)
from csv import *
# with open ('data.csv') as opendata:
#     data=reader(opendata,delimiter=',')
    # count=0
    # for i in data:
    #     if count==0:
    #         count+=1
    #     else:
    #         print(i)
    # data=list(data)
    # count=0
    # total=0
    # for i in data:
    #     if count==0:
    #         count+=1
    #     else:
    #         total+=(int(i[2].replace('\"','')))
    # print('All Company Is Making',total,'Milions')
with open ('newdata.csv','w') as writedata:
    datawriter=writer(writedata)
    header=('School Name', 'Type', 'Enrollment', 'Graduation Rate')
    data=   (("Acme High School", "Public", "1000", "85%"),
            ("Best Elementary", "Private", "500", "90%"),
            ("Cool College", "Public", "10000", "70%"),
            ("Dynamic Academy", "Charter", "750", "95%"),
            ("Efficient Institute", "Private", "2000", "80%"))
    datawriter.writerow(header)
    for i in data:
        datawriter.writerow(i)