from maskpass import *

users={
        'admin':{
            'pass':'adminjoethegreat2.&*',
            'role':'administrator',
            'nick':'Joe2.0'
            },
        'coadmin':{
            'pass':'adminbin132$@8',
            'role':'administrator',
            'nick':'Bin'
            },
        'member1':{
            'pass':'hole241@#!',
            'role':'member',
            'nick':'HumanOMG'
            },
        }
def adduser(id,password,roleuser,nick):
    users.update({id,{
            'pass':password,
            'role':roleuser,
            'nick':nick}})
def login(u,p):
    success=False
    for i in users.values():
        if u==i['nick']:
            success=True
            if p==i['pass']:
                print('Login Successful')
                return i['role']
            else:
                print('Wrong Password')
    if not success:
        print('User Not Found')
u=input('username:')
p=askpass('password:')
role=login(u,p)
while True:
    def admin(role):
        if role!='administrator':
            print('You Dont Have Access!')
            return 0
        print('Welcome to Administrator Menu:')
        print('1.Add User')
        print('2.Delete User')
        print('3.Print User')
        choice=input('Pick:')
        if choice=='1':
            id=input('id:')
            nick=input('username:')
            password=input('password:')
            if input('administrator(y/n):')=='y':
                roleuser='administrator'
            else:
                roleuser='member'
            adduser(id,password,roleuser,nick)
        elif choice=='3':
            print(users)
    admin(role)
    exit=input('Exit?(y/n):')
    if exit=='y':
        break