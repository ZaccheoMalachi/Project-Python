from maskpass import askpass
from random import choice
qNa={
    "What is the capital of Spain?": "Madrid",
    "Who wrote the novel 'Pride and Prejudice' ?": "Jane Austen",
    "What is the symbol for Oxygen?": "O",
    "In what year did World War II end?": "1945",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Who painted the 'Starry Night'": "Vincent van Gogh",
    "What is the capital of Australia?": "Canberra",
    "Who played the role of Harry Potter in the film series?":"Daniel Radcliffe",
    "What is the most abundant gas in Earth's atmosphere?":"Nitrogen",
    "What is the largest known star in the universe?": "UY Scuti",
    "What is the name of the protein that forms the shell of the SARS-CoV-2 virus?": "Spike protein",
    "What is the name of the largest known galaxy?": "IC 1101",
    "What is the name of the smallest known mammal?": "Bumblebee bat",
    "What is the name of the largest known fish?": "Whale shark",
    "What is the name of the largest known volcano on Earth?": "Mauna Loa",
    "What is the name of the longest known river in the world?": "Nile",
    "What is the name of the highest known point on Earth?": "Mount Everest",
    "What is the name of the deepest known point in the ocean?": "Challenger Deep",
    "What is the name of the largest known desert on Earth?": "Antarctica",
    "What is the name of the oldest known tree in the world?": "Methuselah",
    "What is the name of the largest known canyon in the solar system?": "Valles Marineris",
    "What is the name of the largest known galaxy cluster?": "Abell 2744",
    "What is the name of the largest known asteroid in our solar system?": "Ceres",
    "What is the name of the largest known organism on Earth?": "Armillaria ostoyae",
    "What is the name of the largest known subatomic particle?": "Higgs boson",
    "What is the name of the largest known black hole?": "TON 618",
    "What is the capital of China?": "Beijing",
    "Which is the smallest country in the world?": "Vatican City",
    "What is the largest desert in the world?": "Antarctica",
    "What is the highest point on Earth?": "Mount Everest",
    "Who wrote the famous novel 'The Great Gatsby'": "F. Scott Fitzgerald",
    "What is the capital of Russia?": "Moscow",
    "What is the largest mammal in the world?": "Blue Whale",
    "In what year was the Declaration of Independence signed?": "1776",
    "Which is the longest river in the world?": "Nile",
    "What is the capital of India?": "New Delhi",
    "Which planet is known as the 'Red Planet'?": "Mars",
    "What is the national bird of the United States?": "American Bald Eagle",
    "In what year was the World Wide Web invented?": "1989",
    "What is the capital of Japan?": "Tokyo",
    "What is the capital of Canada?": "Ottawa",
    "What is the capital of Germany?": "Berlin",
    "What is the capital of Italy?": "Rome",
    "What is the capital of Spain?": "Madrid",
    "What is the capital of France?": "Paris",
    "What is the capital of Australia?": "Canberra",
    "What is the capital of Brazil?": "Brasília",
    "What is the capital of Mexico?": "Mexico City",
    "What is the capital of Argentina?": "Buenos Aires",
    "What is the capital of South Africa?": "Pretoria",
    "What is the capital of Egypt?": "Cairo",
    "What is the capital of Greece?": "Athens"
}
uAp = {
    "jim": "password1",
    "orman": "password2",
    "xavier": "password3",
    "bob": "password4",
    "tommy": "password5",
    "thomas": "password6",
    "jerry": "password7",
    "shawn": "password8",
    "tim": "password9",
    "mark": "password10"
}
login=False
print('please login to play theinfinite quiz')
username=input('user:').lower()
password=askpass('pass:')
if username in uAp:
    if uAp[username]==password:
        login=True      
if login:
    print('login is done')
    print('welcome',username)
    score=0
    while True:
        question=(choice(list(qNa.keys())))
        answer=qNa[question]
        # print(question)
        if input(question).lower()==answer.lower():
            print('GOOD!')
            score+=10
        else:
            print('NOGOOD!')
            break
    print('YOU LOSE!!')
    print('Score:',score)
else:
    print('login failed')