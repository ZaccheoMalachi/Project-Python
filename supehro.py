import pandas as p
from matplotlib import pyplot as pp
dat=p.read_csv('her.csv')
print(dat.shape)
print(dat['Alignment'].value_counts())
gud=dat[dat['Alignment']=='good']
bed=dat[dat['Alignment']=='bad']
normal=dat[dat['Alignment']=='neutral']
print(gud,bed,normal)
print(normal.sort_values(by='Speed',ascending=False).head(30))
spidr=gud[gud['Name']=='Spider-Man']
print(spidr)
spidrlist=list(spidr.values)
spidrlist=spidrlist[0][2:8]
label=list(spidr.columns.values)
label=label[2:8]
pp.pie(spidrlist,labels=label)
pp.show()