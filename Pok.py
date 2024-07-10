import random, time, sys

Enemy_Health = 100
Your_Health = 10
Move_list = ["A", "B", "C", "D"]
Damage_Delt = [10, 20, 30, 40]
Pokemon_Enemy = random.choice(Move_list)
x = 1
if Pokemon_Enemy == "A":
    print("You encountered a wild Pikachu")
elif Pokemon_Enemy == "B":
    print("You encountered a wild Bulbasaur")
elif Pokemon_Enemy == "C":
    print("You encountered a wild Charmander")
elif Pokemon_Enemy == "D":
    print("You encountered a wild Squirtle")
time.sleep(2)
Pokemon = input("Enter answer as a capital letter\nA. Pikachu\nB. Bulbasaur\nC. Charmander\nD. Squirtle\n")



while Your_Health > 0:
    if Pokemon == "A":
            Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock Wave\n")
            y = 1
            if Moveset == "A":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Thunder"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "B":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Volt Tackle"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "C":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Electro Ball"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "D":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Shock Wave"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            else:
                y = 2
                while y == 2:
                    print("Invalid Answer")
                    y = 1
                    Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock Wave\n")
                    if Moveset == "A":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Thunder"
                    elif Moveset == "B":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Volt Tackle"
                    elif Moveset == "C":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Electro Ball"
                    elif Moveset == "D":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Shock Wave"
                    else:
                        y = 2
                    print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            if Pokemon_Enemy == "A":
                moveset = random.choice(Move_list)
                print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Thunder"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Volt Tackle"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Electro Ball"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Shock Wave"
                else:
                    y = 2
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "B":
                moveset = random.choice(Move_list)
                print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Vine Whip"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Energy Ball"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Leaf Blade"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Razor Leaf"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "C":
                moveset = random.choice(Move_list)
                print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Flamethrower"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Will-o-Wisp"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Overheat"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Fire Punch"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "D":
                moveset = random.choice(Move_list)
                print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Hydro Pump"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Surf"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Scald"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Aqua Tail"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
            if Enemy_Health <= 0:
                break

    elif Pokemon == "B":
            Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf\n")
            y = 1
            if Moveset == "A":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Vine Whip"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "B":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Energy Ball"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "C":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Leaf Blade"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "D":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Razor Leaf"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            else:
                y = 2
                while y == 2:
                    print("Invalid Answer")
                    y = 1
                    Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf\n")
                    if Moveset == "A":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Vine Whip"
                    elif Moveset == "B":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Energy Ball"
                    elif Moveset == "C":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Leaf Blade"
                    elif Moveset == "D":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Razor Leaf"
                    else:
                        y = 2
                    print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            if Pokemon_Enemy == "A":
                moveset = random.choice(Move_list)
                print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Thunder"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Volt Tackle"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Electro Ball"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Shock Wave"
                else:
                    y = 2
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "B":
                moveset = random.choice(Move_list)
                print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Vine Whip"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Energy Ball"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Leaf Blade"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Razor Leaf"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "C":
                moveset = random.choice(Move_list)
                print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Flamethrower"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Will-o-Wisp"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Overheat"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Fire Punch"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "D":
                moveset = random.choice(Move_list)
                print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Hydro Pump"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Surf"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Scald"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Aqua Tail"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
            if Enemy_Health <= 0:
                break
    elif Pokemon == "C":
            Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch\n")
            y = 1
            if Moveset == "A":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Flamethrower"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "B":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Will-o-Wisp"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "C":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Overheat"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "D":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Fire Punch"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            else:
                y = 2
                while y == 2:
                    print("Invalid Answer")
                    y = 1
                    Moveset = input("Enter answer as a capital letter\nA. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch\n")
                    if Moveset == "A":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Flamethrower"
                    elif Moveset == "B":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Will-o-Wisp"
                    elif Moveset == "C":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Overheat"
                    elif Moveset == "D":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Fire Punch"
                    else:
                        y = 2
                    print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            if Pokemon_Enemy == "A":
                moveset = random.choice(Move_list)
                print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Thunder"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Volt Tackle"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Electro Ball"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Shock Wave"
                else:
                    y = 2
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "B":
                moveset = random.choice(Move_list)
                print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Vine Whip"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Energy Ball"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Leaf Blade"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Razor Leaf"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "C":
                moveset = random.choice(Move_list)
                print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Flamethrower"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Will-o-Wisp"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Overheat"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Fire Punch"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "D":
                moveset = random.choice(Move_list)
                print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Hydro Pump"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Surf"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Scald"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Aqua Tail"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
            if Enemy_Health <= 0:
                break
    elif Pokemon == "D":
            Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail\n")
            y = 1
            if Moveset == "A":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Hydro Pump"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "B":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Surf"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "C":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Scald"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            elif Moveset == "D":
                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                Moveset = "Aqua Tail"
                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            else:
                y = 2
                while y == 2:
                    print("Invalid Answer")
                    y = 1
                    Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail\n")
                    if Moveset == "A":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Hydro Pump"
                    elif Moveset == "B":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Surf"
                    elif Moveset == "C":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Scald"
                    elif Moveset == "D":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Aqua Tail"
                    else:
                        y = 2
                    print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
            if Pokemon_Enemy == "A":
                moveset = random.choice(Move_list)
                print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Thunder"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Volt Tackle"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Electro Ball"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Shock Wave"
                else:
                    y = 2
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "B":
                moveset = random.choice(Move_list)
                print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Vine Whip"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Energy Ball"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Leaf Blade"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Razor Leaf"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "C":
                moveset = random.choice(Move_list)
                print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Flamethrower"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Will-o-Wisp"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Overheat"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Fire Punch"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

            elif Pokemon_Enemy == "D":
                moveset = random.choice(Move_list)
                print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                time.sleep(2)
                if moveset == "A":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Hydro Pump"
                elif moveset == "B":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Surf"
                elif moveset == "C":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Scald"
                elif moveset == "D":
                    Your_Health = Your_Health - random.choice(Damage_Delt)
                    moveset = "Aqua Tail"
                print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
            if Enemy_Health <= 0:
                break
    else:
        x = 2
        while x == 2:
            Pokemon = input("Enter answer as a capital letter\nA. Pikachu\nB. Bulbasaur\nC. Charmander\nD. Squirtle\n")
            x = 1
            if Pokemon == "A":
                    Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock Wave\n")
                    y = 1
                    if Moveset == "A":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Thunder"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "B":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Volt Tackle"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "C":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Electro Ball"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "D":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Shock Wave"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    else:
                        y = 2
                        while y == 2:
                            print("Invalid Answer")
                            y = 1
                            Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock Wave\n")
                            if Moveset == "A":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Thunder"
                            elif Moveset == "B":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Volt Tackle"
                            elif Moveset == "C":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Electro Ball"
                            elif Moveset == "D":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Shock Wave"
                            else:
                                y = 2
                            print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    if Pokemon_Enemy == "A":
                        moveset = random.choice(Move_list)
                        print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Thunder"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Volt Tackle"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Electro Ball"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Shock Wave"
                        else:
                            y = 2
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "B":
                        moveset = random.choice(Move_list)
                        print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Vine Whip"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Energy Ball"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Leaf Blade"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Razor Leaf"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "C":
                        moveset = random.choice(Move_list)
                        print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Flamethrower"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Will-o-Wisp"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Overheat"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Fire Punch"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "D":
                        moveset = random.choice(Move_list)
                        print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Hydro Pump"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Surf"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Scald"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Aqua Tail"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
                    if Enemy_Health <= 0:
                        break

            elif Pokemon == "B":
                    Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf\n")
                    y = 1
                    if Moveset == "A":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Vine Whip"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "B":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Energy Ball"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "C":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Leaf Blade"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "D":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Razor Leaf"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    else:
                        y = 2
                        while y == 2:
                            print("Invalid Answer")
                            y = 1
                            Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf\n")
                            if Moveset == "A":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Vine Whip"
                            elif Moveset == "B":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Energy Ball"
                            elif Moveset == "C":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Leaf Blade"
                            elif Moveset == "D":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Razor Leaf"
                            else:
                                y = 2
                            print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    if Pokemon_Enemy == "A":
                        moveset = random.choice(Move_list)
                        print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Thunder"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Volt Tackle"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Electro Ball"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Shock Wave"
                        else:
                            y = 2
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "B":
                        moveset = random.choice(Move_list)
                        print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Vine Whip"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Energy Ball"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Leaf Blade"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Razor Leaf"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "C":
                        moveset = random.choice(Move_list)
                        print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Flamethrower"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Will-o-Wisp"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Overheat"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Fire Punch"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "D":
                        moveset = random.choice(Move_list)
                        print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Hydro Pump"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Surf"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Scald"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Aqua Tail"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
                    if Enemy_Health <= 0:
                        break
            elif Pokemon == "C":
                        Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch\n")
                        y = 1
                        if Moveset == "A":
                            Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                            Moveset = "Flamethrower"
                            print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                        elif Moveset == "B":
                            Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                            Moveset = "Will-o-Wisp"
                            print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                        elif Moveset == "C":
                            Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                            Moveset = "Overheat"
                            print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                        elif Moveset == "D":
                            Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                            Moveset = "Fire Punch"
                            print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                        else:
                            y = 2
                            while y == 2:
                                print("Invalid Answer")
                                y = 1
                                Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch\n")
                                if Moveset == "A":
                                    Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                    Moveset = "Flamethrower"
                                elif Moveset == "B":
                                    Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                    Moveset = "Will-o-Wisp"
                                elif Moveset == "C":
                                    Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                    Moveset = "Overheat"
                                elif Moveset == "D":
                                    Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                    Moveset = "Fire Punch"
                                else:
                                    y = 2
                                print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                        if Pokemon_Enemy == "A":
                            moveset = random.choice(Move_list)
                            print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                            time.sleep(2)
                            if moveset == "A":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Thunder"
                            elif moveset == "B":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Volt Tackle"
                            elif moveset == "C":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Electro Ball"
                            elif moveset == "D":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Shock Wave"
                            else:
                                y = 2
                            print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                        elif Pokemon_Enemy == "B":
                            moveset = random.choice(Move_list)
                            print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                            time.sleep(2)
                            if moveset == "A":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Vine Whip"
                            elif moveset == "B":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Energy Ball"
                            elif moveset == "C":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Leaf Blade"
                            elif moveset == "D":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Razor Leaf"
                            print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                        elif Pokemon_Enemy == "C":
                            moveset = random.choice(Move_list)
                            print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                            time.sleep(2)
                            if moveset == "A":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Flamethrower"
                            elif moveset == "B":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Will-o-Wisp"
                            elif moveset == "C":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Overheat"
                            elif moveset == "D":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Fire Punch"
                            print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                        elif Pokemon_Enemy == "D":
                            moveset = random.choice(Move_list)
                            print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                            time.sleep(2)
                            if moveset == "A":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Hydro Pump"
                            elif moveset == "B":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Surf"
                            elif moveset == "C":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Scald"
                            elif moveset == "D":
                                Your_Health = Your_Health - random.choice(Damage_Delt)
                                moveset = "Aqua Tail"
                            print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
                        if Enemy_Health <= 0:
                            break
            elif Pokemon == "D":
                    Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail\n")
                    y = 1
                    if Moveset == "A":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Hydro Pump"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "B":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Surf"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "C":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Scald"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    elif Moveset == "D":
                        Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                        Moveset = "Aqua Tail"
                        print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    else:
                        y = 2
                        while y == 2:
                            print("Invalid Answer")
                            y = 1
                            Moveset = input("What move would you like to use?\nEnter answer as a capital letter\nA. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail\n")
                            if Moveset == "A":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Hydro Pump"
                            elif Moveset == "B":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Surf"
                            elif Moveset == "C":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Scald"
                            elif Moveset == "D":
                                Enemy_Health = Enemy_Health - random.choice(Damage_Delt)
                                Moveset = "Aqua Tail"
                            else:
                                y = 2
                            print(f"You used {Moveset}. The other pokemon's health is now {Enemy_Health}")
                    if Pokemon_Enemy == "A":
                        moveset = random.choice(Move_list)
                        print("A. Thunder\nB. Volt Tackle\nC. Electro Ball\nD. Shock")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Thunder"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Volt Tackle"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Electro Ball"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Shock Wave"
                        else:
                            y = 2
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "B":
                        moveset = random.choice(Move_list)
                        print("A. Vine Whip\nB. Energy Ball\nC. Leaf Blade\nD. Razor Leaf")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Vine Whip"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Energy Ball"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Leaf Blade"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Razor Leaf"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "C":
                        moveset = random.choice(Move_list)
                        print("A. Flamethrower\nB. Will-o-Wisp\nC. Overheat\nD. Fire Punch")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Flamethrower"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Will-o-Wisp"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Overheat"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Fire Punch"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")

                    elif Pokemon_Enemy == "D":
                        moveset = random.choice(Move_list)
                        print("A. Hydro Pump\nB. Surf\nC. Scald\nD. Aqua Tail")
                        time.sleep(2)
                        if moveset == "A":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Hydro Pump"
                        elif moveset == "B":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Surf"
                        elif moveset == "C":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Scald"
                        elif moveset == "D":
                            Your_Health = Your_Health - random.choice(Damage_Delt)
                            moveset = "Aqua Tail"
                        print(f"The other pokemon used {moveset}. Your pokemon's health is now {Your_Health}")
                    if Enemy_Health <= 0:
                        break
            else:
                x = 2
                print("Invalid Option")

if Enemy_Health > Your_Health:
    print("You lost", end="")
    sys.stdout.flush()
    time.sleep(1)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(1)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(1)
    print(".")
    print("The pokemon ran away", end="")
    sys.stdout.flush()
    time.sleep(1)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(1)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(1)
    print(".")
elif Your_Health > Enemy_Health:
    print("You won!")
else:
    print("It's a tie!")