import random

jackpot=random.randint(1,100)

number=int(input("Guess your number"))
count=1

while number!=jackpot:
    if number<jackpot:
        print('Galat hai, upar guess karo')
    else:
        print('Galat hai, neeche guess karo')


    number=int(input("Guess kar fir se"))
    count=count+1


print("sahi jawab")
print("No of attempts" ,count)
