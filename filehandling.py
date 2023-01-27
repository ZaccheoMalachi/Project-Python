# # # jimn=open('file.txt','r')
# # # print(jimn.read())
# # # jimn=open('file.txt','a')
# # # jimn.write('\ncool')
# # # print(jimn.read())
# # jimn=open('file.txt','r')
# # # while(True):
# # #     text=jimn.readline()
# # #     if text!='':
# # #          print(text,end="")
# # #     else:
# # #         break
# # print(jimn.readlines())
# # jimn=open('file2.txt','x')
# from os import *
# if path.exists('jimn'):
#     rmdir('jimn')
# else:
#     print('folder not found')
wordToFind=input('enter word to find in text==')
openText=open('file.txt','r')
data=openText.read()
data=data.split()
counter=0
for i in data:
    if i.lower()==wordToFind.lower():
        counter+=1
print('There are',counter,wordToFind,'in text')