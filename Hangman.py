import random
from wonderwords import *
word=RandomWord()
senteces=RandomSentence()
# print(senteces.simple_sentence())
# print(word.word())
# print(word.word(starts_with="a",ends_with='h'))
# print(word.word(include_categories=['adjective']))
randomWords=word.word()
lives=5
# print(randomWords)
print('_ '*len(randomWords))
exitrno=''
result=''
while True:
    letter=str(input('guess the letter:'))
    if letter not in randomWords:
        lives-=1
    print('Lives=',lives)
    for i in randomWords:
        if i==letter or (i in result):
            print(i,end=' ')
            if i not in result:
                result+=i
        else:
            print('_',end=' ')
    print()
    # print(result)
    if len(result)==len(randomWords):
        print('You Won!')
        exitrno=input('try again?yes/no:')
        if exitrno=='no':
            break
        if exitrno=='yes':
            randomWords=word.word()
            lives=5
            result=''
    if lives==0:
        print('You lose the answer is',randomWords)
        exitrno=input('try again?yes/no:')
        if exitrno=='no':
            break
        if exitrno=='yes':
            randomWords=word.word()
            lives=5
            result=''