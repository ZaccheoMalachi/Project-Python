flag='灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽'
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
step1=[]
for i in flag:
    step1.append(ord(i))
print(chr((ord('c') << 8) + ord("o")))
step2=[]
for j in step1:
    for i in range(127):
        step2.append(j-ord(chr(i)))