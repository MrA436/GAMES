import random

def disaster_simulator():
    health = 100
    rounds = 0  # renamed from 'round'
    disasters = ["Earthquake", "Food Wars", "alien invasion"]
    print("You will get 3 choices to choose from: hide, fight, do nothing.")
    
    while health > 0:
        selected_disaster = random.choice(disasters)
        print(f"\nA {selected_disaster} has occurred!")
        
        while True: 
            choice = input("Enter your choice (hide, fight, do nothing): ").lower()
            
            if selected_disaster == "Earthquake":
                if choice == "hide":
                    print("You found a safe spot and survived the earthquake! 😎")
                    break
                elif choice == "fight":
                    health -= 50
                    print("Bro for real? how are you planning to fight a fxking EARTHQUAKE? 🙄")
                    print("health:", health)
                    break
                elif choice == "do nothing":
                    health -= 70
                    print("You don't love yourself do you? there's an fxing earthquake and you decided to eat 5star? 😑")
                    print("health:", health)
                    break
                else:
                    print('''if you can't even type "hide, fight, or do nothing"? what are you doing with a PC?''')
            
            elif selected_disaster == "Food Wars":
                if choice == "hide":
                    print("Why are you hiding? Are you scared of food? 😐")
                    break
                elif choice == "fight":
                    print("Whom will you fight with? A pumpkin? 😒")
                    break
                elif choice == "do nothing":
                    health = 100
                    print("Your health restored as you found asian food. 😍")
                    break
                else:
                    print("Bro come on can't you just type (hide, fight, or do nothing.)?")
            
            elif selected_disaster == "alien invasion":
                if choice == "hide":
                    health -= 30
                    print("Bro why do you think you can hide from aliens? 😂")
                    print("health:", health)
                    break
                elif choice == "fight":
                    health -= 80
                    print("You were trynna impress your crush by fighting aliens right? you are such a simp 😐")
                    print("health:", health)
                    break
                elif choice == "do nothing":
                    health -= 100
                    print("The aliens BDSMed you after changing you gender. ☠")
                    print("health:", health)
                    break
                else:
                    print("""if you can't even type "hide, fight, or do nothing" why are you even using a Computer?.""")
        
        # increment rounds **after a valid action**, i.e., after inner loop breaks
        rounds += 1
        print(f"Disasters survived so far: {rounds}")
        
        if health <= 0:
            print("\nGame Over. You died.")
            print(f"You survived {rounds} disasters!")
            break

disaster_simulator()
