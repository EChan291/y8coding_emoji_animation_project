from time import sleep

heart = "💗"

for i in range(10):
    print(i * heart)
    sleep(0.1)

for f in range(10):
    print(heart * (10 - f))
    sleep(0.1)

for y in range(3, 31, 3):
    print(y,y * heart)
    sleep(0.1)
for x in range(30, 2, -3):
    print(x,x * heart)
    sleep(0.1)