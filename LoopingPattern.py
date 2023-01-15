# for i in range(1,11):
#     print(i)
# for i in range(1,11):
#     print(i,end='*')
# word=input('word:')
# length=len(word)
# for i in range(0,length):
#     print(word[0:i+1])
# for i in range(0,length):
#     for j in range(0,i+1):
#         print(word[i],end=' ')
#     print()
# for i in range(0,length):
#     print(end=' '*(length-i))
#     print(word[0:i+1])
# line=int(input('line:'))
# for i in range(0,line*2-1):
#     if i<5:
#         print(' '*(line-i),'* '*(i+1))
#     else:
#         print(' '*(i-line+2),'* '*((i-(i-line+(i-line-1)))-2))
# def sum(a,b):
#     return sum(a,b)
# sum(4,4)
# line=int(input('line:'))
# for i in range(0,line-1):
#     print(' '*(line-i),'* '*(i+1))
# line2=line-1
# for i in range(line-1,-1,-1):
#     print(' '*(line-i),'* '*(i+1))
line=int(input('line:'))
for i in range(0,line-1):
    print('* '*(i+1))
line2=line-1
for i in range(line-1,-1,-1):
    print('* '*(i+1))