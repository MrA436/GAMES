import random as r
def number_guesser():
    a= r.randint(1,100)

    while True:
        b=int(input('choose a number between 1 and 100: '))
        if a==b:
            print('you won!')
            break
        elif a > b:
            print('too low, try again')
        else:
            print('too high, try again')

while True:
    number_guesser()
    c=input('try again? (y/n): ').lower()
    if c !='y':
        print('thanks for playing!')
        break
    
        


























































































