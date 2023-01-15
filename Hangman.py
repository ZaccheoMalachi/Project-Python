import random
word=['house','person','studio','dog','tree','happy','water','sun','small','yellow']
randomWords=random.choice(word)
# print(randomWords)
print('_ '*len(randomWords))
result=''
while True:
    letter=str(input('guess the letter:'))
    for i in randomWords:
        if i==letter or (i in result):
            print(i,end=' ')
            if i not in result:
                result+=i
        else:
            print('_',end=' ')
    print()
    print(result)
    if len(result)==len(randomWords):
        print('You Won!')
        break