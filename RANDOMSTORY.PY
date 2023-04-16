import random as r
starter=['It was the first day of school ','It was a dark and stormy night ','Once upon a time ']
character=['Jane was all alone.','John had always been fascinated by space.','Rachel was nervous about fitting in with her new classmates.']
time=['One day ','One time ','One night ']
activity=['he/she never expected to find himself stranded ','he/she never expected to find herself in the middle of a mystery involving a missing teacher ','he/she was selected to be part of a crew on a mission to Mars ']
place=['in an old creaky house ','in her home ','in a foreign country ']
age=['It happend when he/she was 15 years old ','It happend when he/she was at school ','It happend when he/she was very young ']
story=r.choice(2*starter)+r.choice(2*character)+r.choice(2*time)+r.choice(2*activity)+r.choice(2*place)+r.choice(2*age)
print(story)