import seaborn as sb
import matplotlib.pyplot as mp
import pandas as p
data=p.read_csv('vacine.csv')
# mp.show()
country=data.groupby('country')['total_vaccinations'].max().sort_values(ascending=False)[10:15].index
print(country)
col=p.DataFrame(columns=data.columns)
for i in country:
    col=col.append(data.loc[data['country']==i])
print(col)
mp.figure(figsize=(20,8))
sb.lineplot(x=col['date'],y=col["daily_vaccinations_per_million"],hue=col['country'])
mp.show()