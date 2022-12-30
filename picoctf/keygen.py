from hashlib import *
user=b'FREEMAN'
dinamic=''
process=sha256(user).hexdigest()
dinamic+=process[4]
dinamic+=process[5]
dinamic+=process[3]
dinamic+=process[6]
dinamic+=process[2]
dinamic+=process[7]
dinamic+=process[1]
dinamic+=process[8]
print('picoCTF{1n_7h3_|<3y_of_'+dinamic+'}')
