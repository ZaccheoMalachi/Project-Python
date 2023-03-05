import pandas as pd
# data={
#     'Watermelon':   [10.4315, 6.7189, 11.9632, 12.2851, 9.0298, 6.5782, 8.7653, 5.7734, 13.9019, 6.1342, 10.2501, 14.3746],
#     'Apple':        [5.1912, 3.8921, 4.3743, 3.6569, 4.8157, 4.0086, 4.3084, 5.4372, 5.5938, 5.1129, 2.5218, 2.9061],
#     'Banana':       [5.3621, 6.2469, 5.1527, 6.8332, 5.8196, 6.4168, 5.5937, 6.0813, 5.9329, 6.9281, 4.7843, 4.3126]
# }
# months=[
#     'January', 'February', 'March', 'April', 'May', 'June', 'July',
#     'August', 'September', 'October', 'November', 'December'
# ]
# table=pd.DataFrame(data,index=months)
# # print(table) Printing data in table
# print(table.loc['May'])
# dataz=pd.read_csv('data.csv',index_col=0)
# print(dataz)
# print(dataz.head(2))
# print(dataz.info())
# print(dataz.shape)
dataz=pd.read_csv('movie.csv',index_col=1)
# print(dataz)
#print(dataz.head())
# print(dataz.info())
print(dataz.shape)
print(dataz.drop_duplicates(inplace=True,keep='last'))
dataz.rename(columns={'Runtime (Minutes)':'Runtime','Revenue (Millions)':'Revenue'},inplace=True)
# dataz.columns=[col.lower()for col in dataz]
# for i in dataz:
#     print(i)   
# print(dataz.info())
# print(dataz.isnull().sum())
# print(dataz.dropna())
# print(dataz['Revenue'])
# print(dataz['Revenue'].describe())
# print(dataz['Genre'].describe())
# print(dataz['Genre'].value_counts().head(10))
print(dataz.corr())