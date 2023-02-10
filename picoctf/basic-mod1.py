mmsg=[54 ,396 ,131 ,198 ,225 ,258 ,87 ,258 ,128 ,211 ,57 ,235, 114 ,258 ,144 ,220 ,39 ,175 ,330,338,297,288]
mods=[]
char=[]
for j in range(65,91):
    char.append(chr(j))
for j in range(48,58):
    char.append(chr(j))
char.append('_')
# print(char)
for i in mmsg:
    mods.append(i%37)
# print(mods)
result=''
for i in mods:
    result+=char[i]
print(result)