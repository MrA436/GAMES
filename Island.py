def game():
    def start():
        print("🏝️ Welcome to Treasure Island!")
        print("Your mission is to find the treasure.")
        crossroads()
    
    def crossroads():
        c1 = input('you arrive at a crossroad where do u want to go?(left/right): ').lower()
        if c1 == 'left':
            print('you found a lake!')
            lake()
        else:
            print('you got took as a prisioner by tribesmen! Game Over')
            return

    def lake():
        c2 = input('you arrive at a lake. (wait/swim): ').lower()
        if c2 == 'wait':
            print('a boat took you and you arrived at the treasure island')
            island()
        else:
            print('you got eaten by crocodile! Game Over')
            return

    def island():
        c3 = input('you see two doors where do u wanna go? (left/right): ').lower()
        if c3 =='left':
            print('you won!')
        else:
            print('you died because the room was filled with poison gas! Game Over')    
            return

    start()

while True:
    game()
    c = input('try again? (y/n): ')
    if c!= 'y':
        print('thanks for playing!')
        break 
